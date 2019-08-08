from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from home.views import index


urlpatterns = [
    path(r'', index, name='apiindex'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
