from django.urls import path
from .views import ChangeLogListView, ChangeLogDetailView, ChangeLogCreateView, ChangeLogUpdateView, ChangeLogDeleteView
from . import views

urlpatterns = [
    path('changelog/', ChangeLogListView.as_view(), name='changelog'),
    path('changelog/<int:pk>/', ChangeLogDetailView.as_view(), name='changelog-detail'),
    path('changelog/new/', ChangeLogCreateView.as_view(), name='changelog-create'),
    path('changelog/<int:pk>/update/', ChangeLogUpdateView.as_view(), name='changelog-update'),
    path('changelog/<int:pk>/delete/', ChangeLogDeleteView.as_view(), name='changelog-delete'),
]
