from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Location
from civic_map import settings
from .forms import LocationForm, ReviewForm


def index(request):
    locations = Location.objects.all()
    paginator = Paginator(locations, 25)
    page = request.GET.get('page', default=1)
    try:
        locations = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        locations = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        locations = paginator.page(paginator.num_pages)
    context = {'locations': locations}

    return render(request, 'locations/index.html', context)


def view(request, id):
    location = get_object_or_404(Location, id=id)
    context = {
        'location': location,
        'reviews': location.review_set.all(),
    }

    return render(request, 'locations/view.html', context)


@login_required
def review(request, id):
    location = get_object_or_404(Location, id=id)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.location = location
            review.save()

            return redirect('locations:view', id=location.id)
    else:
        review_form = ReviewForm()

    context = {
        'location': location,
        'review_form': review_form,
    }

    return render(request, 'locations/review.html', context)


@login_required
def edit(request, id):
    location = get_object_or_404(Location, id=id)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            location = form.save(commit=False)
            location.user = request.user
            location.save()

            return redirect('locations:view', id=location.id)
    else:
        form = LocationForm(instance=location)

    context = {'form': form}

    return render(request, 'locations/edit.html', context)


@login_required
def new(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)

        if form.is_valid():
            location = form.save(commit=False)
            location.user = request.user
            location.save()

            return redirect('locations:view', id=location.id)
    else:
        form = LocationForm()

    context = {'form': form}

    return render(request, 'locations/edit.html', context)


def bigmap(request):
    locations = Location.objects.all()
    paginator = Paginator(locations, 10)

    page = request.GET.get('page', default=1)
    try:
        locations = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        locations = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        locations = paginator.page(paginator.num_pages)

    if len(locations) == 0:
        lat, lng = settings.EASY_MAPS_CENTER
    else:
        lat = sum(l.latitude for l in locations) / len(locations)
        lng = sum(l.longitude for l in locations) / len(locations)

    map_center = {
        'latitude': lat,
        'longitude': lng,
    }

    context = {
        'locations': locations,
        'map_center': map_center
    }

    return render(request, 'locations/bigmap.html', context)
