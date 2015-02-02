$(document).ready(function() {

    // Open controls when click on card
    $(document).on('click', '.card:not(.card--form) .card__content', function () {
        var $card = $(this).parents('.card'),
            $allCards = $('.card:not(.card--form)');
        $card.find('.card__controls').toggle();
        $allCards.not($card).find('.card__controls').hide();
    });

    // Delete card
    $(document).on('click', '.card__button--remove', function () {
        var $card = $(this).parents('.card'),
            $cardId = $card.data('id');
            deleteUrl = $(this).data('url');
        $.ajax({
            url: url,
            method: 'post',
            data: {'id': $card.data}
        }).done(function() {
            $showFormButton.removeClass('loading');
            $form.remove();
        }).error(function() {
            $form.show();
            $showFormButton.removeClass('loading');
            $showFormButton.addClass('active');
            $contentOverlay.show();
            $overlay.css('color', '#ff0000').text('Ошибка при добавлении').appendTo($form);
            setTimeout(function() {
                $overlay.remove();
            }, 1500);
        });
    });

    $(document).on('submit', '.card__form--delete', deleteCard);

    function deleteCard() {
        event.preventDefault();
        var $form = $(this),
            $card = $(this).parents('.card'),
            $overlay = $card.find('.card__overlay');
        $card.hide();
        $.ajax({
            url: $form.attr('action'),
            method: 'post',
            data: $form.serialize()
        }).done(function() {
            $card.remove();
        }).error(function() {
            $card.show();
            $overlay.css('color', '#ff0000').text('Ошибка при удалении').appendTo($form);
            $overlay.show();
            setTimeout(function() {
                $overlay.hide();
            }, 1500);
        });
    }

    // Close controls in all cards
    $(document).on('click', function(event) {
        var $target = $(event.target),
            $cards = $('.card:not(.card--form)');
        if (!$cards.is($target) && !$cards.has($target).length > 0) {
            $cards.find('.card__controls').hide();
        }
    });
});