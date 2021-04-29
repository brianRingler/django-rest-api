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

        # There are multiple validators we can use to validate 
        if serializer.is_valid():
            # Here we are validating that the name is at least 10 characters
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            # if we have status 200 return a dict response object of our validated message
            return Response({'message' : message})
        else:
            # if not status 200 inform requester of bad request
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                 )

    def put(self, request, pk=None):
        '''
        Handle updating an entire object based on primary key. This would 
        be same as ModelName.objects.get(id=pk)'''
        # Here we are just returning a response and not updating our empty db
        return Response({
                        'id' : pk,
                        'method' : 'PUT'
                        })

    def patch(self, request, pk=None):
        '''patch will handle a partial update of an object. If we had a model with
        first_name, last_name, dob, favorite_food then this would update on the first
        and name for the user. We would query the db and then only update required
        fields based on keys'''
        return Response({
                        'id' : pk,
                        'first_name' : 'Teddy' , 
                        'last_name' : 'Cool', 
                        'method' : 'PATCH'
                        })
    def delete(self, request, pk=None):
        '''Like PUT and UPDATE we are going to DELETE a record from our 
        db table.'''
        return Response({
                        'id' : pk,
                        'first_name' : 'Teddy', 
                        'last_name' : 'Cool', 
                        'method' : 'DELETE'
                        })