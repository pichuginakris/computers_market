from django.urls import path
from .views import MainCategoryView, SubCategoryView, ProductView, MainCategoryView_v2,  ProductView_v2, SubCategoryView_v2

app_name = "models"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('main_category/<int:pk>', MainCategoryView_v2.as_view()),
    path('main_category/', MainCategoryView.as_view()),
    path('sub_category/<int:pk>', SubCategoryView_v2.as_view()),
    path('sub_category/', SubCategoryView.as_view()),
    path('product_category/', ProductView.as_view()),
    path('product_category/<int:pk>', ProductView_v2.as_view()),
]