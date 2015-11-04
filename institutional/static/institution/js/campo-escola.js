(function($, window, document, undefined) {
	'use strict';

	var campoEscola = {

		slider: function() {
			
			var gallery = $('#thumbs').galleriffic({
				delay: 3000,
				numThumbs: 6,
				preloadAhead: 6,
				enableTopPager: false,
				enableBottomPager: false,
				imageContainerSel: '#slideshow',
				captionContainerSel: '#caption',
				controlsContainerSel: '#controls',
				loadingContainerSel: '#loading',
				renderSSControls: false,
				renderNavControls: true,
				prevLinkText: '&lsaquo; Previous Photo',
				nextLinkText: 'Next Photo &rsaquo;',
				nextPageLinkText: 'Next &rsaquo;',
				prevPageLinkText: '&lsaquo; Prev',
				enableHistory: false,
				autoStart: false,
				syncTransitions: false,
				defaultTransitionDuration: 1000
			});

			/**************** Event handlers for custom next / prev page links **********************/

			gallery.find('a.prev').click(function(e) {
				gallery.previousPage();
				e.preventDefault();
			});

			gallery.find('a.next').click(function(e) {
				gallery.nextPage();
				e.preventDefault();
			});

			$('.nav-controls a').addClass('btn ir');
			$('.caption').addClass('clearfix');
		},

		googleMaps: function() {
			var map;
			var mapOptions = {
				zoom: 16,
				scrollwheel: false,
				panControl: false,
				zoomControl: true,
				zoomControlOptions: {
					style: google.maps.ZoomControlStyle.SMALL
				},
				streetViewControl: false,
				scaleControl: true,
				center: new google.maps.LatLng(-29.679478, -51.11608),
				mapTypeId: google.maps.MapTypeId.ROADMAP
			};

			map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);

			new google.maps.Marker({
				position: map.getCenter(),
				map: map,
				title: 'Escoteiros',
				icon: 'assets/img/marker.png',
				cursor: 'default',
				draggable: false
			});

		},

		init: function() {
			campoEscola.slider();
			campoEscola.googleMaps();
		}
	};

	campoEscola.init();

}(jQuery, window, document));