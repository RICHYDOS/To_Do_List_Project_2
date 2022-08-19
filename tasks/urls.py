from django.urls import path
from .views import *

urlpatterns = [
    path("<int:pk>", UserItemView.as_view(), name = "task"),
    path("item/<int:pk>", ItemDetailView.as_view(), name = "item_detail"),
    path("item/<int:pk>/delete", ItemDeleteView.as_view(), name = "item_delete"),
    path("item/<int:pk>/edit", ItemUpdateView.as_view(), name = "item_update"),
    path("item/new", ItemCreateView.as_view(), name = "item_new"),
    path("", DoneView.as_view(), name="done"),
]