import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.db.models import Sum
from .models import StudentResult

def home(request):
    return render(request, 'index.html')

def about(request):
    # Automatically load all images from the static/images folder
    images_dir = os.path.join(settings.BASE_DIR, 'website', 'static', 'images')
    image_list = []
    if os.path.exists(images_dir):
        for filename in os.listdir(images_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                # Exclude the main logo and the student passport from the gallery
                if filename not in ['logo.png', 'passport.png']:
                    image_list.append(filename)
    return render(request, 'about.html', {'gallery_images': image_list})

def academics(request):
    return render(request, 'academics.html')

def admissions(request):
    return render(request, 'admissions.html')

def portal(request):
    return render(request, 'portal.html')

def contact(request):
    return render(request, 'contact.html')

# --- RESULT SECTION ---
def result_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('result_dashboard')
        else:
            messages.error(request, "Invalid Username or Password.")
    return render(request, 'results_login.html')

@login_required(login_url='result_login')
def result_dashboard(request):
    results = None
    selected_term = None
    selected_year = None
    total_score = 0
    average = 0
    position = "-"

    if request.method == 'POST':
        selected_term = request.POST.get('term')
        selected_year = request.POST.get('year')
        
        results = StudentResult.objects.filter(
            student=request.user,
            term=selected_term,
            year=selected_year
        )
        
        if results.exists():
            # Calculate Total and Average
            total_score = sum(r.total_score for r in results)
            average = round(total_score / results.count(), 2)
            
            # Calculate Position
            all_students = StudentResult.objects.filter(
                term=selected_term,
                year=selected_year
            ).values('student').annotate(grand_total=Sum('total_score')).order_by('-grand_total')
            
            for index, entry in enumerate(all_students):
                if entry['student'] == request.user.id:
                    position = index + 1
                    break

    return render(request, 'results_dashboard.html', {
        'results': results,
        'selected_term': selected_term,
        'selected_year': selected_year,
        'total_score': total_score,
        'average': average,
        'position': position,
    })

def result_logout(request):
    logout(request)
    return redirect('home')