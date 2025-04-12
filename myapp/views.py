from django.shortcuts import render



from django.shortcuts import render

def home(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')  # Use 'myapp/about.html' to ensure Django finds it

def skills(request):
    return render(request, 'myapp/skills.html')  # Similarly, specify the app folder for 'skills.html'

def services(request):
    return render(request, 'myapp/services.html')  # Specify app folder here too

def contactme(request):
    return render(request, 'myapp/contactme.html')  # Specify app folder here
