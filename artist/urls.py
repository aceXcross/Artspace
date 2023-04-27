from django.urls import path
from .views import index, portfolio, brushes, reviews

urlpatterns = [
    path('', index, name='index'),
    path('portfolio/', portfolio, name='portfolio'),
    path('brushes/', brushes, name='brushes'),
    path('reviews/', reviews, name='reviews')
]