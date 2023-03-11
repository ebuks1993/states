from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('state',views.StateViewset,basename='state')

urlpatterns = [
    path('',include(router.urls))
]
