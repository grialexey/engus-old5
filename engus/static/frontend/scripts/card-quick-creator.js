var CardQuickCreator = function () {
    this.init();
};

CardQuickCreator.prototype.init = function() {
    this.loading = false;
    this.cacheElements();
    this.bindEvents();
};

CardQuickCreator.prototype.cacheElements = function() {
    this.$template = $('.header').find('.card.m-creator');
    this.$button = $('.header__menu-link--add');
    this.$pageOverlay = $('.content__overlay');
    this.$cardCreator = this.createCardCreator();
};

CardQuickCreator.prototype.bindEvents = function() {
    this.$button.on('click', { self: this }, this.clickButtonEvent);
    $(document).on('click', { self: this }, this.clickOutsideEvent);
};

CardQuickCreator.prototype.createCardCreator = function() {
    var $cardCreator = this.$template.clone();
    $cardCreator.removeClass('m-hide').addClass('m-quick-creator').hide();
    $cardCreator.$fullOverlay = $cardCreator.find('.card__overlay');
    $cardCreator.prependTo('.header__menu');
    $cardCreator.find('.card__form--create').on('submit', { self: this }, this.createEvent);
    return $cardCreator;
};

CardQuickCreator.prototype.clickOutsideEvent = function(event) {
    var $target = $(event.target),
        self = event.data.self;
    if (!self.$cardCreator.is($target) && !self.$cardCreator.has($target).length && !$target.is(self.$button)) {
        self.$button.removeClass('active');
        self.$pageOverlay.fadeOut(150);
        self.$cardCreator.fadeOut(150);
    }
};

CardQuickCreator.prototype.clickButtonEvent = function(event) {
    var self = event.data.self;
    if (!self.loading) {
        if (self.$button.is('.active')) {
            self.close();
        } else {
            self.open();
        }
    }
};

CardQuickCreator.prototype.open = function() {
    this.$button.addClass('active');
    this.$pageOverlay.fadeIn(150);
    this.$cardCreator.fadeIn(150).find('input[type=text]').first().focus();
};

CardQuickCreator.prototype.close = function() {
    this.$button.removeClass('active');
    this.$pageOverlay.fadeOut(150);
    this.$cardCreator.fadeOut(150);
};

CardQuickCreator.prototype.createEvent = function(event) {
    event.preventDefault();
    var self = event.data.self,
        $form = $(this);
    self.loading = true;
    self.$cardCreator.hide();
    self.$button.removeClass('active').addClass('loading');
    self.$pageOverlay.fadeOut(150);
    $.ajax({
        url: $form.attr('action'),
        method: $form.attr('method'),
        data: new FormData($form[0]),
        cache: false,
        contentType: false,
        processData: false
    }).done(function(data) {
        $('.header__menu-repeat-count').text(data['cards_to_repeat_count']);
        self.loading = false;
        self.$button.removeClass('loading');
        self.$cardCreator.remove();
        self.$cardCreator = self.createCardCreator();
    }).error(function() {
        self.loading = false;
        self.$button.removeClass('loading');
        self.$button.addClass('active');
        self.$cardCreator.fadeIn(150);
        self.$pageOverlay.fadeIn(150);
        self.$cardCreator.$fullOverlay.css('opacity', '1').css('color', '#ff0000').text('Ошибка при добавлении').show();
        self.$cardCreator.$fullOverlay.show();
        setTimeout(function() {
            self.$cardCreator.$fullOverlay.css('opacity', '0.5').css('color', '#000').text('').hide();
        }, 1500);
    });
};
