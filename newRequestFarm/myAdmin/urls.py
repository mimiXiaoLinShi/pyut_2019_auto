# coding:utf8
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from myAdmin import views, views2

urlpatterns = [

    # url(r'^index$', views.index),
    # url(r'^indexbook/(P<city>[a-z]/(?P<year>\D{4})$', views.indexBook),
    # url(r'^indexinfo/(\d+)/$', views.HeroInfo.as_view()),
    # url(r'^delete/(\d+)/$', views.delete),
    # url(r'^create/$', views.create),
    # url(r'^show_reqarg/$', views.show_reqarg),
    # url(r'^pic_upload/$',views.pic_upload),
    # url(r'^pic_handle/$', views.pic_handle),
    ##########################################页面新做#############################
    # url(r'^', views.get_index),
    url('^index/$', views.get_index),
    url(r'^books1/$', views2.BookListAPIView.as_view()),
    url(r'^case/$', views.caseList.as_view())
]

router = DefaultRouter()
router.register(r'books2', views2.BookInfoViewSet)

urlpatterns += router.urls