from django.urls import path
from.import views

urlpatterns =[ 
    path('brand_list/',views.brandlist,name='brand_list'),
    path('add-product/',views.Addproduct.as_view(),name='add_product'),
    path('product_list/',views.productlist,name='product_list'),
    path('product-details/<int:id>/',views.product_details,name='product_details'),
    path('update-product/<int:id>/',views.update_product,name='update_product'),
    path('delete-product/<int:id>/',views.product_details,name='delete_product'),
    path('add-product-with-django-form',views.add_product_with_django_form,name='add_product_with_django_form'),
    path('add-brand',views.add_brand,name='add_brand'),
]