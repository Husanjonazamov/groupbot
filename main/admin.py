from django.contrib import admin
from .models import User, Notice, Elonlarim


@admin.register(Elonlarim)
class ElonlarimAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at')  
    search_fields = ('description',)  




admin.site.register(User)
admin.site.register(Notice)

