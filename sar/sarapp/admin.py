from django.contrib import admin
from .models import TextEntry
# Register your models here.
class TextEntryAdmin(admin.ModelAdmin):
    list_display=('id','text','sentiment_score')
    search_fields=('text',)
admin.site.register(TextEntry,TextEntryAdmin)    