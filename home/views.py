from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import EventType, ContactPost, HomePage
from .forms import EventForm, UpdateHomeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ColourView(object):
    def get_context_data(self, **kwargs):
        context = super(ColourView, self).get_context_data(**kwargs)
        context['home'] = HomePage.objects.all()[0]
        return context


class EventListView(ListView, ColourView):
    model = EventType
    template_name = 'home/home.html'
    context_object_name = 'events'
    ordering = ['priority']

    def get_context_data(self, *args, **kwargs):
        context = super(EventListView, self).get_context_data(*args, **kwargs)
        context['home'] = HomePage.objects.all()[0]
        return context


class EventDetailView(DetailView, ColourView):
    model = EventType
    template_name = 'home/detail_event.html'
    ordering = ['priority']

    def get_context_data(self, *args, **kwargs):
        context = super(EventDetailView, self).get_context_data(*args, **kwargs)
        context['events'] = EventType.objects.all()
        context['home'] = HomePage.objects.all()[0]
        return context


class EventCreateView(LoginRequiredMixin, FormView, ColourView):
    model = EventType
    template_name = 'home/create_event.html'
    form_class = EventForm
    success_url = '/'

    #fields = ['title', 'background_image', 'text_over_image', 'content', 'colour']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(EventCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EventCreateView, self).get_context_data(**kwargs)
        context['home'] = HomePage.objects.all()[0]
        return context


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, ColourView):
    model = EventType
    form_class = EventForm
    # fields = ['title', 'background_image', 'text_over_image', 'content', 'colour']
    template_name = 'home/create_event.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(EventUpdateView, self).get_context_data(**kwargs)
        context['home'] = HomePage.objects.all()[0]
        return context


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView, ColourView):
    model = EventType
    success_url = '/'
    template_name = 'home/delete_event.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(EventDeleteView, self).get_context_data(**kwargs)
        context['home'] = HomePage.objects.all()[0]
        return context
###################################################################################


class HomePageDetailView(DetailView):
    model = HomePage
    template_name = 'home/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageDetailView, self).get_context_data(*args, **kwargs)
        context['events'] = EventType.objects.all()
        context['home'] = HomePage.objects.all()[0]
        return context


class HomePageUpdateView(LoginRequiredMixin, UpdateView, ColourView):
    model = HomePage
    template_name = 'home/update_home.html'
    form_class = UpdateHomeForm

    #fields = ['title', 'background_image', 'content', 'colour']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageUpdateView, self).get_context_data(*args, **kwargs)
        context['home'] = HomePage.objects.all()[0]
        return context

###################################################################################


class ContactListView(ListView, ColourView):
    model = ContactPost
    template_name = 'contact/contact.html'
    context_object_name = 'contacts'
    ordering = ['priority']

    def get_context_data(self, *args, **kwargs):
        context = super(ContactListView, self).get_context_data(*args, **kwargs)
        context['contact'] = ContactPost.objects.all()[0]
        context['home'] = HomePage.objects.all()[0]
        return context


class MyContactListView(ListView, ColourView):
    model = ContactPost
    template_name = 'contact/contact.html'
    context_object_name = 'contacts'
    ordering = ['priority']

    def get_context_data(self, *args, **kwargs):
        context = super(MyContactListView, self).get_context_data(*args, **kwargs)
        context['contact'] = ContactPost.objects.all()[1]
        context['home'] = HomePage.objects.all()[0]
        return context


class ContactDetailView(DetailView, ColourView):
    model = ContactPost
    template_name = 'contact/detail_contact.html'


class ContactCreateView(LoginRequiredMixin, CreateView, ColourView):
    model = ContactPost
    template_name = 'contact/create_contact.html'

    fields = ['title', 'contact_text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ContactUpdateView(LoginRequiredMixin, UpdateView, ColourView):
    model = ContactPost
    fields = ['title', 'contact_text']
    template_name = 'contact/create_contact.html'
    success_url = '/contact'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ContactUpdateView, self).get_context_data(*args, **kwargs)
        context['home'] = HomePage.objects.all()[0]
        return context


class ContactDeleteView(LoginRequiredMixin, DeleteView, ColourView):
    model = ContactPost
    success_url = '/'
    template_name = 'contact/delete_contact.html'
