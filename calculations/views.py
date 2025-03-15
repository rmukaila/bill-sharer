from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def calculations(request):
    template = loader.get_template('base.html')
    return HttpResponse (template.render())

# endpoint for creating appartment including handling creating
# bill shares, adding members to the apartment etc
def create_apartment(request):
    pass

# endpoint for adding members to an apartment
def add_member(request):
    pass

# endpoint for adding bill shares to an apartment
def add_bill_share(request):
    pass    