from django.urls import path
from .views import HomePageView, Billioneries

urlpatterns = [
    path('', HomePageView, name='home'),
    path('Billioneries/', Billioneries.as_view(), name="good"),
]