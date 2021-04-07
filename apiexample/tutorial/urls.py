from django.urls import path
from tutorial import views

urlpatterns = [
    path('api/tutorial', views.tutorial_list),
    path('api/tutorial/<int:pk>', views.tutorial_detail),
    path('api/tutorial/published',views.tutorial_list_published)
]
