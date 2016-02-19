(function($, window, document, undefined) {
    'use strict';

    var oQueFazemos = {

        spot: function() {

            // Initialize Advanced Galleriffic Gallery
            var gallery = $('#thumbs').galleriffic({
                delay:                     3000,
                numThumbs:                 6,
                preloadAhead:              6,
                enableTopPager:            false,
                enableBottomPager:         false,
                imageContainerSel:         '#slideshow',
                captionContainerSel:       '#caption',
                controlsContainerSel:      '#controls',
                loadingContainerSel:       '#loading',
                renderSSControls:          false,
                renderNavControls:         true,
                prevLinkText:              '&lsaquo; Previous Photo',
                nextLinkText:              'Next Photo &rsaquo;',
                nextPageLinkText:          'Next &rsaquo;',
                prevPageLinkText:          '&lsaquo; Prev',
                enableHistory:             false,
                autoStart:                 false,
                syncTransitions:           false,
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

        }

    };


    oQueFazemos.spot();

}(jQuery, window, document));
