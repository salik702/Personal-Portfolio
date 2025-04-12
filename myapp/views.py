from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages  

def home(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def skills(request):
    return render(request, 'myapp/skills.html')

def services(request):
    return render(request, 'myapp/services.html')

def contactme(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')  
            return redirect('contactme')  
    else:
        form = ContactForm()
    return render(request, 'myapp/contactme.html', {'form': form})
