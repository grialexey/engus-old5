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


    var $article = $('.article');
    if ($article.length > 0) {
        $article.on('submit', '.article__copy-cards-form', function(event) {
            event.preventDefault();
            var $form = $(this),
                $btn = $form.find('.article__copy-btn');
            $btn.removeClass('m-active');
            $btn.attr('disabled', 'disabled');
            $.ajax({
                url: $form.attr('action'),
                method: $form.attr('method'),
                data: $form.serialize()
            }).done(function(data) {
                $('.header__menu-repeat-count').text(data['cards_to_repeat_count']);
                $btn.html('Все&nbsp;карточки добавлены в&nbsp;Мои&nbsp;карточки');
            }).error(function() {
                var text = $btn.text();
                $btn.addClass('m-active');
                $btn.text('Ошибка при добавлении');
                window.setTimeout(function() {
                    $btn.removeAttr('disabled');
                    $btn.text(text);
                }, 1500);
            });
        })
    }
});