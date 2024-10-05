""" Declares all of the views the pages will reach for"""

from django.shortcuts import render, redirect
# Everything under here I added
from .models import Owner, VehicleType, CarMake, CarInstance
from django.views import generic
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import OwnerForm  # the form is named owner form

# Views go under here
def home_page(request):
    # Get the current visit count from the session, or 0 if it doesn't exist
    num_visits = request.session.get('num_visits', 0)
    
    # Increment the visit count
    num_visits += 1
    
    # Save the new visit count to the session
    request.session['num_visits'] = num_visits

    if request.user.is_authenticated:
        # Render the authenticated user's home page
        # Generate counts of some of the main objects
        num_instances = CarInstance.objects.all().count()
        num_owners = Owner.objects.all().count()

        context = {
        'num_instances': num_instances,
        'num_owners': num_owners,
        'num_visits': num_visits,
    }
        return render(request, 'index.html', context=context)
    else:
        # Render the non-authenticated user's home page
        return render(request, 'no_auth_home.html', {'num_visits': num_visits})

def owner_success_view(request):
    return render(request, 'owner_success.html')


# Classes go under here
"""CAR related classes"""
class CarListView(ListView):
    model = CarInstance
    context_object_name = 'car_list'

class CarDetailView(DetailView):
    model = CarInstance 

"""OWNER related classes"""
class OwnerListView(ListView):
    model = Owner
    context_object_name = 'owner_list'  

class OwnerDetailView(DetailView):
    model = Owner

class OwnerCreateView(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'Owner_details.html'

    def get_success_url(self):
        return reverse('owner-success')  # Use the name of your success URL pattern
    
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle invalid form submission (e.g., return to the same page with errors)
        return super().form_invalid(form)
