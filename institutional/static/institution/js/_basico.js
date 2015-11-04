(function($, window, document, undefined) {
    'use strict';

    function noWatermark(value, element) {
        return (value !== element.title);
    }
    var x = 0;

    var basico = {
        loader: function() {
            $('body').queryLoader2({
                barColor: '#6e6d73',
                backgroundColor: '#fff1b0',
                percentage: true,
                barHeight: 10,
                minimumTime: 100,
                onComplete: function() {
                    setTimeout(function() {
                        $('#loader-bg').fadeOut(400, function() {
                            $(this).remove();
                        });
                    }, 100);
                }
            });

            var percentageElem = $('#qLpercentage'),
                loading = $('.loading'),
                loadingPercent = $('#loader-percent');

            setInterval(function() {
                loading.height((parseInt(percentageElem.text().replace('%', ''), 10)) * 3.21);
                loadingPercent.text(parseInt(percentageElem.text().replace('%', ''), 10) + '%');
            }, 10);
        },

        menu: function() {
            $('.btn-menu').on('click', function() {
                if ($(this).hasClass('open')) {
                    $('.open-submenu').removeClass('open');
                    $('.menu').removeClass('open mHeight');
                    $(this).removeClass('open');
                } else {
                    $(this).addClass('open');
                    $('.menu').addClass('open');
                }
            });
        },

        submenu: function() {
            $('.open-submenu').on('click', function() {
                $(this).toggleClass('open');
                $('.menu').toggleClass('mHeight');
            });
        },

        exeMenu: function(){
            if(x === 0){
                if($(window).width() < 1020){
                    basico.menu();
                    basico.submenu();
                    x++;
                }
            }
        },

        tweetButton: function() {
            ! function(d, s, id) {
                var js, fjs = d.getElementsByTagName(s)[0];
                if (!d.getElementById(id)) {
                    js = d.createElement(s);
                    js.id = id;
                    js.src = 'https://platform.twitter.com/widgets.js';
                    fjs.parentNode.insertBefore(js, fjs);
                }
            }(document, 'script', 'twitter-wjs');
        },

        likeButton: function() {
            (function(d, s, id) {
                var js, fjs = d.getElementsByTagName(s)[0];
                if (d.getElementById(id)) return;
                js = d.createElement(s);
                js.id = id;
                js.src = '//connect.facebook.net/pt_BR/all.js#xfbml=1';
                fjs.parentNode.insertBefore(js, fjs);
            }(document, 'script', 'facebook-jssdk'));
        },

        textFooter: function() {
            if ($(window).width() < 768) {
                $('.union').html('União dos Escoteiros do Brasil<br> Rio Grande do Sul');
                $('.location').html('<span></span>Rua Castro Alves, 398<br> Bairro Rio Branco - Porto Alegre');
            } else {
                $('.union').html('União dos Escoteiros do Brasil - Rio Grande do Sul');
                $('.location').html('<span></span>Rua Castro Alves, 398, Bairro Rio Branco - Porto Alegre');
            }

        },

        dialogEmail: function() {
            $('body').on('click', function(e) {
                var elem = $(e.target),
                    dialog = $('.dialog-email'),
                    btn = $('.btn-email');

                if (elem.hasClass('btn-email')) {
                    if (elem.hasClass('show-email')) {
                        btn.removeClass('show-email');
                        dialog.fadeOut(350);
                    } else {
                        btn.addClass('show-email');
                        dialog.fadeIn(350);
                    }
                } else if (elem.parents('.dialog-email').length > 0 || elem.hasClass('dialog-email')) {
                    btn.addClass('show-email');
                    dialog.fadeIn(350);
                } else {
                    btn.removeClass('show-email');
                    dialog.fadeOut(350);
                }
            });

            $('.dialog-sucesso a').on('click', function() {
                $('.dialog-sucesso').fadeOut(350);
            });

            $.validator.addMethod('nowatermark',
                function(value, element) {
                    return noWatermark(value, element);
                });

            $('.form-email input').each(function() {
                $(this).watermark($(this).attr('title'), '#999');
            });

            $('.form-email').validate({
                submitHandler: function() {
                    $('.dialog-sucesso').fadeIn(350);
                },
                rules: {
                    txtEmailNome: {
                        required: true,
                        nowatermark: true
                    },
                    txtEmailEmail: {
                        required: true,
                        nowatermark: true,
                        email: true
                    },
                    txtEmailNomeAmigo: {
                        required: true,
                        nowatermark: true
                    },
                    txtEmailEmailAmigo: {
                        required: true,
                        nowatermark: true,
                        email: true
                    }
                }
            });
        }
    };

    basico.loader();
    basico.tweetButton();
    basico.likeButton();
    basico.textFooter();
    basico.dialogEmail();
    basico.exeMenu();

    $(window).resize(function() {
        basico.textFooter();
        basico.exeMenu();
    });

}(jQuery, window, document));
