# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import CardsGoal


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=254, label=u'Имя пользователя',
        help_text=u'Не более 30 символов. Только <b>латинские</b> буквы, цифры и символы @/./+/-/_.')
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', )


class CardsGoalForm(forms.ModelForm):
    days = forms.IntegerField(min_value=1, required=True, label=u'Через дней')

    class Meta:
        model = CardsGoal
        fields = ['number', ]