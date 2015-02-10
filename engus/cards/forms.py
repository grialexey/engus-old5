# -*- coding: utf-8 -*-
from django import forms
from .models import Card, CardFront


class CardForm(forms.ModelForm):
    front = forms.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CardForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(CardForm, self).clean()
        self.cleaned_data['back'] = self.cleaned_data['back'].strip()
        self.cleaned_data['example'] = self.cleaned_data['example'].strip()
        self.cleaned_data['front'] = self.cleaned_data['front'].strip()

    def get_card_front(self):
        front = self.cleaned_data['front']
        try:
            card_front_obj = CardFront.objects.filter(text__iexact=front, is_public=True)[0]
        except IndexError:
            card_front_obj = CardFront.objects.create(text=front, author=self.user)
        self.instance.front = card_front_obj

    class Meta:
        model = Card
        fields = ['back', 'example', ]


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
            self.instance.level_up()
        elif level_change == UpdateCardLevelForm.DOWN:
            self.instance.level_down()

    class Meta:
        model = Card
        fields = []


class DeleteCardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = []
