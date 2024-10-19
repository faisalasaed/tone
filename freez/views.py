from django.shortcuts import render

def home(request):
    return render(request, 'freez/home.html')  # تأكد من وجود home.html في المسار الصحيح

def about(request):
    return render(request, 'hot/about.html')  # تأكد من وجود about.html في المسار الصحيح
