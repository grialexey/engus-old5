# -*- coding: utf-8 -*-
from django import forms
from .models import Card, CardFront


class CardForm(forms.ModelForm):
    front = forms.CharField(max_length=255)

    def clean(self):
        super(CardForm, self).clean()
        self.cleaned_data['back'] = self.cleaned_data['back'].strip()
        self.cleaned_data['example'] = self.cleaned_data['example'].strip()
        self.cleaned_data['front'] = self.cleaned_data['front'].strip()
        article = self.cleaned_data['article']
        if article and article.card_set.count() > 12:
            raise forms.ValidationError('Не более 12 карточек в статье')


    class Meta:
        model = Card
        fields = ['back', 'example', 'article', 'image', ]


class UpdateCardLevelForm(forms.ModelForm):
    UP = 'up'
    DOWN = 'down'

    LEVEL_CHOICES = (
        (UP, 'Up'),
        (DOWN, 'Down'),
    )

    level = forms.ChoiceField(choices=LEVEL_CHOICES)

    def update_level(self):
        level_change = self.cleaned_data.get('level')
        if level_change == UpdateCardLevelForm.UP:
            self.instance.good()
        elif level_change == UpdateCardLevelForm.DOWN:
            self.instance.bad()

    class Meta:
        model = Card
        fields = []


class DeleteCardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = []
