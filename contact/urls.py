from django.urls import path
from . import views


app_name = "contact"
urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    # Contact (CRUD)
    path('contact/<int:contact_id>/detail', views.contact_detail, name="contact_detail"),
    path('contact/<int:contact_id>/update', views.update, name="update"),
    path('contact/<int:contact_id>/delete', views.delete, name="delete"),
    path('contact/create', views.create_contact, name="create"),
]
