from django.shortcuts import render, redirect, HttpResponse
from django.views import View


class Index(View):
    def get(self, request):
        return HttpResponse('index')
