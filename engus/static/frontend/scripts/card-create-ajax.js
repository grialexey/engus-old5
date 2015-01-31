$(document).ready(function() {
    var $newCardForm = $('.card--form'),
        $showFormButton = $('.header__item--add'),
        $overlay = $('<div class="card__overlay"></div>');

    $showFormButton.on('click', function() {
        $newCardForm.toggle();
        if ($newCardForm.is(':visible')) {
            $showFormButton.addClass('active');
            $newCardForm.find('input[type=text]').first().focus();
        } else {
            $showFormButton.removeClass('active');
        }
    });

    $(document).on('click', function(event) {
        var $target = $(event.target);
        if (!$newCardForm.is($target) && !$newCardForm.has($target).length && !$target.is($showFormButton)) {
            $newCardForm.hide();
            $showFormButton.removeClass('active');
        }
    });

    $newCardForm.on('submit', function(event) {
        event.preventDefault();
        $newCardForm.css('opacity', '0.5');
        $.ajax({
            url: $newCardForm.attr('action'),
            method: 'post',
            data: $newCardForm.serialize()
        }).done(function () {
            $newCardForm.css('opacity', '1');
            $overlay.css('color', '#008000').text('Добавлено').appendTo($newCardForm);
            setTimeout(function() {
                $overlay.remove();
                $newCardForm.hide();
                $showFormButton.removeClass('active');
                $newCardForm.find('input[name=front]').val('');
                $newCardForm.find('input[name=back]').val('');
            }, 1000);
        }).error(function() {
            $newCardForm.css('opacity', '1');
            $overlay.css('color', '#ff0000').text('Ошибка').appendTo($newCardForm);
            setTimeout(function() {
                $overlay.remove();
            }, 1000);
        });
    });
});