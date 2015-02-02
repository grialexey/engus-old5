$(document).ready(function() {
    var $cardListWrapper = $('.card-list'),
        $overlay = $cardListWrapper.find('.card-list__overlay'),
        $cardListAndPages = $cardListWrapper.find('.card-list__content');


    var LEARN_MODE = 'learn',
        REPEAT_MODE = 'repeat',
        MODES = [LEARN_MODE, REPEAT_MODE],
        cardsToReapeat = 0,
        $switcher = $('.card-list__modeswitch'),
        $switchItems = $('.card-list__modeswitch-item');

    // Switch mode (learning and repeating)
    $switchItems.on('click', function() {
        var mode = $(this).data('mode');
        switchMode(mode);
    });


    // Load pages ajax
    $cardListWrapper.on('click', '.pages__link', function(event) {
        event.preventDefault();
        var $link = $(this),
            url = $link.attr('href');
        $overlay.appendTo($cardListAndPages).show();
        $.ajax({
            url: url,
            method: 'get'
        }).done(function(data) {
            $cardListAndPages.html(data);
            if(url != window.location){
                window.history.pushState({ path:url }, '', url);
            }
            var mode = $switchItems.filter('.active').data('mode');
            switchMode(mode);
        });
    });


    function switchMode(mode) {
        $switcher.removeClass(MODES.join(' '));
        $switcher.addClass(mode);
        $switchItems.removeClass('active');
        $switchItems.filter('.' + mode).addClass('active');
        var $cards = $cardListWrapper.find('.card'),
            $overlays = $cards.find('.card__overlay');
        switch(mode) {
            case 'learn':
                learnCards($cards);
                break;
            case 'repeat':
                repeatCards($cards);
                break;
        }
    }

    function learnCards($cards) {
        $cards.find('.card__overlay').hide();
        $cards.children('.card__back, .card__front, .card__image').show();
        $cards.children('.card__content').addClass('editable');
    }

    function repeatCards($cards) {
        $cards.children('.card__back, .card__image, .card__infoline, .card__controls').hide();
        $cards.children('.card__content').removeClass('editable');
        $cards.randomize();
        cardsToReapeat = $cards.length;
        $cards.each(function() {
            var $card = $(this),
                $overlay = $card.find('.card__overlay').addClass('right');
            $overlay.show();
            $overlay.one('click', function() {
                cardsToReapeat -= 1;
                $card.find('.card__back, .card__front, .card__image').show();
                $overlay.hide().removeClass('right');
                if (cardsToReapeat == 0) {
                    //switchMode(LEARN_MODE);
                }
            });
        });
    }

});