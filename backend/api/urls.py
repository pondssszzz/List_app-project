from django.urls import path
from .views import (
    MenuNoteRequest,
    MenuNotePost,
)

urlpatterns = [
    path('menunote/', MenuNoteRequest, name='MenuNoteRequest'),
    path('add/menunote/', MenuNotePost, name='MenuNotePost'),
]