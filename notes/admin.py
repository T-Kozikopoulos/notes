from django.contrib import admin
from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Note


admin.site.register(Note, NoteAdmin)
