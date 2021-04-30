from rest_framework import serializers

from profiles_api_app import models 

class HelloSerializer(serializers.Serializer):
    '''Serializes a name filed for testing APIView'''
    name = serializers.CharField(max_length=10)


class UserProfilerSerializer(serializers.ModelSerializer):
    '''Serializes a user profile object'''
    class Meta:
        model = models.UserProfile
        fields = ['id','email','name', 'password']
        extra_kwargs = {
                        'password': {
                            'write_only':True,
                            'style' : {'input_type' : 'password'}
                                    }    
                        }
    
    def create(self, validated_data):
        '''Create and return a new user'''
