import random
import string

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View

from .forms import GenerateForm, CompareForm
from .models import User, Molecular


class HomeView(View):
    def get(self, *args, **kwargs):
        form = GenerateForm(self.request.GET or None)
        context = {"form": form}
        if form.is_valid():
            # 여기서 moflow 함수 실행
            random_molecular = [(''.join(random.choice(string.ascii_letters.capitalize()) for _ in range(10))) for _ in range(10)]
            context['data'] = form.cleaned_data
            context['molecular_list'] = random_molecular[:5]
        return render(self.request, "home.html", context)


class DetailView(View):
    def get(self, *args, **kwargs):
        molecular = kwargs['id']    
        context = {"id": molecular}
        return render(self.request, "detail.html", context)

    def post(self, *args, **kwargs):
        pass


class CompareView(View):
    def get(self, *args, **kwargs):
        form = CompareForm(self.request.GET or None)
        context = {"form": form}
        if form.is_valid():
            context['data'] = form.cleaned_data
        return render(self.request, "compare.html", context)

    def post(self, *args, **kwargs):
        pass


class SavedListView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "savedList.html")

    def post(self, *args, **kwargs):
        pass