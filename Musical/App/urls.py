from rest_framework.routers import DefaultRouter
from App import views
from django.urls import path,include
router = DefaultRouter()
router.register('showdata',views.ShowDataAPI)
router.register('music',views.MusicAPI)

urlpatterns = [
    path('',include(router.urls)),
]