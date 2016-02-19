(function($, window, document, undefined) {
    'use strict';

    var noticias = {
        infScroll: function() {
            $('.list-news').infinitescroll({
                navSelector: '.btn-load-more',
                nextSelector: '.btn-load-more',
                itemSelector: '.list-news li',
                dataType: 'html',
                animate: false,
                loading: {
                    img: 'assets/img/ajax-loader.gif',
                    finishedMsg: '<span class="txt-loader">Não há mais registros.</span>'
                },
                path: function() {
                    return 'noticias-ajax.html';
                }
            }, function() {
                $('.btn-load-more').fadeIn();
            });

            $(window).unbind('.infscr');

            $('.btn-load-more').on('click', function() {
                $('.list-news').infinitescroll('retrieve');
                return false;
            });

        }
    };

    noticias.infScroll();
    $('.watermark').watermark('Busca por palavra-chave','#999');

}(jQuery, window, document));
