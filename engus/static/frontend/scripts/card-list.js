$(document).ready(function() {
    var $cardList = $('.card-list');
    $cardList.on('click', '.pages__link', function(event) {
        event.preventDefault();
        var $link = $(this),
            $overlay = $cardList.find('.card-list__overlay');
        $overlay.show();
        $.ajax({
            url: $link.attr('href'),
            method: 'get'
        }).done(function(data) {
            $overlay.hide();
            $cardList.html(data);
        });
    })
});