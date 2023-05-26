from django.urls import path

from .views import AboutPageView
from .views import HomePageView
from .views import ContactPageView

urlpatterns = [
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]
