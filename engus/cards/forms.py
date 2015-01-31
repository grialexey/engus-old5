# -*- coding: utf-8 -*-
from django import forms


class NewCardForm(forms.Form):
    front = forms.CharField(max_length=255)
    back = forms.CharField(max_length=255, required=False)