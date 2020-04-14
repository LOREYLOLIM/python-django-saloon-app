from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

# Create your views here.
def home(request):
    template = 'index.html'
    return  render(request, template)

def service(request):
    template = 'service.html'
    return  render(request, template)

def book(request):    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm
    template = 'report.html'
    context = {'form':form}
    template = 'book.html'
    return  render(request, template, context)

def time(request):
    Booking = Book.objects.all()
    context = {'Booking':Booking}
    template = 'time.html'
    return  render(request, template, context)