(function($, window, document, undefined) {
    'use strict';

    var index = {

        slider: function() {

            $('.slider').cycle({
                fx: 'scrollHorz',
                speed: 600,
                slideResize: false,
                containerResize: false,
                fit: 1,
                timeout: 0,
                next: '.next',
                prev: '.prev',
                pager: '.pagination'
            });

        },

        news: function() {

            $('.list-news').cycle({
                fx: 'scrollHorz',
                speed: 600,
                slideResize: false,
                containerResize: false,
                fit: 1,
                timeout: 0,
                pager: '.pag-news'
            });

        },

        store: function() {

            $('.products').cycle({
                fx: 'scrollHorz',
                speed: 600,
                slideResize: false,
                containerResize: false,
                fit: 1,
                timeout: 0,
                next: '.next-store',
                prev: '.prev-store',
                pager: '.carrousel-products'
            });

        },

        sliderReset: function() {
            $('.slider').cycle('destroy');
            index.slider();
        },

        resetProducts: function() {
            $('.products').cycle('destroy');
        }
    };

    index.slider();
    //index.news();

    if ($(window).width() > 750) {
        index.resetProducts();
    } else {
        index.store();
    }

    $(window).resize(function() {
        if ($(window).width() > 948) {
            index.sliderReset();
        }

        if ($(window).width() > 750) {
            index.resetProducts();
        } else {
            index.resetProducts();
            index.store();
        }
    });

    $('.watermark').watermark('Busca por palavra-chave (Grupo, cidade, etc)', '#999');

}(jQuery, window, document));