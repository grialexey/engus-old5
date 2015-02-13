var CardList = function($cardListWrapper) {
    this.cardsToRepeatCount = 0;
    this.$wrapper = $cardListWrapper;
    this.$fullOverlay = this.$wrapper.find('.card-list__overlay');
    this.$content = this.$wrapper.find('.card-list__content');
    this.$modeSwitcher = $('.card-list__modeswitch');
    this.$filterSwitcher = $('.card-list__filter-list');
    this.$filterSwitcherLinks = this.$filterSwitcher.find('.card-list__filter-list-item-link');
    this.$toLearnCardsCount = this.$filterSwitcherLinks.filter('.m-to-learn').find('.card-list__filter-list-item-count');
    this.$newCardsCount = this.$filterSwitcherLinks.filter('.m-new ').find('.card-list__filter-list-item-count');
    this.$toRepeatCardsCount = this.$filterSwitcherLinks.filter('.m-to-repeat').find('.card-list__filter-list-item-count');
    this.$learnedCardsCount = this.$filterSwitcherLinks.filter('.m-learned').find('.card-list__filter-list-item-count');
    this.$modeSwitcher.$items = this.$modeSwitcher.find('.card-list__modeswitch-item');
    this.$pages = this.$content.find('.paginator__link');
    this.cards = this.getCards();
    this.bindEvents();
};

CardList.prototype.getModeInUrl = function() {
    var currentUrl = new Url;
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
    //this.$content.on('click', '.paginator__link', { self: this }, this.changePageEvent);
    this.$modeSwitcher.$items.on('click', { self: this }, this.switchModeEvent);
};

CardList.prototype.getCards = function() {
    var self = this,
        cards = [],
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
    self.changePagesUrls();
};

CardList.prototype.changePagesUrls = function() {
    var self = this;
    this.$pages.each(function() {
        var href = new Url($(this).attr('href')),
            url = new Url(),
            modeInUrl = self.getModeInUrl();
        if (modeInUrl) {
            href.query['mode'] = modeInUrl;
        } else {
            delete href.query['mode'];
        }
        $(this).attr('href', href.toString());
    })
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