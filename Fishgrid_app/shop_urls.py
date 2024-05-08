from django.urls import path
from Fishgrid_app.shop_views import IndexView, Addproduct, Add_category, Shop_productview, Delete_product, \
    Feedback_view, View_booking

urlpatterns = [

    path('',IndexView.as_view()),
    path('addcateg',Add_category.as_view()),
    path('addproduct',Addproduct.as_view()),
    path('view_product',Shop_productview.as_view()),
        path('delete',Delete_product.as_view()),
    path('view_feedback',Feedback_view.as_view()),
    path('view_booking',View_booking.as_view())


]
def urls():
    return urlpatterns, 'shop','shop'




