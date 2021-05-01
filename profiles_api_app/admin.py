from django.contrib import admin

# from the profiles_api_app application we need to import models
from profiles_api_app import models


admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
