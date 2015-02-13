var Card = function($element) {
    this.init($element);
};

Card.prototype.init = function($element) {
    this.cacheElements($element);
    this.bindEvents();
    this.isRegisteredUserOwned = this.$el.is('.m-user-owned');
    this.isToRepeat = this.$content.is('.m-to-repeat');
};

Card.prototype.destroy = function() {
    this.unbindEvents();
    this.$el.remove();
};

Card.prototype.cacheElements = function($element) {
    this.$el = $element;
    this.$infoline = this.$el.find('.card__infoline');
    this.$infoMenu = this.$el.find('.card__infomenu');
    this.$editControls = this.$el.find('.card__controls--edit');
    this.$levelChangeControls = this.$el.find('.card__controls--level-change');
    this.$fullOverlay = this.$el.find('.card__overlay.m-full');
    this.$rightOverlay = this.$el.find('.card__overlay.m-right');
    this.$leftOverlay = this.$el.find('.card__overlay.m-left');
    this.$content = this.$el.find('> .card__content');
    this.$back = this.$content.find('.card__back');
    this.$front = this.$content.find('.card__front');
    this.$frontContent = this.$content.find('.card__front > *');
    this.$image = this.$content.find('.card__image');
    this.$example = this.$content.find('.card__example');
    this.$deleteForm = this.$el.find('.card__form--delete');
    this.$editForm = this.$el.find('.card__form--update');
    this.$levelChangeForm = this.$el.find('.card__form--level');
    this.$editButton = this.$el.find('.card__button--edit');
    this.$playAudioBtn = this.$el.find('.card__front-pron.with-audio');
    this.$audio = this.$el.find('.card__audio');
    this.$editForm.$exampleTextArea = this.$editForm.find('.card__form-input[name=example]');

};

Card.prototype.bindEvents = function() {
    this.$deleteForm.on('submit', { self: this }, this.deleteCardEvent);
    this.$editForm.on('submit', { self: this }, this.updateCardEvent);
    this.$levelChangeForm.on('submit', { self: this }, this.updateCardLevelEvent);
    this.$content.on('click', { self: this }, this.clickOnContentEvent);
    this.$editButton.on('click', { self: this }, this.clickOnEditButtonEvent);
    this.$playAudioBtn.on('click', { self: this }, this.playAudioEvent);
    this.$rightOverlay.on('click', { self: this }, this.clickRightOverlayEvent);
    this.$leftOverlay.on('click', { self: this }, this.clickLeftOverlayEvent);
    $(document).on('click', { self: this }, this.clickOutsideEvent);
};

Card.prototype.unbindEvents = function() {
    this.$deleteForm.off('submit', this.deleteCardEvent);
    this.$editForm.off('submit', this.updateCardEvent);
    this.$levelChangeForm.off('submit', this.updateCardLevelEvent);
    this.$content.off('click', this.clickOnContentEvent);
    this.$editButton.off('click', this.clickOnEditButtonEvent);
    this.$playAudioBtn.off('click', this.playAudioEvent);
    this.$rightOverlay.off('click', this.clickRightOverlayEvent);
    this.$leftOverlay.off('click', this.clickLeftOverlayEvent);
    $(document).off('click', this.clickOutsideEvent);
};

Card.prototype.isEditable = function() {
    return this.$content.is('.editable');
};

Card.prototype.levelUp = function() {
    this.$content.removeClass('m-to-repeat');
};

Card.prototype.levelDown = function() {
    this.$content.addClass('m-to-repeat');
};

Card.prototype.playAudio = function() {
    if (this.$audio.length) {
        this.$audio[0].play();
    }
};

Card.prototype.playAudioEvent = function(event) {
    var self = event.data.self;
    event.stopPropagation();
    self.playAudio();
};

Card.prototype.clickOnContentEvent = function(event) {
    var self = event.data.self;
    if (self.isEditable()) {
        self.toggleControlsMenu();
    }
};

Card.prototype.clickRightOverlayEvent = function(event) {
    var self = event.data.self;
    self.normalMode();
    self.playAudio();
    self.$rightOverlay.removeClass('m-active');
    if (self.isToRepeat) {
        setTimeout(function() {
            self.$levelChangeControls.slideDown(200);
        }, 350);
    }
    //self.cardsToRepeatCount -= 1;
    //if (self.cardsToRepeatCount == 0) {
        //switchMode(NORMAL_MODE);
    //}
};

