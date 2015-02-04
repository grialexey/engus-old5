var CardList = function($cardListWrapper) {
    this.LEARN_MODE = 'learn';
    this.REPEAT_MODE = 'repeat';
    this.MODES = [this.LEARN_MODE, this.REPEAT_MODE];
    this.cardsToRepeatCount = 0;
    this.$wrapper = $cardListWrapper;
    this.$overlay = this.$wrapper.find('.card-list__overlay');
    this.$content = this.$wrapper.find('.card-list__content');
    this.$modeSwitcher = $('.card-list__modeswitch');
    this.$modeSwitcher.$items = this.$modeSwitcher.find('.card-list__modeswitch-item');
    this.cards = this.getCards();
    this.bindEvents();
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
    self.switchMode(mode);
};

CardList.prototype.switchMode = function(mode) {
    this.$modeSwitcher.removeClass(this.MODES.join(' ')).addClass(mode);
    this.$modeSwitcher.$items.removeClass('active').filter('.' + mode).addClass('active');
    switch(mode) {
        case 'learn':
            this.setLearnMode(this.cards);
            break;
        case 'repeat':
            this.setRepeatMode(this.cards);
            break;
    }
};

CardList.prototype.setLearnMode = function() {
    this.cardsToRepeatCount = 0;
    this.cards.forEach(function(card) {
        card.learn();
    });
};

CardList.prototype.setRepeatMode = function() {
    this.cardsToRepeatCount = this.cards.length;
    this.randomize();
    this.cards.forEach(function(card) {
        card.repeat();
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
    return this.$modeSwitcher.$items.filter('.active').data('mode');
};

CardList.prototype.reloadPage = function() {
    this.$overlay.appendTo(this.$content).show();
    var self = this,
        url = window.location.href;
    $.ajax({
        url: url,
        method: 'get'
    }).done(function(data) {
        self.$content.html(data);
        self.cards = self.getCards();
        self.switchMode(self.getMode());
    });
};

CardList.prototype.changePageEvent = function(event) {
    event.preventDefault();
    var self = event.data.self,
        $link = $(this),
        url = $link.attr('href');
    self.$overlay.appendTo(self.$content).show();
    $.ajax({
        url: url,
        method: 'get'
    }).done(function(data) {
        self.$content.html(data);
        if(url != window.location){
            window.history.pushState({ path:url }, '', url);
        }
        self.cards = self.getCards();
        self.switchMode(self.getMode());
    });
};