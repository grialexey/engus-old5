$(document).ready(function() {
    var $cardList = $('.card-list'),
        $overlay = $cardList.find('.card-list__overlay'),
        $content = $cardList.find('.card-list__content');
    $cardList.on('click', '.pages__link', function(event) {
        event.preventDefault();
        var $link = $(this);
        $overlay.show();
        $.ajax({
            url: $link.attr('href'),
            method: 'get'
        }).done(function(data) {
            $overlay.hide();
            $content.html(data);
        });
    })
});