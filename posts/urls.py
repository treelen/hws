from django.urls import path
from posts import views

urlpatterns = [
    path("", views.get_index, name="index-page"),
    path("contacts/", views.get_contacts, name="contacts-page"),
    path("about/", views.get_about, name="about-page"),
    path("posts/<int:pk>", views.get_post, name="post-detail"),
]