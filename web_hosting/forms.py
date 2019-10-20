from django import forms

class RestaurantForm(forms.Form):
   user_input = forms.CharField(label='Search for questions related to restaurant', max_length=100)
   
