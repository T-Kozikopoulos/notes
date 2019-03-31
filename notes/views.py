from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from notes.forms import NoteForm
from .models import Note


@login_required
def index(request):
    notes = Note.objects.filter(author=request.user)
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.instance.author = request.user
        saved = form.save(commit=False)
        saved.save()
        return redirect('notes_index')

    context = {
        'notes': notes,
        'form': form
    }
    return render(request, 'notes/index.html', context)


def app(request):
    return render(request, 'notes/app.html')


class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('notes_index')
    template_name = 'notes/delete_note.html'
