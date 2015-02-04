var Card = function($element) {
    this.$el = $element;
    this.$infoline = this.$el.find('.card__infoline');
    this.$editControls = this.$el.find('.card__controls--edit');
    this.$overlay = this.$el.find('.card__overlay');
    this.$content = this.$el.find('.card__content');
    this.$back = this.$content.find('.card__back');
    this.$front = this.$content.find('.card__front');
    this.$image = this.$content.find('.card__image');
    this.$example = this.$content.find('.card__example');
    this.$deleteForm = this.$el.find('.card__form--delete');
    this.$editForm = this.$el.find('.card__form--update');
    this.$editButton = this.$el.find('.card__button--edit');
    this.bindEvents();
};

Card.prototype.bindEvents = function() {
    this.$deleteForm.on('submit', this.deleteCardEvent.bind(this));
    this.$editForm.on('submit', this.updateCardEvent.bind(this));
    this.$content.on('click', this.clickOnContentEvent.bind(this));
    this.$editButton.on('click', this.clickOnEditButtonEvent.bind(this));
    $(document).on('click', this.clickOutsideEvent.bind(this));
};

Card.prototype.isEditable = function() {
    return this.$content.is('.editable')
};

Card.prototype.clickOnContentEvent = function() {
    if (this.isEditable()) {
        this.toggleControls();
    }
};

Card.prototype.toggleControls = function() {
    this.$editControls.toggle();
    this.$infoline.toggle();
    this.$content.show();
    this.$editForm.hide();
};

Card.prototype.closeControls = function() {
    this.$editControls.hide();
    this.$infoline.hide();
    this.$content.show();
    this.$editForm.hide();
};

Card.prototype.clickOutsideEvent = function(event) {
    var $target = $(event.target);
    if (!this.$el.is($target) && !this.$el.has($target).length > 0) {
        this.closeControls();
    }
};

Card.prototype.clickOnEditButtonEvent = function(event) {
    this.openEditForm();
};

Card.prototype.openEditForm = function() {
    this.$content.hide();
    this.$infoline.hide();
    this.$editControls.hide();
    this.$editForm.show();
};

Card.prototype.closeEditForm = function() {
    this.$editForm.hide();
    this.$content.show();
    this.$infoline.hide();
    this.$editControls.hide();
};

Card.prototype.learn = function() {
    this.$overlay.hide();
    this.$back.show();
    this.$example.show();
    this.$image.show();
    this.$content.addClass('editable');
};

Card.prototype.repeat = function() {
    this.$overlay.hide();
    this.$back.hide();
    this.$example.hide();
    this.$image.hide();
    this.$content.removeClass('editable');
    this.$overlay.addClass('right');
    this.$overlay.show().text('Показать');
    var self = this;
    this.$overlay.one('click', function() {
        //self.cardsToRepeatCount -= 1;
        self.learn();
        self.$overlay.hide().removeClass('right').text('');
        //if (self.cardsToRepeatCount == 0) {
            //switchMode(LEARN_MODE);
        //}
    });
};

Card.prototype.deleteCardEvent = function(event) {
    event.preventDefault();
    this.$el.hide();
    var self = this;
    $.ajax({
        url: self.$deleteForm.attr('action'),
        method: 'post',
        data: self.$deleteForm.serialize()
    }).done(function() {
        self.$el.remove();
    }).error(function() {
        self.$el.show();
        self.$overlay.css('color', '#ff0000').text('Ошибка при удалении').show();
        setTimeout(function() {
            self.$overlay.css('color', '#000').text('').hide();
        }, 1500);
    });
};

Card.prototype.updateCardEvent = function(event) {
    event.preventDefault();
    this.$overlay.show();
    var self = this;
    $.ajax({
        url: self.$editForm.attr('action'),
        method: 'post',
        data: self.$editForm.serialize()
    }).done(function(data) {
        self.$overlay.hide();
        self.$el.html(data);
    }).error(function() {
        self.$editForm.show();
        self.$overlay.css('opacity', '1').css('color', '#ff0000').text('Ошибка при сохранении');
        setTimeout(function() {
            self.$overlay.hide();
            self.$overlay.css('opacity', '0.5');
        }, 1500);
    });
};