from django.contrib import admin

from .models import Venue, Court, SocialGame

admin.site.register(Venue)
admin.site.register(Court)
admin.site.register(SocialGame)