from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("article/", views.article, name="article"),
    path("nutritions/", views.allFood, name="nutritions"),
    path("dri-calculator/", views.calculate, name="calculate"),
    path("dri-calculator/result/", views.dri_result, name="dri_result"),

    path("profile/", views.profile, name="profile"),
    path("data_date/", views.data_date, name="data_date"),

    path("add_nutrition/", views.add_nutrition, name="add_nutrition"),
    path("add_sda/", views.add_sda, name="add_sda"),
    path("store_consumed_nutritions/", views.store_consumed_nutritions, name="store_consumed_nutritions"),
    

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