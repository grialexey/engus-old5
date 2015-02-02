$(document).ready(function() {
    var $newCardFormTmpl = $('.card--form'),
        $showFormButton = $('.header__menu-link--add'),
        $content = $('.content'),
        $contentOverlay = $('.content__overlay');

    $showFormButton.not('.loading').on('click', function() {
        if ($showFormButton.is('.active')) {
            $showFormButton.removeClass('active');
            $contentOverlay.fadeOut(150);
            $('.card--form').remove();
        } else {
            $showFormButton.addClass('active');
            $contentOverlay.fadeIn(150);
            var $newCardForm = $newCardFormTmpl.clone().appendTo('.header__wrapper');
            $newCardForm.fadeIn(150).find('input[type=text]').first().focus();
            $newCardForm.on('submit', newCardSubmit);
        }

    });

    $(document).on('click', function(event) {
        var $target = $(event.target),
            $cardForms = $('.card--form');
        if (!$cardForms.is($target) && !$cardForms.has($target).length && !$target.is($showFormButton)) {
            $('.card--form').remove();
            $showFormButton.removeClass('active');
            $contentOverlay.fadeOut(150);
        }
    });


    function newCardSubmit(event) {
        event.preventDefault();
        var $form = $(this),
            $overlay = $form.find('.card__overlay');
        $form.hide();
        $showFormButton.removeClass('active');
        $contentOverlay.fadeOut(150);
        $showFormButton.addClass('loading');
        $.ajax({
            url: $form.attr('action'),
            method: 'post',
            data: $form.serialize()
        }).done(function() {
            $showFormButton.removeClass('loading');
            $form.remove();
        }).error(function() {
            $form.show();
            $showFormButton.removeClass('loading');
            $showFormButton.addClass('active');
            $contentOverlay.fadeIn(150);
            $overlay.css('color', '#ff0000').text('Ошибка при добавлении').appendTo($form);
            $overlay.show();
            setTimeout(function() {
                $overlay.hide();
            }, 1500);
        });
    }
});