from django.urls import path
from .views import advert, place_ads, view_ad

urlpatterns = [
    path('adverts/', advert, name="advert"),
    path('adverts/place/', place_ads, name="place_advert"),
    path('adverts/<int:id>/', view_ad, name="view_ad"),
]