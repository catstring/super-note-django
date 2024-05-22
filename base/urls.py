from django.urls import path
from .views import first_page
from base.views import greeting


urlpatterns = [
    path('', first_page, name='first_page'),
    path('greeting/', greeting, name='greeting'),
]
