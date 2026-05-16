from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token # <- The critical import line!
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    # Secure token endpoint
    path('api-token-auth/', obtain_auth_token),
]