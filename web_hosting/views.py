from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .forms import RestaurantForm

def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = RestaurantForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            print(form.cleaned_data['search'])

            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = RestaurantForm() # An unbound form
    # Render the HTML template index.html with the data in the context variable
    return render(request,'index.html',{'form': form})
# Create your views here.
