from django.urls import path
from . import views
from .views import EventListView, EventCreateView, EventUpdateView, EventDetailView, EventDeleteView, ContactListView, ContactCreateView, ContactDetailView, ContactUpdateView, ContactDeleteView, HomePageUpdateView, HomePageDetailView, MyContactListView

urlpatterns = [
    path('', EventListView.as_view(), name='home'),
    path('event/new', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/update', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>', EventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/delete', EventDeleteView.as_view(), name='event-delete'),

    path('home/<int:pk>', HomePageDetailView.as_view(), name='home-detail'),
    path('home/update/<int:pk>', HomePageUpdateView.as_view(), name='home-update'),

    path('contact', ContactListView.as_view(), name='contact'),
    path('contact/new', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/update', ContactUpdateView.as_view(), name='contact-update'),
    path('contact/<int:pk>', ContactDetailView.as_view(), name='contact-detail'),
    path('contact/<int:pk>/delete', ContactDeleteView.as_view(), name='contact-delete'),


    path('contact/developer', MyContactListView.as_view(), name='my-contact'),




]
