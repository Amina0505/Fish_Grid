from django.urls import path

from Fishgrid_app.admin_views import IndexView, ApproveView, Shop_Approvel, Customer_approvel, Shop_View, Customer_View, \
    Complaint_View, BookingView

urlpatterns = [

    path('',IndexView.as_view()),
    path('shop_approve',Shop_Approvel.as_view()),
    path('cus_approve',Customer_approvel.as_view()),
    path('approve', ApproveView.as_view()),
    path('view_shop',Shop_View.as_view()),
    path('view_cust',Customer_View.as_view()),
    path('compl',Complaint_View.as_view()),
    path('booking',BookingView.as_view())


]
def urls():
    return urlpatterns, 'admin','admin'