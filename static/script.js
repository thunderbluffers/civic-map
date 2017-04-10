var navMenuActive = function(selector) {
    var $items = $(selector).find('li a');
    var path = location.pathname;
    $items.each(function() {
        var $item = $(this);
        if ($item.attr('href') === path) {
            $item.parent('li').addClass('active');
        }
    });
}

jQuery('document').ready(function($) {
    navMenuActive('.nav.navbar-nav');
});
