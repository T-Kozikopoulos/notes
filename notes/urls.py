from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='notes_index'),
    path('app/', views.app, name='notes_app'),
    path('delete/<pk>', views.NoteDelete.as_view(), name="delete_note"),
]
