$(document).ready(function() {
    var cardList = new CardList($('.card-list'));
    $('.card-list .card.m-creator').each(function() {
        var cardCreator = new CardCreator($(this));
        cardCreator.$el.on('created', function(event, data) {
            window.location.hash = '#card' + data['id'];
            window.location.reload();
        });
    });
    new CardQuickCreator();
});