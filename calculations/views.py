from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework import status
from django.template import loader
from .models import BillShare
from .serializers import BillShareSerializer



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

#endpoint for fetching bill shares for an apartment
class AppartmentBillSharesList(APIView):
    """
    GET  → Return a list of bill shares for an apartment (requires ?apartment=)
    POST → Create a new bill share (requires all serializer fields)
    """

    def get(self, request, format=None):

        apartment_id = request.query_params.get('apartment', None)
        if apartment_id is not None:
            shares = BillShare.objects.filter(apartment=apartment_id)
            serializer = BillShareSerializer(shares, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Apartment ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = BillShareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)