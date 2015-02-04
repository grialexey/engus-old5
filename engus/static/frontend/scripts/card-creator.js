var CardCreator = function ($template, $button, $pageOverlay) {
    this.loading = false;
    this.$template = $template;
    this.$button = $button;
    this.$pageOverlay = $pageOverlay;
    this.$form = this.createForm();
    this.bindEvents();
};

CardCreator.prototype.bindEvents = function() {
    this.$button.on('click', this.clickButtonEvent.bind(this));
    $(document).on('click', this.clickOutsideEvent.bind(this));
};

CardCreator.prototype.createForm = function() {
    var form = this.$template.clone();
    form.$overlay = form.find('.card__overlay');
    form.on('submit', this.createEvent.bind(this));
    return form;
};

CardCreator.prototype.clickOutsideEvent = function(event) {
    var $target = $(event.target);
    if (!this.$form.is($target) && !this.$form.has($target).length && !$target.is(this.$button)) {
        this.$form.remove();
        this.$button.removeClass('active');
        this.$pageOverlay.fadeOut(150);
    }
};

CardCreator.prototype.clickButtonEvent = function(event) {
    if (!this.loading) {
        if (this.$button.is('.active')) {
            this.close();
        } else {
            this.open();
        }
    }
};

CardCreator.prototype.open = function() {
    this.$button.addClass('active');
    this.$pageOverlay.fadeIn(150);
    this.$form = this.createForm().appendTo('.header__wrapper');
    this.$form.fadeIn(150).find('input[type=text]').first().focus();
};

CardCreator.prototype.close = function() {
    this.$form.remove();
    this.$button.removeClass('active');
    this.$pageOverlay.fadeOut(150);
};

CardCreator.prototype.createEvent = function(event) {
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
    }).done(function() {
        self.loading = false;
        self.close();
    }).error(function() {
        self.loading = false;
        self.$form.show();
        self.$button.removeClass('loading');
        self.$button.addClass('active');
        self.$pageOverlay.fadeIn(150);
        self.$form.$overlay.css('color', '#ff0000').text('Ошибка при добавлении');
        self.$form.$overlay.show();
        setTimeout(function() {
            self.$form.$overlay.hide();
        }, 1500);
    });
};
