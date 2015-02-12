var CardCreatorForArticle = function ($template) {
    this.$template = $template;
    this.init();
};

CardCreatorForArticle.prototype.init = function() {
    this.cacheElements();
    this.bindEvents();
};

CardCreatorForArticle.prototype.cacheElements = function() {
    this.$form = this.$template;
    this.$fullOverlay = this.$form.find('.card__overlay.m-full');
};

CardCreatorForArticle.prototype.bindEvents = function() {
    this.$form.on('submit', {self: this}, this.createCardEvent);
};

CardCreatorForArticle.prototype.createCardEvent = function(event) {
    event.preventDefault();
    var self = event.data.self,
        $form = $(this);
    self.$fullOverlay.addClass('m-active');
    var formData = new FormData($form[0]);
    $.ajax({
        url: $form.attr('action'),
        method: $form.attr('method'),
        data: formData,
        cache: false,
        contentType: false,
        processData: false
    }).done(function(data) {
        self.$fullOverlay.removeClass('m-active');
        window.location = window.location;
    }).error(function() {
        $form.show();
        self.$fullOverlay.addClass('m-active m-error').text('Ошибка при добавлении');
        setTimeout(function() {
            self.$fullOverlay.removeClass('m-active m-error').text('');
        }, 1500);
    });
};
