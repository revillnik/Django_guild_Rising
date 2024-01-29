from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    UpdateView,
    CreateView,
    TemplateView,
    ListView,
    DetailView,
    FormView,
    DeleteView,
)
from .models import all_information


def linkings(s):
    s = s.split(",")
    links = []
    for i in range(len(s)):
        s[i] = s[i].strip("\r\n.,")
        s[i] = s[i].replace(" ", "")
        if "://" in s[i]:
            links.append(s[i])
    s = links
    return s


class Home(ListView):
    template_name = "guild/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return all_information.objects.all()


class ShowPost(DetailView):
    template_name = "guild/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        links = context["post"].link
        context["post"].link = linkings(links)
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(all_information, slug=self.kwargs[self.slug_url_kwarg])
