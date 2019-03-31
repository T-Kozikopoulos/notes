from django import forms
from .models import Note


class NoteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Note
        fields = ('title', 'content')
        required = ('title', 'content')
