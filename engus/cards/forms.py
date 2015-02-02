# -*- coding: utf-8 -*-
from django import forms


class CreateCardForm(forms.Form):
    front = forms.CharField(max_length=255)
    back = forms.CharField(max_length=255, required=False)
    example = forms.CharField(required=False)


class UpdateCardForm(forms.Form):
    id = forms.IntegerField()
    front = forms.CharField(max_length=255)
    back = forms.CharField(max_length=255, required=False)
    example = forms.CharField(required=False)


class DeleteCardForm(forms.Form):
    id = forms.IntegerField()
