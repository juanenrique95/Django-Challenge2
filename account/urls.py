from django.urls import path, include

from . import views
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()

router.register(r'account', views.AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('fizz-buzz/', views.fizz_buzz, name='fizz_buzz')                    
]

