var Card = function($element) {
    this.$el = $element;
    this.init();
};

Card.prototype.init = function() {
    this.cacheElements();
    this.bindEvents();
    this.isRegisteredUserOwned = this.$el.is('.m-user-owned');
    this.isRepeatedToday = this.$level.is('.m-repeated-today');
};

Card.prototype.cacheElements = function() {
    this.$infoline = this.$el.find('.card__infoline');
    this.$infoMenu = this.$el.find('.card__infomenu');
    this.$editControls = this.$el.find('.card__controls--edit');
    this.$levelChangeControls = this.$el.find('.card__controls--level-change');
    this.$overlay = this.$el.find('.card__overlay');
    this.$content = this.$el.find('> .card__content');
    this.$back = this.$content.find('.card__back');
    this.$front = this.$content.find('.card__front');
    this.$image = this.$content.find('.card__image');
    this.$example = this.$content.find('.card__example');
    this.$deleteForm = this.$el.find('.card__form--delete');
    this.$editForm = this.$el.find('.card__form--update');
    this.$levelChangeForm = this.$el.find('.card__form--level');
    this.$editButton = this.$el.find('.card__button--edit');
    this.$playAudioBtn = this.$el.find('.card__front-pron.with-audio');
    this.$audio = this.$el.find('.card__audio');
    this.$level = this.$el.find('.card__level');
    this.$editForm.$exampleTextArea = this.$editForm.find('.card__form-input[name=example]');

};

Card.prototype.bindEvents = function() {
    this.$deleteForm.on('submit', { self: this }, this.deleteCardEvent);
    this.$editForm.on('submit', { self: this }, this.updateCardEvent);
    this.$levelChangeForm.on('submit', { self: this }, this.updateCardLevelEvent);
    this.$content.on('click', { self: this }, this.clickOnContentEvent);
    this.$editButton.on('click', { self: this }, this.clickOnEditButtonEvent);
    this.$playAudioBtn.on('click', { self: this }, this.playAudioEvent);
    this.$overlay.on('click', { self: this }, this.clickOverlayEvent);
    $(document).on('click', { self: this }, this.clickOutsideEvent);
};

Card.prototype.isEditable = function() {
    return this.$content.is('.editable');
};

Card.prototype.getLevel = function() {
    return parseInt(this.$level.data('level'));
};

Card.prototype.setLevel = function(level) {
    this.$level
        .removeClass('level1 level2 level3 level4 level5')
        .addClass('level' + level)
        .text(level)
        .data('level', level);
};

Card.prototype.levelUp = function() {
    var level = this.getLevel();
    if (level == 0) {
        this.setLevel(2);
    } else if (level < 5) {
        this.setLevel(level + 1);
    }
};

Card.prototype.levelDown = function() {
    this.setLevel(1);
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

Card.prototype.clickOverlayEvent = function(event) {
    var self = event.data.self;
    if ($(this).filter('.right')) {
        self.learn();
        self.$overlay.hide().removeClass('right').text('').css('z-index', '10');
        if (!self.isRepeatedToday) {
            setTimeout(function() {
                self.$levelChangeControls.slideDown(200);
            }, 350);
        }
        //self.cardsToRepeatCount -= 1;
        //if (self.cardsToRepeatCount == 0) {
            //switchMode(LEARN_MODE);
        //}

    }
};

Card.prototype.toggleControlsMenu = function() {
    this.$infoMenu.slideToggle(200);
    this.$content.show();
    this.$editForm.hide();
    this.$levelChangeControls.hide();
};

Card.prototype.closeControlsMenu = function() {
    this.$infoMenu.hide();
    this.$content.show();
    this.$editForm.hide();
    this.$levelChangeControls.hide();
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
    if (this.isRegisteredUserOwned) {
        this.$content.addClass('editable');
    }
};

Card.prototype.repeat = function() {
    this.$overlay.hide();
    this.$back.hide();
    this.$example.hide();
    this.$image.hide();
    this.$content.removeClass('editable');
    this.$overlay.addClass('right');
    this.$overlay.show().text('Показать').css('z-index', '3');
    var self = this;
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
        self.$overlay.css('opacity', '1').css('color', '#ff0000').text('Ошибка при удалении').show();
        setTimeout(function() {
            self.$overlay.css('opacity', '0.5').css('color', '#000').text('').hide();
        }, 1500);
    });
};

Card.prototype.updateCardLevelEvent = function(event) {
    event.preventDefault();
    var self = event.data.self,
        $form = $(this),
        levelChange = $form.find('input[name=level]').val();
    self.$levelChangeControls.hide();
    if (levelChange == 'up') {
        self.levelUp();
    } else if (levelChange == 'down') {
        self.levelDown();
    }
    if (self.isRegisteredUserOwned) {
        self.updateCardAjax($form);
    }
};

Card.prototype.updateCardEvent = function(event) {
    event.preventDefault();
    var self = event.data.self,
        $form = $(this);
    self.$overlay.show();
    self.updateCardAjax($form);
};

Card.prototype.updateCardAjax = function($form) {
    var self = this;
    $.ajax({
        url: $form.attr('action'),
        method: $form.attr('method'),
        data: $form.serialize()
    }).done(function(data) {
        self.$overlay.hide();
        self.$el.html(data);
        self.init();
    }).error(function() {
        $form.show();
        self.$overlay.show().css('opacity', '1').css('color', '#ff0000').text('Ошибка при сохранении');
        setTimeout(function() {
            self.$overlay.hide();
            self.$overlay.css('opacity', '0.5').css('color', '#000').text('');
        }, 1500);
    });
};