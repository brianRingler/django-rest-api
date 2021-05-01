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
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def updated(self, instance, validated_data):
        '''Handle updating user account'''
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
            
        return super().update(instance, validated_data)



class ProfileFeedItemSerializer(serializers.ModelSerializer):
    '''Serializers profile feed items'''

    class Meta:
        model = models.ProfileFeedItem
        # id & created_on are auto set so by default they are read only
        fields = ['id', 'user_profile', 'status_text', 'created_on']

        # user_profile and status text are not read only - With the profile 
        extra_kwargs = {'user_profile': {'read_only':True}}

