from django.urls import path


from Fishgrid_app.customer_views import IndexView, Viewproducts, Singleproducts, Cart, Product_categ, \
    ViewCart, RejectcartView, checkout, chpayment, BookingView, Add_complaint, Complaint_replay, Cart_singleview, \
    Cart_buynow, Direct_checkout, Direct_payment, My_Profile

urlpatterns = [

    path('',IndexView.as_view()),
    path('products',Viewproducts.as_view()),
    path('single_view',Singleproducts.as_view()),
    path('categ_view',Product_categ.as_view()),

    path('cart',Cart_singleview.as_view()),
    path('cart2',Cart_buynow.as_view()),
    # path('cart2',Cart_buynow.as_view()),
    path('viewCart',ViewCart.as_view()),
    path('removecart',RejectcartView.as_view()),
    path('chpy',chpayment.as_view()),
    path('checkout',checkout.as_view()),
    path('directcheckout',Direct_checkout.as_view()),
    path('booking',BookingView.as_view()),
    path('complaint',Add_complaint.as_view()),
    path('replay',Complaint_replay.as_view()),
    path('direct_checkout',Direct_checkout.as_view()),
    path('d_payment',Direct_payment.as_view()),
    path('my_profile',My_Profile.as_view())




]
def urls():
    return urlpatterns, 'customer', 'customer'