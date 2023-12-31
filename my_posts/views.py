from django.shortcuts import render
from django.http import HttpResponse

from .models import Quote


def index(request):
    quotes = Quote.objects.all()
    return render(request, 'my_quotes/quotes.html', {'quotes': quotes})
