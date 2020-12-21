from django.urls import path
from .views import MainCategoryView, SubCategoryView, ProductView

app_name = "models"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('main_category/(?P<pk>[0-9]+)$', MainCategoryView.as_view()),
    path('sub_category/(?P<pk>[0-9]+)$', SubCategoryView.as_view()),
    path('product_category/<int:pk>', ProductView.as_view()),
    path('main_category/', MainCategoryView.as_view()),
    path('sub_category/', SubCategoryView.as_view()),
    path('product_category/', ProductView.as_view()),
]