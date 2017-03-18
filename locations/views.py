from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    get_list_or_404
)
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Location
from .forms import LocationForm


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
    context = {'location': location}

    return render(request, 'locations/view.html', context)


@login_required
def edit(request, id):
    location = get_object_or_404(Location, id=id)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            location = form.save(commit=False)
            location.user = request.user
            location.save()
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

            return redirect(
                reverse('locations:edit', args=[location.id])
            )
    else:
        form = LocationForm()

    context = {'form': form}

    return render(request, 'locations/edit.html', context)
