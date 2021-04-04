from django.contrib import admin

from passwords.models import EncPassword


class EncPasswordAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'username',)


admin.site.register(EncPassword, EncPasswordAdmin)
