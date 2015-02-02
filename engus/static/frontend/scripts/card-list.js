$(document).ready(function() {
    var $cardListWrapper = $('.card-list'),
        $overlay = $cardListWrapper.find('.card-list__overlay'),
        $content = $cardListWrapper.find('.card-list__content');

    // Load pages ajax
    $cardListWrapper.on('click', '.pages__link', function(event) {
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
    });


    var LEARN_MODE = 'learn',
        REPEAT_MODE = 'repeat',
        MODES = [LEARN_MODE, REPEAT_MODE],
        cardsToReapeat = 0,
        $switcher = $('.card-list__modeswitch'),
        $switchItems = $('.card-list__modeswitch-item');

    $switchItems.on('click', function() {
        var mode = $(this).data('mode');
        switchMode(mode);
    });

    function switchMode(mode) {
        $switcher.removeClass(MODES.join(' '));
        $switcher.addClass(mode);
        $switchItems.removeClass('active');
        $switchItems.filter('.' + mode).addClass('active');
        repeatCards(mode);

    }

    function repeatCards(mode) {
        var $cardList = $cardListWrapper.find('.card-list__list'),
            $cards = $cardList.find('.card'),
            $cardsContents = $cards.find('.card__content'),
            $overlays = $cards.find('.card__overlay');
        switch(mode) {
            case 'learn':
                $cards.find('.card__back, .card__front, .card__image').show();
                $cardsContents.addClass('editable');
                $overlays.hide();
                break;
            case 'repeat':
                $cards.find('.card__back, .card__image, .card__infoline, .card__controls').hide();
                $cardsContents.removeClass('editable');
                cardsToReapeat = $cards.length;
                $cards.randomize();
                $cards.each(function() {
                    var $card = $(this),
                        $overlay = $card.find('.card__overlay--right');
                    $overlay.show();
                    $overlay.one('click', function() {
                        cardsToReapeat -= 1;
                        $card.find('.card__back, .card__front, .card__image').show();
                        $overlay.hide();
                        if (cardsToReapeat == 0) {
                            switchMode(LEARN_MODE);
                        }
                    });
                });
                break;
        }
    }
});