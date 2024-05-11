from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from Account.models import Account
from home.models import Posting
user=get_user_model()

def home(request):
    user_id = request.user.id
    context = {}
    try:
        account = Account.objects.get(pk=user_id)
        if account:
            context['profile_image'] = account.ImageURL
    except:
        pass
    return render(request, 'home/home.html',context)

def job_posting(request):
    user_id = request.user.id
    customer = request.user.customer
    context = {}
    try:
        account = Account.objects.get(pk=user_id)
        if account:
            context['profile_image'] = account.ImageURL
    except:
        pass

    if request.method == 'POST':
        Posting.objects.create(
            customer=customer,
            title=request.POST['title'],
            abstract=request.POST['abstract'],
            detail_description=request.POST['description'],
            skills=request.POST['skills'],
            budget=request.POST['budget'],
            image=request.FILES['image']
        )
        return redirect('home')
    return render(request, 'home/job_posting.html',context)

def list_jobs(request):
    user_id = request.user.id
    customer = request.user.customer
    context = {}
    try:
        account = Account.objects.get(pk=user_id)
        if account:
            context['profile_image'] = account.ImageURL
    except:
        pass
    context['jobs'] = Posting.objects.filter(customer=customer)
    return render(request, 'home/list_jobs.html',context)

def list_all_jobs(request):
    user_id = request.user.id
    context = {}
    try:
        account = Account.objects.get(pk=user_id)
        if account:
            context['profile_image'] = account.ImageURL
    except:
        pass
    context['jobs'] = Posting.objects.all()
    return render(request, 'home/list_jobs.html',context)

def job_detail(request,job_id):
    user_id = request.user.id
    context = {}
    try:
        account = Account.objects.get(pk=user_id)
        if account:
            context['profile_image'] = account.ImageURL
    except:
        pass
    context['job'] = Posting.objects.get(pk=job_id)
    return render(request, 'home/job_detail.html',context)
