from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def main():
    print("Hello world! My name is...")

def home(request):
    template = loader.get_template('MainPage/myfirst.html')
    return HttpResponse(template.render())