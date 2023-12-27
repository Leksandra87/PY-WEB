from django.shortcuts import render
from datetime import datetime

from django.views import View
from django.http import HttpResponse
from random import randint
from django.shortcuts import render


class CurrentDateView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)


class RandomView(View):
    def get(self, request):
        html = f"{randint(0, 1000)}"
        return HttpResponse(html)


class HelloView(View):
    def get(self, request):
        html = """<h1>Hello, World</h1>"""
        return HttpResponse(html)


def current(request):  # функциональный подход
    if request.method == "GET":
        html = f"{datetime.now()}"
        return HttpResponse(html)


class IndexView(View):
    def get(self, request):
        return render(request, 'first/index.html')

# class JsonView(View):
#     def get(self, request):
#         return render(request, 'first/course.json')


# Create your views here.
