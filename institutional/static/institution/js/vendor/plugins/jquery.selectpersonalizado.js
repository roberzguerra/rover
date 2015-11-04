(function($){
    $.fn.extend({
        selectPersonalizado:function(){
            var $selector=$(this);

			$selector.each(function(){
                var $combo=$(this),initialValue=$combo.attr('title')?$combo.attr('title'):$combo.find('option:selected').text();
                $combo.css('position','relative').before('<span>'+initialValue+'</span>')
            });

			$selector.bind('change keypress keydown keyup',function(){
                $(this).prev().html($(this).find('option:selected').text())
            });

            $selector.focus(function(){
                $(this).parent().addClass('selectOpen')
            }).blur(function(){
                $(this).parent().removeClass('selectOpen')
            })
        }
    })
})(jQuery);
