// Archivo: main.js

// LiveHelpSettings - Código para el soporte de Live Help
var LiveHelpSettings = { server: 'www.easybuypharma.com', embedded: true };

// Inicializar Foundation
$(document).foundation();

// Yandex.Metrika counter
(function (d, w, c) {
    (w[c] = w[c] || []).push(function () {
        try {
            w.yaCounter49932829 = new Ya.Metrika2({
                id: 49932829,
                clickmap: true,
                trackLinks: true,
                accurateTrackBounce: true,
                webvisor: true
            });
        } catch (e) { }
    });

    var n = d.getElementsByTagName("script")[0],
        s = d.createElement("script"),
        f = function () { n.parentNode.insertBefore(s, n); };
    s.type = "text/javascript";
    s.async = true;
    s.src = "https://mc.yandex.ru/metrika/tag.js";

    if (w.opera == "[object Opera]") {
        d.addEventListener("DOMContentLoaded", f, false);
    } else { f(); }
})(document, window, "yandex_metrika_callbacks2");

// Código para el contador de Yandex sin JavaScript
document.write('<noscript><div><img src="https://mc.yandex.ru/watch/49932829" style="position:absolute; left:-9999px;" alt="" /></div></noscript>');

// Código para descripción de productos minimizada si es vista móvil
$(document).ready(function () {
    var responsive_viewport = $(window).width();

    if (responsive_viewport < 768) {
        var minimized_elements = $('.productDescription');

        minimized_elements.each(function () {
            var t = $(this).html();
            if (t.length < 400)
                return;

            $(this).html(
                t.slice(0, 400) + '<a href="#" class="moreProductDesc"> ... Read More </a>' +
                '<div class="showContent" style="display:none; float: none; position: relative; overflow: hidden;">' + t.slice(400, t.length) + '<a href="#" class="less">Show Less</a>'
            );
        });

        $('a.moreProductDesc', minimized_elements).click(function (event) {
            event.preventDefault();
            $(this).hide().prev().hide();
            $(this).next().show();
            $('.showContent').css("display", "inline");
        });

        $('a.less', minimized_elements).click(function (event) {
            event.preventDefault();
            $(this).parent().hide().prev().show().prev().show();
        });
    }

    // Añadir clase cuando se hace scroll
    $(window).scroll(function () {
        var scroll = $(window).scrollTop();

        if (scroll >= 200) {
            $(".mainHeader").addClass("fixHeader");
        } else {
            $(".mainHeader").removeClass("fixHeader");
        }
    });

    // Scroll al hacer click en el menú
    $('.left-off-canvas-toggle').click(function () {
        $('html, body').animate({ scrollTop: $('.left-off-canvas-menu').offset().top }, 1000);
    });
    $('.right-off-canvas-toggle').click(function () {
        $('html, body').animate({ scrollTop: $('.right-off-canvas-menu').offset().top }, 1000);
    });
});

// Lazy Load para estilos CSS
function lazyLoad(script) {
    var font = document.createElement('link');
    font.type = 'text/css';
    font.rel = 'stylesheet';
    font.href = script;

    var h = document.getElementsByTagName('head')[0];
    h.appendChild(font);
}

var css = [
    'https://fonts.googleapis.com/css?family=PT+Sans+Narrow:400,700',
    'https://fonts.googleapis.com/css?family=PT+Sans:400,700',
    'https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css'
];

for (var i = 0; i < css.length; i++) {
    console.log("Lazy load: " + css[i]);
    lazyLoad(css[i]);
}

// Inicializar LazyLoad
lazyload();