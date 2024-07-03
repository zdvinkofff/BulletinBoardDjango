from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Advertisement
from .forms import AdvertisementForm

def home(request):
    return render(request, 'home.html')

def advertisement_list(request):
    advertisements = Advertisement.objects.all()
    return render(request, 'board/advertisement_list.html', {'advertisements': advertisements})

def advertisement_detail(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    return render(request, 'board/advertisement_detail.html', {'advertisement': advertisement})

@login_required
def add_advertisement(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.author = request.user
            advertisement.save()
            return redirect('board:advertisement_list')
    else:
        form = AdvertisementForm()
    return render(request, 'board/add_advertisement.html', {'form': form})

@login_required
def edit_advertisement(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, instance=advertisement)
        if form.is_valid():
            form.save()
            return redirect('board:advertisement_detail', pk=advertisement.pk)
    else:
        form = AdvertisementForm(instance=advertisement)
    return render(request, 'board/edit_advertisement.html', {'form': form})
