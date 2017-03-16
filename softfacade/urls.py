from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from core.views import BookModelViewSet, AuthorModelViewSet, LibraryModelViewSet, StatisticViewSet

router = routers.SimpleRouter()
router.register(r'books', BookModelViewSet)
router.register(r'authors', AuthorModelViewSet)

library_view = LibraryModelViewSet.as_view({'get': 'list'})
statistic_view = StatisticViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^library/', library_view),
    url(r'^statistics/', statistic_view),
]

urlpatterns += router.urls
