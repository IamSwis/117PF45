from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def home(request):
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            print("Send Email")

    else:
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})