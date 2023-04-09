# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Sample
from django.urls import reverse_lazy

# Create your views here.
class IndexList(ListView):
    model = Sample
    template_name = 'list.html'
    context_object_name = 'post_list'

class PostDetail(DetailView):
    model = Sample
    template_name = 'detail.html'
    context_object_name = 'post'

class PostNew(CreateView):
    model = Sample
    template_name = 'create.html'
    fields = ('title','text')
    success_url = reverse_lazy('list')

class PostUpdate(UpdateView):
    model = Sample
    template_name = 'update.html'
    fields = ('title','text')
    success_url = reverse_lazy('list')

class PostDelete(DeleteView):
    model = Sample
    template_name = 'delete.html'
    success_url = reverse_lazy('list')
