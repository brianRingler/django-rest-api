# This is the API view class. We are using this in-place of Django's View class
from rest_framework.views import APIView
from rest_framework.response import Response
# List of HTTP status codes 
from rest_framework import status

# from our profiles_api_app directory import serializers.py 
from profiles_api_app import serializers


class HelloApiView(APIView):
    '''Test API View'''
    # this is the serializer class created in serializer.py
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''Returns a list of APIView features'''

        an_apiview = [
            'Uses HTTP methods: get, push, patch, post, delete',
            'Is similar to a traditional Django View',
            'Gives you the most control over the application logic',
            'Is mapped manually to URL\'s',
        ]
        # Every function added to an APIView that is an HTTP method must return response object
        # it most be a list or a dictionary 
        return Response({'message': 'hello', 'an_apiview': an_apiview})

    def post(self, request):
        '''We are getting some data from the POST request and passing it to the 
        variable we created above. This value should have max char of 10.'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validation_data.get('name')
