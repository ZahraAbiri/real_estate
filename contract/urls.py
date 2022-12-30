from django.urls import path
from . import views

urlpatterns = [
    path('buy/',views.buy ,name='buy_contract'),
    path('sell/',views.sell,name='sell_contract' ),
    path('rent/',views.rent,name='rent_contract'),
    path('mortgage/',views.mortgage,name='mortgage_contract'),
]