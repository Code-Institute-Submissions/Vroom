from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Car, TrackDayAddon, InsuranceAddon, PrivateDriverAddon
from .forms import CarRegistrationForm, CarUpdateForm


def all_cars(request):
    """Function to display all cars into the search page"""

    cars = Car.objects.all()
    return render(request, "findcar.html", {"cars": cars})


def custom_classic_only(request):
    """Function to display only Custom Classic cars into the search page"""

    CS = Car.objects.filter(car_class="Custom Classic")
    return render(request, "findcar.html", {"cars": CS})


def luxury_only(request):
    """Function to display only Luxury cars into the search page"""

    LX = Car.objects.filter(car_class="Luxury")
    return render(request, "findcar.html", {"cars": LX})


def supersport_only(request):
    """Function to display only Supersport cars into the search page"""

    SS = Car.objects.filter(car_class="Supersport")
    return render(request, "findcar.html", {"cars": SS})


@login_required
def car_register(request):
    """Function to allow users to add their cars to the database"""

    if request.method == 'POST':
        form = CarRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            car_reg_form = form.save(commit=False)
            car_reg_form.car_owner = request.user
            form.save()

            messages.success(request, "Your car is ready to Vroom!")
            return redirect(reverse('index'))
        else:
            messages.error(
                request,
                "We were unable to add your car! Please check the information"
            )

    else:
        car_reg_form = CarRegistrationForm()
    args = {'crf': car_reg_form}
    return render(request, 'rentmycar.html', args)


def car_detail(request, car_id):
    """
    Function to display expanded details of the chosen car based on its ID
    """

    car = Car.objects.get(pk=car_id)

    return render(request, 'cardetail.html', {'car': car})


@login_required
def edit_car(request, car_id):
    """Function to allow user to edit their own cars"""

    instance = get_object_or_404(Car, id=car_id)

    form = CarUpdateForm(
                         request.POST or None,
                         request.FILES or None,
                         instance=instance
                        )
    if request.method == 'POST':

        if form.is_valid():

            form.save()

            messages.error(request, "Your car has been successfully updated!")
            return redirect(reverse('index'))
        else:
            messages.error(
                request,
                "We were unable to update your car!"
            )

    else:
        form = CarUpdateForm(instance=instance)

    args = {'car_edit_form': form, 'car': instance}
    return render(request, 'editcar.html', args)


@login_required
def delete_car(request, car_id):
    """Function to allow users to delete their own profile"""

    c = Car.objects.get(pk=car_id)
    c.delete()
    messages.success(request, "The car was deleted")

    return redirect(reverse('index'))


def add_ons(request, item_type):
    """
    Function to add other products to their cart after choosing a car
    """

    if item_type == 'car':
        addon = TrackDayAddon.objects.all()
    elif item_type == 'track_day':
        addon = TrackDayAddon.objects.all()
    elif item_type == 'insurance':
        addon = InsuranceAddon.objects.all()
    elif item_type == 'private_driver':
        addon = PrivateDriverAddon.objects.all()

    return render(
                request,
                'addons.html',
                {
                    'item_type': item_type,
                    'addon': addon,
                })
