import logging
from django.conf import settings
from django.db import models
from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from modelcluster.contrib.taggit import ClusterTaggableManager

from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase, TagBase, ItemBase
from wagtail import blocks
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.images.blocks import ImageChooserBlock

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
from wagtail.search import index
from wagtailcodeblock.blocks import CodeBlock

logger = logging.getLogger(__name__)


class BlogIndexPage(Page):
    subpage_types = ['blog.BlogPage', 'blog.TagPage']
    sub_heading = models.CharField(max_length=255, blank=True, default='')
    content_panels = [
        FieldPanel('title'),
        FieldPanel('sub_heading'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Add extra variables and return the updated context
        all_posts = BlogPage.objects.child_of(self).live().order_by('-first_published_at')
        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            all_posts = all_posts.filter(tags__name=tag)

        paginator = Paginator(all_posts, 8)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        context['blog_entries'] = posts
        return context


class BlogPage(Page):
    # Database fields
    intro = models.TextField(blank=True, default='')
    show_toc = models.BooleanField(
        default=True,
        verbose_name="Show Table of Contents")

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('code', CodeBlock()),
    ])
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True, null=True,
        verbose_name='Author',
        on_delete=models.SET_NULL,
        related_name='author_pages',
    )
    # Search index configuration
    tags = ClusterTaggableManager(through='BlogPageTag', blank=True)
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('body', classname="full"),
        InlinePanel('related_links', label="Related links"),
        FieldPanel('tags'),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        FieldPanel('feed_image'),
    ]
    settings_panels = [
        FieldPanel('show_toc'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('go_live_at'),
                FieldPanel('expire_at'),
            ], classname="label-above"),
        ], 'Scheduled publishing', classname="publishing"),
        FieldPanel('author'),
    ]
    # Parent page / subpage type rules

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []

    def get_blog_main(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(BlogIndexPage).last().specific

    def get_tags_list(self):
        try:
            tag_page = get_object_or_404(TagPage, slug='tags')
        except Page.DoesNotExist:
            logger.warning("You need to create a 'Tags' page with 'tags' slug")
            return []
        tags = self.tags.all()
        result = [{
            "tag": tag,
            "url": tag_page.url + tag_page.reverse_subpage("tag", args=(tag.name,))
        } for tag in tags]
        return result


class BlogPageRelatedLink(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='related_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]


class TagPage(RoutablePageMixin, Page):
    def get_blog_main(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(BlogIndexPage).last().specific

    @route(r'^$')
    def main(self, request):
        tags = BlogTag.objects.all().order_by('name')

        all_tags = [{
            "tag": tag,
            "url": self.url + self.reverse_subpage("tag", args=(tag.name,))
        } for tag in tags]
        return self.render(
            request,
            template='blog/blog_tags.html',
            context_overrides={
                'all_tags': all_tags,
            })

    @route(r'^(.+)/$')
    def tag(self, request, tag):
        tag = get_object_or_404(BlogTag, name=tag)
        context = {
            'tag': tag,

        }
        all_posts = tag.tagged_posts.all()
        paginator = Paginator(all_posts, 8)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        context['blog_entries'] = posts
        return self.render(request, context_overrides=context)


class BlogTag(TagBase):
    h1 = models.CharField(
        verbose_name="h1",
        max_length=255,
        blank=True,
        default='',
    )
    seo_title = models.CharField(
        verbose_name="title tag",
        max_length=255,
        blank=True,
        default='',
        help_text="The name of the page displayed on search engine results as the clickable headline.",
    )
    seo_description = models.CharField(
        verbose_name='seo description',
        max_length=255,
        blank=True,
        default='',
        help_text="The description of the page displayed on search engine under the clickable headline.",
    )
    article = RichTextField(
        verbose_name="article",
        blank=True,
        default=''
    )

    class Meta:
        verbose_name = "Blog Tag"
        verbose_name_plural = "Blog Tags"

    panels = [
        FieldPanel('h1'),
        FieldPanel('seo_title'),
        FieldPanel('seo_description'),
        FieldPanel('article'),
    ]


class BlogPageTag(ItemBase):
    tag = models.ForeignKey(
        BlogTag, related_name="tagged_posts", on_delete=models.CASCADE
    )
    content_object = ParentalKey(
        'blog.BlogPage',
        on_delete=models.CASCADE,
        related_name='tagged_items')
