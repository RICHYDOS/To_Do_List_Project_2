#This is for the basic functionality of a To Do List: Add, Delete, Edit, etc

from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.models import CustomUser
from django.urls import reverse_lazy
from .models import Item

class UserItemView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = CustomUser
    template_name = "tasks.html"

    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk

class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "item_detail.html"

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = "item_delete.html"
    success_url = reverse_lazy("done")

    def test_func(self):
        obj = self.get_object()
        return obj.customer == self.request.user

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    template_name = "item_update.html"
    fields = ("title", "description")

    def test_func(self):
        obj = self.get_object()
        return obj.customer == self.request.user

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "item_new.html"
    fields = ("title", "description")

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

class DoneView(LoginRequiredMixin, TemplateView):
    template_name = "done.html"


