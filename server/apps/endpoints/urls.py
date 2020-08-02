from django.urls import path
from apps.endpoints import views

urlpatterns = [
               path('',views.index_page),
               path('cropArrival', views.predict_cropArrival),
               path('pricePredict', views.predict_pricePredict),
               path('psfPredict', views.predict_psfPredict),
               ]
