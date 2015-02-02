$(document).ready(function() {

    // Open controls and infoline when click on card
    $(document).on('click', '.card:not(.card--form) .card__content.editable', function () {
        var $card = $(this).parents('.card'),
            $otherCards = $('.card:not(.card--form)').not($card);
        $card.find('.card__infoline, .card__controls--edit').toggle();
        $otherCards.not($card)
            .find('.card__infoline, .card__controls').hide();
    });

    // Close controls in all cards
    $(document).on('click', function(event) {
        var $target = $(event.target),
            $cards = $('.card:not(.card--form)');
        if (!$cards.is($target) && !$cards.has($target).length > 0) {
            $cards.find('.card__infoline, .card__controls').hide();
        }
    });


    // Delete card
    $(document).on('submit', '.card__form--delete', deleteCard);

    function deleteCard(event) {
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
});