Card.prototype.clickLeftOverlayEvent = function(event) {
    var self = event.data.self;
    self.normalMode();
    self.playAudio();
    self.$leftOverlay.removeClass('m-active');
    if (self.isToRepeat) {
        setTimeout(function() {
            self.$levelChangeControls.slideDown(200);
        }, 550);
    }
    //self.cardsToRepeatCount -= 1;
    //if (self.cardsToRepeatCount == 0) {
        //switchMode(NORMAL_MODE);
    //}
};

Card.prototype.toggleControlsMenu = function() {
    this.$infoMenu.slideToggle(200);
    this.$content.show();
    this.$editForm.hide();
    this.$levelChangeControls.slideUp(100);
};

Card.prototype.closeControlsMenu = function() {
    this.$infoMenu.slideUp(100);
    this.$content.show();
    this.$editForm.hide();
    this.$levelChangeControls.slideUp(100);
};

Card.prototype.clickOutsideEvent = function(event) {
    var self = event.data.self;
    var $target = $(event.target);
    if (!self.$el.is($target) && !self.$el.has($target).length > 0) {
        self.closeControlsMenu();
    }
};

Card.prototype.clickOnEditButtonEvent = function(event) {
    var self = event.data.self;
    self.openEditForm();
};

Card.prototype.openEditForm = function() {
    this.$content.hide();
    this.$infoline.hide();
    this.$infoMenu.hide();
    this.$editForm.show();
};

Card.prototype.closeEditForm = function() {
    this.$editForm.hide();
    this.$content.show();
    this.$infoline.hide();
    this.$infoMenu.hide();
};

Card.prototype.normalMode = function() {
    this.$rightOverlay.removeClass('m-active');
    this.$leftOverlay.removeClass('m-active');
    this.$frontContent.removeClass('m-hide');
    this.$back.removeClass('m-hide');
    this.$example.removeClass('m-hide');
    this.$image.removeClass('m-hide');
    if (this.isRegisteredUserOwned) {
        this.$content.addClass('editable');
    }
};

Card.prototype.repeatRightMode = function() {
    this.$back.addClass('m-hide');
    this.$frontContent.removeClass('m-hide');
    this.$example.addClass('m-hide');
    this.$image.addClass('m-hide');
    this.$content.removeClass('editable');
    this.$leftOverlay.removeClass('m-active');
    this.$rightOverlay.addClass('m-active');
};

Card.prototype.repeatLeftMode = function() {
    this.$frontContent.addClass('m-hide');
    this.$back.removeClass('m-hide');
    this.$example.addClass('m-hide');
    this.$image.addClass('m-hide');
    this.$content.removeClass('editable');
    this.$rightOverlay.removeClass('m-active');
    this.$leftOverlay.addClass('m-active');
};

Card.prototype.deleteCardEvent = function(event) {
    event.preventDefault();
    var self = event.data.self;
    self.$el.hide();
    $.ajax({
        url: self.$deleteForm.attr('action'),
        method: 'post',
        data: self.$deleteForm.serialize()
    }).done(function() {
        self.$el.remove();
    }).error(function() {
        self.$el.show();
        self.$fullOverlay.addClass('m-active m-error').text('Ошибка при удалении');
        setTimeout(function() {
            self.$fullOverlay.removeClass('m-active m-error').text('');
        }, 1500);
    });
};

Card.prototype.updateCardLevelEvent = function(event) {
    event.preventDefault();
    var self = event.data.self,
        $form = $(this),
        levelChange = $form.find('input[name=level]').val();
    self.$levelChangeControls.slideUp(100);
    if (levelChange == 'up') {
        self.levelUp();
    } else if (levelChange == 'down') {
        self.levelDown();
    }
    if (self.isRegisteredUserOwned) {
        self.$fullOverlay.addClass('m-active');
        self.updateCardAjax($form);
    }
};

Card.prototype.updateCardEvent = function(event) {
    event.preventDefault();
    var self = event.data.self,
        $form = $(this);
    self.$fullOverlay.addClass('m-active');
    self.updateCardAjax($form);
};

Card.prototype.updateCardAjax = function($form) {
    var self = this;
    var formData = new FormData($form[0]);
    $.ajax({
        url: $form.attr('action'),
        method: $form.attr('method'),
        data: formData,
        cache: false,
        contentType: false,
        processData: false
    }).done(function(data) {
        $('.header__menu-repeat-count').text(data['cards_to_repeat_count']);
        var $updatedCardEl = $(data['card']);
        $updatedCardEl.insertAfter(self.$el);
        new Card($updatedCardEl);
        self.destroy();
    }).error(function() {
        $form.show();
        self.$fullOverlay.addClass('m-active m-error').text('Ошибка при сохранении');
        setTimeout(function() {
            self.$fullOverlay.removeClass('m-active m-error').text('');
        }, 1500);
    });
};