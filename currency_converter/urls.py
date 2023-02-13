from django.urls import path

from .views import CurencyView

urlpatterns = [
    path("", CurencyView.as_view(), name="index"),
]
