from django.urls import path
from .views import PostList, post_detail,registration

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>', post_detail, name='post_detail'),
    path('register/', registration, name='registration')
]