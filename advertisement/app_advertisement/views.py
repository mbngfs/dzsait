from django.shortcuts import render, redirect
from .models import Advertisement
from forms import AdvertisementForm
from django.urls import reverse


def index(request):
    advertisements = Advertisement.objects.all
    context = {'advertisements': advertisements}
    return render(request, 'index.html')


def top_sellers(request):
    return render(request, 'top-sellers.html')


def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main_page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)
