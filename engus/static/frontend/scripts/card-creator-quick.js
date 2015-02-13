var CardCreatorQuick = function ($template, $button, $pageOverlay) {
    this.loading = false;
    this.$template = $template;
    this.$button = $button;
    this.$pageOverlay = $pageOverlay;
    this.$form = this.createForm();
    this.bindEvents();
};

CardCreatorQuick.prototype.bindEvents = function() {
    this.$button.on('click', this.clickButtonEvent.bind(this));
    $(document).on('click', this.clickOutsideEvent.bind(this));
};

CardCreatorQuick.prototype.createForm = function() {
    var $form = this.$template.clone();
    $form.$fullOverlay = $form.find('.card__overlay');
    $form.appendTo('.header__wrapper');
    $form.on('submit', this.createEvent.bind(this));
    return $form;
};

CardCreatorQuick.prototype.clickOutsideEvent = function(event) {
    var $target = $(event.target);
    if (!this.$form.is($target) && !this.$form.has($target).length && !$target.is(this.$button)) {
        this.$form.remove();
        this.$button.removeClass('active');
        this.$pageOverlay.fadeOut(150);
    }
};

CardCreatorQuick.prototype.clickButtonEvent = function(event) {
    if (!this.loading) {
        if (this.$button.is('.active')) {
            this.close();
        } else {
            this.open();
        }
    }
};

CardCreatorQuick.prototype.open = function() {
    this.$button.addClass('active');
    this.$pageOverlay.fadeIn(150);
    this.$form = this.createForm();
    this.$form.fadeIn(150).find('input[type=text]').first().focus();
};

CardCreatorQuick.prototype.close = function() {
    this.$form.remove();
    this.$button.removeClass('active');
    this.$pageOverlay.fadeOut(150);
};

CardCreatorQuick.prototype.createEvent = function(event) {
    event.preventDefault();
    this.loading = true;
    this.$form.hide();
    this.$button.removeClass('active').addClass('loading');
    this.$pageOverlay.fadeOut(150);
    var self = this;
    $.ajax({
        url: self.$form.attr('action'),
        method: 'post',
        data: self.$form.serialize()
    }).done(function(data) {
        self.loading = false;
        self.$button.removeClass('loading');
        self.close();

        $('.header__menu-repeat-count').text(data['cards_to_repeat_count']);
    }).error(function() {
        self.loading = false;
        self.$button.removeClass('loading');
        self.$button.addClass('active');
        self.$form.show();
        self.$pageOverlay.fadeIn(150);
        self.$form.$fullOverlay.css('opacity', '1').css('color', '#ff0000').text('Ошибка при добавлении').show();
        self.$form.$fullOverlay.show();
        setTimeout(function() {
            self.$form.$fullOverlay.css('opacity', '0.5').css('color', '#000').text('').hide();
        }, 1500);
    });
};
