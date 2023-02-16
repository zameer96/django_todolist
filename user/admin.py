from django.contrib import admin
from user.models import User

@admin.register(User)
class userAdmin(admin.ModelAdmin):
    pass

