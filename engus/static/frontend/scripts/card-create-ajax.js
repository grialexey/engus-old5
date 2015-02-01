$(document).ready(function() {
    var $newCardFormTmpl = $('.card--form'),
        $showFormButton = $('.header__item--add'),
        $overlay = $('<div class="card__overlay"></div>');

    $showFormButton.on('click', function() {
        if ($showFormButton.is('.active')) {
            $showFormButton.removeClass('active');
            $('.card--form').remove();
        } else {
            $showFormButton.addClass('active');
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
        }
    });


    function newCardSubmit(event) {
        event.preventDefault();
        var $form = $(this);
        $form.hide();
        $showFormButton.removeClass('active');
        $.ajax({
            url: $form.attr('action'),
            method: 'post',
            data: $form.serialize()
        }).done(function() {
            $form.remove();
        }).error(function() {
            $form.show();
            $showFormButton.addClass('active');
            $overlay.css('color', '#ff0000').text('Ошибка').appendTo($form);
            setTimeout(function() {
                $overlay.remove();
            }, 1000);
        });
    }
});