(function($, window, document, undefined) {
	'use strict';

	function noWatermark(value, element) {
		return (value !== element.title);
	}

	var escotismo = {
		formularioPesquisa: function() {
			
			$('.filtro select').selectPersonalizado();

			$('.txtPesquisar').watermark('Busca por palavra-chave (Grupo, cidade, etc)','#999999');

			$.validator.addMethod('nowatermark',
				function(value, element) {
					return noWatermark(value, element);
				});

			$('#formProcurar').validate({
				submitHandler: function() {
					// Busca itens.
				},
				rules: {
					txtPesquisar: {
						required: true,
						nowatermark: true
					},
					selCidade: {
						required: true,
						nowatermark: true
					}
				},
				messages: {
					txtPesquisar: {
						required: '*',
						nowatermark: '*'
					},
					selCidade: {
						required: '*',
						nowatermark: '*'
					}
				}
			});


			function verificaFiltro() {
				if ($('.filtro span').text() === 'Cidade') {
					$('.filtro').addClass('error');
					e.preventDefault();
				} else {
					$('.filtro').removeClass('error');
				}
			}

			$('#formProcurar').on('submit', function(e) {
				verificaFiltro(e);
			});

			$('.filtro select').on('change', function() {
				verificaFiltro();
			});

		},

		init: function() {
			escotismo.formularioPesquisa();
		}
	};

	escotismo.init();

}(jQuery, window, document));