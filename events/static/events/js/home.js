Events = {
    init: function () {
        this.pageScroll();
    },

    pageScroll: function () {
        $("body").attr({'id': "page-top", 'data-spy': "scroll", 'data-target': ".navbar-fixed-top"});
        /* Inactive
         $(window).scroll(function() {
         if ($(".navbar").offset().top > 50) {
         $(".navbar-fixed-top").addClass("top-nav-collapse");
         } else {
         $(".navbar-fixed-top").removeClass("top-nav-collapse");
         }
         });
         */

        //jQuery for page scrolling feature - requires jQuery Easing plugin
        $('a.navegacao-link').bind('click', function (event) {
            var $anchor = $(this)
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top
            }, 500, ''); // 'easeInOutExpo'
            event.preventDefault();
        });
    },
    setPageScroll: function (id) {
        //jQuery for page scrolling feature - requires jQuery Easing plugin

        var $anchor = $(this)
        $('html, body').stop().animate({
            scrollTop: $(id).offset().top
        }, 500, ''); // 'easeInOutExpo'
    },

    war: function () {
        var pressedCtrl = false;
        var sss = 0;
        $(document).keyup(function (e) {
            if (e.which == 17) pressedCtrl = false;
        });
        $(document).keydown(function (e) {
            if (e.which == 17) pressedCtrl = true;
            if (pressedCtrl) {
                if ((e.which == 39 || e.keyCode == 39)) sss += 39; else if ((e.which == 38 || e.keyCode == 38)) sss += 38; else if ((e.which == 65 || e.keyCode == 65)) sss += 65; else if ((e.which == 66 || e.keyCode == 66)) {
                    sss += 66;
                    if (sss == 208) window.location = "/star_wars/";
                }
            }
        });
    }
};

/* Para usar ajax */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

window.mapsAsyncInit = function () {
    var container = document.querySelector('[data-address]')
        , address = container.getAttribute('data-address')
        , options = {
            zoom: 16,
            scrollwheel: true,
            mapTypeControl: true,
            labels: true,
            zoomControlOptions: {
                position: google.maps.ControlPosition.TOP_RIGHT
            },
            mapTypeId: google.maps.MapTypeId.ROADMAP,
        };
    var map = new google.maps.Map(container, options),
        search = new google.maps.Geocoder();
    search.geocode({ address: address }, function (data) {
        var location = data[0].geometry.location;
        new google.maps.Marker({
            map: map, position: location
        });
        map.setCenter(location);
    })
};

// Load Scripts
// ===========

function loadScripts(urls) {
    var script = document.getElementsByTagName('script')[0]
    if (!Array.isArray(urls)) {
        urls = [urls]
    }
    urls.forEach(function (url) {
        var element = document.createElement('script')
        element.async = true
        element.src = 'http://' + url
        script.parentNode.insertBefore(element, script)
    })
}