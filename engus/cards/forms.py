# -*- coding: utf-8 -*-
from django import forms


class CreateCardForm(forms.Form):
    front = forms.CharField(max_length=255)
    back = forms.CharField(max_length=255, required=False)
    example = forms.CharField(required=False)


class UpdateCardForm(forms.Form):
    pk = forms.IntegerField()
    front = forms.CharField(max_length=255)
    back = forms.CharField(max_length=255, required=False)
    example = forms.CharField(required=False)


class UpdateCardLevelForm(forms.Form):
    UP = 'up'
    DOWN = 'down'

    LEVEL_CHOICES = (
        (UP, 'Up'),
        (DOWN, 'Down'),
    )

    pk = forms.IntegerField()
    level = forms.ChoiceField(choices=LEVEL_CHOICES)


class DeleteCardForm(forms.Form):
    pk = forms.IntegerField()
