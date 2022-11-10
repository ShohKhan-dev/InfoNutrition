from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("article/", views.article, name="article"),
    path("nutritions/", views.allFood, name="nutritions"),
    path("dri-calculator/", views.calculate, name="calculate"),
    path("dri-calculator/result/", views.dri_result, name="dri_result"),

    path("visualization/", views.visualization, name="visualization"),
    path("visualization/basic_food/", views.basicFood, name="basic_food"),
    
    path("visualization/calories/", views.category, name="calories"),
    path("visualization/protein/", views.category, name="protein"),
    path("visualization/fat/", views.category, name="fat"),
    path("visualization/sat_fat/", views.category, name="sat_fat"),
    path("visualization/fiber/", views.category, name="fiber"),
    path("visualization/carbs/", views.category, name="carbs"),

    path('search/', views.search_results, name='search'),

    path('data_ingredient/', views.data_ingredient, name='data_ingredient'),

]