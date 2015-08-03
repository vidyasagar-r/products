from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+/$)', views.user, name='user'),
    url(r'^(?P<user_id>[0-9]+/category/$)', views.category, name='category'),
    url(r'^product/$', views.product, name='product'),
    url(r'^category/(?P<user_id>[0-9]+)/$', views.category, name='category'),
    url(r'^categories/$', views.category, name='category'),
    url(r'^adduser/$', views.adduser, name='adduser'),
    url(r'^addproduct/$', views.addproduct, name='addproduct'),
    url(r'^editproduct/(?P<product_id>[0-9]+)/$', views.editproduct, name='editproduct'),
    url(r'^editcategory/(?P<category_id>[0-9]+)/$', views.editcategory, name='editcategory'),
    url(r'^addProduct/(?P<user_id>[0-9]+)/$', views.addProduct, name='addProduct'),
    url(r'^addCategory/(?P<user_id>[0-9]+)/$', views.addCategory, name='addCategory'),
    url(r'^addcategory/$', views.addcategory, name='addcategory'),
    url(r'^edituser/(?P<user_id>[0-9]+)/$', views.edituser, name='edituser'),
    url(r'^edited/$', views.edited, name='edited'),
    url(r'^viewcategory/(?P<user_id>[0-9]+)/$', views.viewcategory, name='viewcategory'),
    url(r'^viewCategory/(?P<user_id>[0-9]+)/$', views.viewCategory, name='viewCategory'),
    url(r'^viewCategory/(?P<user_name>[a-zA-Z]+)/$', views.viewCategory, name='viewCategory'),
    url(r'^viewproducts/$', views.viewproducts, name='viewproducts'),
    url(r'^viewProducts/(?P<user_id>[0-9]+)/$', views.viewProducts, name='viewProducts'),
    url(r'^viewProducts/(?P<user_name>[a-zA-Z]+)/$', views.viewProducts, name='viewProducts'),
    url(r'^viewproductsByCat/(?P<user_id>[0-9]+)-(?P<category_id>[0-9]+)/$', views.viewproductsByCat,
        name='viewproductsByCat'),
    url(r'^viewproductsByCategory/(?P<category_id>[0-9]+)/$', views.viewproductsByCategory,
        name='viewproductsByCategory'),
    url(r'^addProductByCat/(?P<user_id>[0-9]+)-(?P<category_id>[0-9]+)/$', views.addProductByCat,
        name='addProductByCat'),
    url(r'^DelProductByCat/(?P<user_id>[0-9]+)-(?P<category_id>[0-9]+)/$', views.DelProductByCat,
        name='DelProductByCat'),
    url(r'^DelProductByCat/(?P<user_id>[0-9]+)-(?P<category_id>[0-9]+)/$', views.DelProductByCat,
        name='DelProductByCat'),
    url(r'^delProduct/(?P<product_id>[0-9]+)/$', views.delProduct, name='delProduct'),
    url(r'^delCategory/(?P<category_id>[0-9]+)/$', views.delCategory, name='delCategory'),
    url(r'^delUser/(?P<user_id>[0-9]+)/$', views.delUser, name='delUser'),

    ####### add to basket
    url(r'^addToBasket/(?P<product_id>[0-9]+)/$', views.addToBasket, name='addToBasket'),
    url(r'^delFromBasket/(?P<product_id>[0-9]+)/$', views.delFromBasket, name='delFromBasket'),

    ######   this url is created to display the content of extended features of 'base2.html' ######
    url(r'^display/$', views.display, name='display')
]
