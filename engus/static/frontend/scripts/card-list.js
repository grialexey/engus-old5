var CardList = function($cardListWrapper) {
    this.cardsToRepeatCount = 0;
    this.$wrapper = $cardListWrapper;
    this.$fullOverlay = this.$wrapper.find('.card-list__overlay');
    this.$content = this.$wrapper.find('.card-list__content');
    this.$modeSwitcher = $('.card-list__modeswitch');
    this.$modeSwitcher.$items = this.$modeSwitcher.find('.card-list__modeswitch-item');
    this.cards = this.getCards();
    this.bindEvents();
};

CardList.prototype.getModeInUrl = function() {
    var currentUrl = new Url;
    console.log(currentUrl.toString());
    return currentUrl.query['mode'];
};

CardList.prototype.setModeInUrl = function(mode) {
    var currentUrl = new Url;
    if (mode === null) {
        delete currentUrl.query['mode'];
        window.history.pushState({}, '', currentUrl.toString());
    } else {
        currentUrl.query['mode'] = mode;
        window.history.pushState({}, '', currentUrl.toString());
    }
};

CardList.prototype.bindEvents = function() {
    this.$content.on('click', '.pages__link', { self: this }, this.changePageEvent);
    this.$modeSwitcher.$items.on('click', { self: this }, this.switchModeEvent);
};

CardList.prototype.getCards = function() {
    var cards = [],
        $cards = this.$content.find('.card');
    $cards.each(function() {
        cards.push(new Card($(this)));
    });
    return cards;
};

CardList.prototype.switchModeEvent = function(event) {
    var self = event.data.self;
    var mode = $(this).data('mode');
    self.$modeSwitcher.$items.removeClass('m-active');
    switch(mode) {
        case 'normal':
            self.setNormalMode(self.cards);
            self.$modeSwitcher.removeClass('m-normal m-repeat m-repeat-right m-repeat-left');
            self.$modeSwitcher.addClass('m-normal');
            self.$modeSwitcher.$items.filter('.m-normal').addClass('m-active');
            self.setModeInUrl(null);
            break;
        case 'repeat':
            if (self.$modeSwitcher.is('.m-repeat-right')) {
                self.setRepeatLeftMode(this.cards);
                self.$modeSwitcher.removeClass('m-normal m-repeat m-repeat-right m-repeat-left');
                self.$modeSwitcher.addClass('m-repeat m-repeat-left');
                self.$modeSwitcher.$items.filter('.m-repeat').addClass('m-active').removeClass('m-repeat-right').addClass('m-repeat-left');
                self.setModeInUrl('repeat-left');
            } else {
                self.setRepeatRightMode(this.cards);
                self.$modeSwitcher.removeClass('m-normal m-repeat m-repeat-right m-repeat-left');
                self.$modeSwitcher.addClass('m-repeat m-repeat-right');
                self.$modeSwitcher.$items.filter('.m-repeat').addClass('m-active').removeClass('m-repeat-left').addClass('m-repeat-right');
                self.setModeInUrl('repeat-right');
            }
            break;
    }
};

CardList.prototype.setNormalMode = function() {
    this.cardsToRepeatCount = 0;
    this.cards.forEach(function(card) {
        card.normalMode();
    });
};

CardList.prototype.setRepeatRightMode = function() {
    this.cardsToRepeatCount = this.cards.length;
    this.randomize();
    this.cards.forEach(function(card) {
        card.repeatRightMode();
    });
};

CardList.prototype.setRepeatLeftMode = function() {
    this.cardsToRepeatCount = this.cards.length;
    this.randomize();
    this.cards.forEach(function(card) {
        card.repeatLeftMode();
    });
};

CardList.prototype.randomize = function() {
    var self = this;
    this.cards.sort(function(card) {
        return Math.round(Math.random())-0.5;
    }).forEach(function(card) {
        card.$el.detach().appendTo(self.$content.find('.card-list__list'));
    });
};

CardList.prototype.getMode = function() {
    return this.$modeSwitcher.$items.filter('.m-active').data('mode');
};

CardList.prototype.reloadPage = function() {
    this.$fullOverlay.appendTo(this.$content).show();
    var self = this,
        url = window.location.href;
    $.ajax({
        url: url,
        method: 'get'
    }).done(function(data) {
        self.$content.html(data);
        self.cards = self.getCards();
    });
};

CardList.prototype.changePageEvent = function(event) {
    event.preventDefault();
    var self = event.data.self,
        $link = $(this),
        modeInUrl = self.getModeInUrl(),
        href = $link.attr('href'),
        url = new Url(href);
    if (modeInUrl) {
        url.query['mode'] = modeInUrl;
    } else {
        delete url.query['mode'];
    }
    self.$fullOverlay.appendTo(self.$content).show();
    $.ajax({
        url: url.toString(),
        method: 'get'
    }).done(function(data) {
        self.$content.html(data);
        if(url != window.location){
            window.history.pushState({}, '', url.toString());
        }
        self.cards = self.getCards();
    });
};