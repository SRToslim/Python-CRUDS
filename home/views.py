import os

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import CustomerCreateForm, UpdateProfileForm
from .models import Customer


def home(request):
    profile = Customer.objects.all()

    p = Paginator(Customer.objects.all().order_by('-id'), 4)
    page = request.GET.get('page')
    profile = p.get_page(page)
    nums = 'a' * profile.paginator.num_pages

    return render(request, 'index.html', {'profile': profile, 'nums': nums})


def create(request):
    if request.method == 'POST' or request.method == 'post':
        form = CustomerCreateForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            slug = user.name.replace(' ', '-')
            user.slug = slug.lower()
            user.save()
        messages.success(request, 'User successfully added.')
        return redirect('index')
    else:
        form = CustomerCreateForm()
        return render(request, 'create.html', {'form': form})


def view(request, slug):
    u = Customer.objects.get(slug=slug)

    return render(request, 'view.html', {'u': u})


def update(request, slug):
    if request.method == 'post' or request.method == 'POST':
        user = Customer.objects.get(slug=slug)
        form = UpdateProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            client = form.save(commit=False)
            slug = client.name.replace(' ', '-')
            client.slug = slug.lower()
            client.save()
        messages.success(request, 'User updated successfully.')
        return redirect('view', user.slug)
    else:
        user = Customer.objects.get(slug=slug)

        return render(request, 'edit.html', {'user': user})


def delete(request, slug):
    user = Customer.objects.get(slug=slug)
    if user.image != 'default_user.png':
        os.remove(user.image.path)
    user.delete()
    return redirect('index')


def search(request):
    query = request.GET.get('q')
    if query:
        profile = Customer.objects.filter(name__icontains=query)
    else:
        profile = Customer.objects.all()

    return render(request, 'index.html', {'profile': profile})
