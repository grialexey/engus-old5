# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Invite


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=254, label=u'Имя пользователя',
        help_text=u'Не более 30 символов. Только <b>латинские</b> буквы, цифры и символы @/./+/-/_.')
    email = forms.EmailField(required=True)
    invite_code = forms.CharField(max_length=20, label=u'Ваше приглашение', required=True)

    class Meta:
        model = User
        fields = ('username', 'email', )

    def clean_invite_code(self):
        invite_code = self.cleaned_data['invite_code']
        try:
            invite_obj = Invite.objects.get(code=invite_code)
            if invite_obj.registered_user is not None:
                raise forms.ValidationError(u'Это приглашение уже использовали', code='invalid')
        except Invite.DoesNotExist:
            raise forms.ValidationError(u'Недействительное приглашение', code='invalid')
        return invite_code