$(document).ready(function() {
    var $newCardFormTmpl = $('.card--form'),
        $showFormButton = $('.header__menu-link--add'),
        $content = $('.content'),
        $contentOverlay = $('.content__overlay');

    $showFormButton.not('.loading').on('click', function() {
        if ($showFormButton.is('.active')) {
            $showFormButton.removeClass('active');
            $contentOverlay.hide();
            $('.card--form').remove();
        } else {
            $showFormButton.addClass('active');
            $contentOverlay.show();
            var $newCardForm = $newCardFormTmpl.clone().appendTo('.header__wrapper');
            $newCardForm.show().find('input[type=text]').first().focus();
            $newCardForm.on('submit', newCardSubmit);
        }

    });

    $(document).on('click', function(event) {
        var $target = $(event.target),
            $cardForms = $('.card--form');
        if (!$cardForms.is($target) && !$cardForms.has($target).length && !$target.is($showFormButton)) {
            $('.card--form').remove();
            $showFormButton.removeClass('active');
            $contentOverlay.hide();
        }
    });


    function newCardSubmit(event) {
        event.preventDefault();
        var $form = $(this),
            $overlay = $form.find('.card__overlay');
        $form.hide();
        $showFormButton.removeClass('active');
        $contentOverlay.hide();
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
            $contentOverlay.show();
            $overlay.css('color', '#ff0000').text('Ошибка при добавлении').appendTo($form);
            $overlay.show();
            setTimeout(function() {
                $overlay.hide();
            }, 1500);
        });
    }
});