from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [

]

router = DefaultRouter()
router.register('books', views.BookInfoViewSet)
urlpatterns += router.urls