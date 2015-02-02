$(document).ready(function() {
    var $cardList = $('.card-list'),
        $overlay = $cardList.find('.card-list__overlay'),
        $content = $cardList.find('.card-list__content');
    $cardList.on('click', '.pages__link', function(event) {
        event.preventDefault();
        var $link = $(this),
            url = $link.attr('href');
        $overlay.show();
        $.ajax({
            url: url,
            method: 'get'
        }).done(function(data) {
            $overlay.hide();
            $content.html(data);
            if(url != window.location){
                window.history.pushState({ path:url }, '', url);
            }
        });
    })
});