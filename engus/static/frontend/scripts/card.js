$(document).ready(function() {

    // Open controls and infoline when click on card
    $(document).on('click', '.card:not(.card--form) .card__content.editable', function () {
        var $card = $(this).parents('.card'),
            $otherCards = $('.card:not(.card__form)').not($card);
        closeUpdateForm($otherCards);
        $card.children('.card__infoline, .card__controls--edit').toggle();
        $otherCards.children('.card__infoline, .card__controls').hide();
    });

    // Close controls in all cards
    $(document).on('click', function(event) {
        var $target = $(event.target),
            $cards = $('.card:not(.card__form)'),
            $cardContent = $cards.children('.card__content');
        if (!$cards.is($target) && !$cards.has($target).length > 0) {
            closeUpdateForm($cards);
            $cards.children('.card__infoline, .card__controls, .card__form').hide();
            $cardContent.show();
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



    /*
    *  Create new card
    */

    var $newCardFormTmpl = $('.card__form--create'),
        $showCreateCardFormButton = $('.header__menu-link--add'),
        $content = $('.content'),
        $contentOverlay = $('.content__overlay');

    $showCreateCardFormButton.not('.loading').on('click', function() {
        if ($showCreateCardFormButton.is('.active')) {
            $showCreateCardFormButton.removeClass('active');
            $contentOverlay.fadeOut(150);
            $('.card__form--create').remove();
        } else {
            $showCreateCardFormButton.addClass('active');
            $contentOverlay.fadeIn(150);
            var $newCardForm = $newCardFormTmpl.clone().appendTo('.header__wrapper');
            $newCardForm.fadeIn(150).find('input[type=text]').first().focus();
            $newCardForm.on('submit', cardCreate);
        }

    });

    $(document).on('click', function(event) {
        var $target = $(event.target),
            $cardCreateForms = $('.card__form--create');
        if (!$cardCreateForms.is($target) && !$cardCreateForms.has($target).length && !$target.is($showCreateCardFormButton)) {
            $cardCreateForms.remove();
            $showCreateCardFormButton.removeClass('active');
            $contentOverlay.fadeOut(150);
        }
    });


    function cardCreate(event) {
        event.preventDefault();
        var $form = $(this),
            $overlay = $form.find('.card__overlay');
        $form.hide();
        $showCreateCardFormButton.removeClass('active');
        $contentOverlay.fadeOut(150);
        $showCreateCardFormButton.addClass('loading');
        $.ajax({
            url: $form.attr('action'),
            method: 'post',
            data: $form.serialize()
        }).done(function() {
            $showCreateCardFormButton.removeClass('loading');
            $form.remove();
        }).error(function() {
            $form.show();
            $showCreateCardFormButton.removeClass('loading');
            $showCreateCardFormButton.addClass('active');
            $contentOverlay.fadeIn(150);
            $overlay.css('color', '#ff0000').text('Ошибка при добавлении').appendTo($form);
            $overlay.show();
            setTimeout(function() {
                $overlay.hide();
            }, 1500);
        });
    }





    /*
    *  Update card
    */

    $(document).on('click', '.card__button--edit', function() {
        var $card = $(this).parents('.card');
        openUpdateForm($card);
    });

    $(document).on('submit', '.card__form--update', cardUpdate);


    function openUpdateForm($cards) {
        var $cardsContent = $cards.children('.card__content, .card__controls, .card__infoline'),
            $updateForms = $cards.find('.card__form--update');
        $cardsContent.hide();
        $updateForms.show();
    }

    function closeUpdateForm($cards) {
        var $cardsContent = $cards.children('.card__content, .card__controls, .card__infoline'),
            $updateForms = $cards.find('.card__form--update');
        $cardsContent.show();
        $updateForms.hide();
    }


    function cardUpdate(event) {
        event.preventDefault();
        var $form = $(this),
            $card = $form.parents('.card'),
            $overlay = $card.find('.card__overlay');
        $overlay.show();
        $.ajax({
            url: $form.attr('action'),
            method: 'post',
            data: $form.serialize()
        }).done(function(data) {
            $overlay.hide();
            $card.html(data);
        }).error(function() {
            $form.show();
            $overlay.css('opacity', '1').css('color', '#ff0000').text('Ошибка при сохранении').appendTo($form);
            setTimeout(function() {
                $overlay.hide();
                $overlay.css('opacity', '0.5');
            }, 1500);
        });
    }
});