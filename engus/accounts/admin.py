# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Invite, CardsGoal


class InviteAdmin(admin.ModelAdmin):
    list_display = ('owner', 'registered_user', 'code', 'created', )
    raw_id_fields = ('owner', 'registered_user')
    readonly_fields = ('code', )


admin.site.register(Invite, InviteAdmin)
admin.site.register(CardsGoal)
