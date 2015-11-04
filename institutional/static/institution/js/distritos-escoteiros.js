(function($, window, document, undefined) {
	'use strict';

	function noWatermark(value, element) {
		return (value !== element.title);
	}

	var distritosEscoteiros = {

		formBusca: function(){
			$.validator.addMethod('nowatermark',
			function(value, element) {
				return noWatermark(value, element);
			});

			$('.txtBuscar').watermark('Busca por palavra-chave (Grupo, cidade, etc)','#999');

			$('#formBuscar').validate({
				submitHandler: function() {
					// Busca itens.
				},
				rules: {
					txtBuscar: {
						required: true,
						nowatermark: true
					}
				},
				messages: {
					txtBuscar: {
						required: '*',
						nowatermark: '*'
					}
				}
			});
		},

        infScroll: function() {
            $('.lista-distritos').infinitescroll({
                navSelector: '.btn-load-district',
                nextSelector: '.btn-load-district',
                itemSelector: '.lista-distritos li',
                dataType: 'html',
                animate: false,
                loading: {
                    img: 'assets/img/ajax-loader.gif',
                    finishedMsg: '<span></span>'
                },
                path: function() {
                    return 'distritos-escoteiros-ajax.html';
                } 
            }, function() {
                $('.btn-load-district').fadeIn();
            });

            $(window).unbind('.infscr');

            $('.btn-load-district').on('click', function() {
                $('.lista-distritos').infinitescroll('retrieve');
                return false;
            });
        },


		init: function() {
            distritosEscoteiros.formBusca();
			distritosEscoteiros.infScroll();
		}

	};

	distritosEscoteiros.init();

}(jQuery, window, document));
