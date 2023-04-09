from django.urls import path
from .views import IndexList, PostDetail, PostNew, PostUpdate, PostDelete

urlpatterns = [
    path('',IndexList.as_view(), name='list'),
    path('<int:pk>',PostDetail.as_view(), name='detail'),
    path('new/',PostNew.as_view(), name='create'),
    path('<int:pk>/update',PostUpdate.as_view(), name='update'),
    path('<int:pk>/delete',PostDelete.as_view(), name='delete'),
]
