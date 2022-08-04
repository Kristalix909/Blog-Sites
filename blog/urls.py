from django.urls import path
from .views import PostList, logoutUser, post_detail,registration, loginUser

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>', post_detail, name='post_detail'),
    path('register/', registration, name='registration'),
    path('logout/', logoutUser, name='logout'),
    path('login/', loginUser, name="login")
]