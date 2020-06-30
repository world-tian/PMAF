from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import RegisterForm


def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {
            'register_form': register_form
        })
