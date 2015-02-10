# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=254, label=u'Имя пользователя',
                               help_text=u'Не более 30 символов. Только <b>латинские</b> буквы, цифры и символы @/./+/-/_.')
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', )