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

    setInterval(function() {
        $.get('/cards/api/my-cards-count/').done(function(data) {
            $('.header__menu-repeat-count').text(data['cards_to_repeat_count']);
        });
    }, 180000);
});