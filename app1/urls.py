from django.contrib import admin
from django.urls import path
from .views import PersonCreateView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'persons',PersonCreateView , basename='user')
urlpatterns = router.urls
# urlpatterns = [
#     path('persons/', PersonCreateView)
# ]