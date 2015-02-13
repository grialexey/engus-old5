var CardCreator = function ($element) {
    this.init($element);
};

CardCreator.prototype.init = function($element) {
    this.cacheElements($element);
    this.bindEvents();
    this.deffered = $.Deferred();
};

CardCreator.prototype.getDeferred = function() {
    return this.deffered;
};

CardCreator.prototype.cacheElements = function($element) {
    this.$el = $element;
    this.$form = $element.find('.card__form--create');
    this.$fullOverlay = this.$el.find('.card__overlay.m-full');
};

CardCreator.prototype.bindEvents = function() {
    this.$form.on('submit', {self: this}, this.createCardEvent);
};

CardCreator.prototype.unbindEvents = function() {
    this.$form.on('submit', this.createCardEvent);
};

CardCreator.prototype.createCardEvent = function(event) {
    event.preventDefault();
    var self = event.data.self,
        $form = $(this);
    self.$fullOverlay.addClass('m-active');
    $.ajax({
        url: $form.attr('action'),
        method: $form.attr('method'),
        data: new FormData($form[0]),
        cache: false,
        contentType: false,
        processData: false
    }).done(function(data) {
        self.unbindEvents();
        self.$el.trigger('created', [data]);
        self.$el.remove();
    }).error(function() {
        $form.show();
        self.$fullOverlay.addClass('m-active m-error').text('Ошибка при добавлении');
        setTimeout(function() {
            self.$fullOverlay.removeClass('m-active m-error').text('');
        }, 1500);
    });
};
