var e=function(e){return e.getAttribute("data-target")&&document.getElementById(e.getAttribute("data-target").replace("#",""))},t=function(e){return 1e3*window.getComputedStyle(e).getPropertyValue("transition-duration").replace("s","")+1},o=function(e,t,o){t.forEach((function(t){e.addEventListener(t,o)}))},n=function(e,t,o){return function(){return document.querySelectorAll(e).forEach((function(e){e.addEventListener(t,(function(){return o(e)}))}))}};const i=n('[data-toggle="accordion"]',"click",(function(e){var o=e.closest(".accordion-item").querySelector(".accordion-collapse"),n=t(o);if(o.style.overflow="hidden",o.style.height=0,"true"===e.getAttribute("aria-expanded"))return e.setAttribute("aria-expanded","false"),o.classList.remove("show"),void window.setTimeout((function(){o.classList.remove("block"),o.classList.add("hidden")}),n);e.setAttribute("aria-expanded","true"),o.classList.add("block"),o.classList.add("show"),o.classList.remove("hidden"),window.setTimeout((function(){o.style.height=o.scrollHeight+"px"}),33),window.setTimeout((function(){o.style.overflow=""}),n)}));const r=n("[data-dismiss]","click",(function(o){var n=e(o);n||(n=o.closest(".".concat(o.getAttribute("data-dismiss")))),n.classList.add("opacity-0"),setTimeout((function(){return n.remove()}),t(n))}));const a=n('[data-toggle="collapse"]',"click",(function(o){var n=e(o);if(n){var i=t(n);if(n.style.overflow="hidden",n.style.height=0,"true"===o.getAttribute("aria-expanded"))return o.setAttribute("aria-expanded","false"),n.classList.remove("show"),void window.setTimeout((function(){return n.classList.remove("block")}),i);o.setAttribute("aria-expanded","true"),n.classList.add("block"),n.classList.add("show"),window.setTimeout((function(){n.querySelectorAll(".dropdown-menu").forEach((function(e){return e.classList.add("hidden")}));var e=n.scrollHeight;n.querySelectorAll(".dropdown-menu").forEach((function(e){return e.classList.remove("hidden")})),n.style.height=e+"px"}),32),window.setTimeout((function(){return n.style.overflow=""}),i)}})),c=function(){return document.querySelectorAll('[data-toggle="dropdown"]').forEach((function(e){var t,n=e.nextSibling.nextSibling;function i(){n.classList.remove("show"),window.setTimeout((function(){n.classList.remove("block")}),300)}o(e,["click"],(function(){n.className.includes("show")?i():(n.classList.add("block"),window.setTimeout((function(){n.classList.toggle("show")}),50))})),o(e,["focus","mouseenter"],(function(){var t=Popper.createPopper(e,n,{placement:"bottom-start",modifiers:[{name:"offset",options:{offset:[0,10]}}]});n.classList.add("block"),t.forceUpdate(),t.update(),window.setTimeout((function(){n.getAttribute("class").includes("show")||n.classList.remove("block")}),50)})),o(e,["blur","mouseleave"],(function(){n.getAttribute("class").includes("show")||n.classList.remove("block")})),t=i,document.addEventListener("keydown",(function(e){"Escape"===e.key&&t()}));document.body.addEventListener("click",(function(t){var o=t.target;o===n||o===e||e.contains(o)||i()}))}))};var s="fixed right-0 top-0 z-50 text-white px-5 close";window.removeModal=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"v-modal",t=document.getElementById(e);t.classList.remove("opacity-100"),window.setTimeout((function(){t.remove(),document.body.style.overflow=""}),500)};const l=n('[data-toggle="modal"]',"click",(function(e){var t=function(e){var t=e.dataset.options;return t?JSON.parse(t.replaceAll("'",'"')):{}}(e),o=t.size,n=t.beforeShown,i=t.id||"v-modal",r=e.dataset.html||"";t.imgSrc&&(r='<img src="'.concat(t.imgSrc,'">')),t.iframeSrc&&(r='<iframe allow="autoplay" class="aspect-video w-full" src="'.concat(t.iframeSrc,'" allowfullscreen="" autoplay=""></iframe>'));var a,c,l='<div class="modal" id="'.concat(i,'">\n  <div class="modal-content ').concat(o?"modal-".concat(o):"",'">\n    ').concat(r,"\n  </div>\n\n  <button onclick=\"removeModal('").concat(i,'\')" type="button" class="').concat(s,'" data-dismiss="modal" aria-label="Close">\n    <span class="text-4xl" aria-hidden="true">&times;</span>\n  </button>\n\n  <div class="modal-bg" onclick="removeModal(\'').concat(i,"')\"></div>\n</div>\n");document.addEventListener("keydown",(function(e){return 27==e.keyCode&&window.removeModal(i)})),document.body.style.overflow="hidden",document.body.insertAdjacentHTML("beforeend",l),(a="#"+i,c=document,new Promise((function(e){if(c.querySelector(a))return e(c.querySelector(a));var t=new MutationObserver((function(o){c.querySelector(a)&&(e(c.querySelector(a)),t.disconnect())}));t.observe(c.body,{childList:!0,subtree:!0})}))).then((function(e){n&&window[n](),window.setTimeout((function(){return e.classList.add("opacity-100")}),32)}))}));function d(e,t){(null==t||t>e.length)&&(t=e.length);for(var o=0,n=new Array(t);o<t;o++)n[o]=e[o];return n}function u(e){return function(e){if(Array.isArray(e))return d(e)}(e)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(e)||function(e,t){if(e){if("string"==typeof e)return d(e,t);var o=Object.prototype.toString.call(e).slice(8,-1);return"Object"===o&&e.constructor&&(o=e.constructor.name),"Map"===o||"Set"===o?Array.from(e):"Arguments"===o||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(o)?d(e,t):void 0}}(e)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}const f=n('[role="tab"]',"click",(function(e){if("true"===e.getAttribute("aria-selected"))return null;var t=document.querySelector('[aria-labelledby="'.concat(e.getAttribute("aria-controls"),'"]'));if(!t)return null;for(var o=e.classList.value,n=e.parentNode;n&&"tablist"!==n.getAttribute("role");)n=n.parentNode;var i=n.querySelectorAll('[aria-selected="true"]');if(!i||0===i.length)return null;var r=i[0].classList.value;n.querySelectorAll('[role="tab"]').forEach((function(e){e.classList=o,e.setAttribute("aria-selected","false")})),e.classList=r,e.setAttribute("aria-selected","true"),"tabcontent"!==t.getAttribute("role")?(u(t.parentNode.children).forEach((function(e){"tabpanel"===e.getAttribute("role")&&e.classList.add("hidden")})),t.classList.remove("hidden")):u(t.children).forEach((function(e){"tabpanel"===e.getAttribute("role")&&e.classList.remove("hidden")}))}));window.vInitialized=!1,window.initializeVUI=function(){window.vInitialized||(window.vInitialized=!0,i(),a(),r(),c(),l(),f(),window.addEventListener("resize",(function(){document.querySelectorAll('[data-toggle="collapse"]').forEach((function(t){var o=e(t);o&&(t.setAttribute("aria-expanded","false"),o.classList.remove("show"),o.classList.remove("block"),o.style.height="auto",o.style.overflow="")}))})))},document.addEventListener("DOMContentLoaded",initializeVUI),"loading"!==document.readyState&&initializeVUI();
//# sourceMappingURL=versoly-ui.js.map