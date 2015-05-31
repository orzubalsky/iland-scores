var $signs = $('.sign');

$signs.on('mouseenter', function() {
    var $container = $(this).parents('.score');
    $container.css('color', '#999');
});

$signs.on('mouseleave', function() {
    var $container = $(this).parents('.score');
    $container.css('color', '#fff');
});