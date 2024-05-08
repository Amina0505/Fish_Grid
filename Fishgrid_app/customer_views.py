from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from Fishgrid_app.models import shopRegistration, Product, Categ, Cart, Checkout_details, Compalaint, Feedback, \
    Customer_Reg


class IndexView(TemplateView):
    template_name = 'customer/shop_view.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)

        view_shop = shopRegistration.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['view_shop'] = view_shop
        return context






class Viewproducts(TemplateView):
    template_name = 'customer/products_view.html'
    def get_context_data(self, **kwargs):
        id =self.request.GET['id']

        context = super(Viewproducts, self).get_context_data(**kwargs)
        category = Categ.objects.all()
        context['category'] = category

        shop = shopRegistration.objects.get(user_id=id)

        view_prodt = Product.objects.filter(user_id=shop.id)

        context['view_prodt'] = view_prodt
        context['userid']=id
        context['shop_id']=shop.id

        return context


class Singleproducts(TemplateView):
    template_name = 'customer/singleproduct_view.html'

    def get_context_data(self, **kwargs):
        id =self.request.GET['id']

        context = super(Singleproducts, self).get_context_data(**kwargs)

        single_view = Product.objects.get(id=id)
        shop = Product.objects.get(id=id)

        feedback=Feedback.objects.all()

        context['single_view'] = single_view
        context['shop_id']=shop.user_id

        context['feedback'] = feedback
        return context

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id)

        id2=request.POST['product_id']
        shop=Product.objects.get(id=id2)


        print(id2,'hggvjkjkj')
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        fe = Feedback()
        fe.user = user
        fe.shop_id=shop.user_id
        fe.product_id=id2

        fe.name = name
        fe.email = email
        fe.subject = subject
        fe.message = message
        fe.save()
        return redirect(request.META['HTTP_REFERER'], {'message': "product successfully added "})


class Product_categ(TemplateView):
    template_name = 'customer/product_categ.html'



    def get_context_data(self, **kwargs):

        id =self.request.GET['id']
        cat_id=self.request.GET['catg_id']
        context = super(Product_categ, self).get_context_data(**kwargs)

        shop = shopRegistration.objects.get(user_id=id)

        fish_view = Product.objects.filter(user_id=shop.id,catg_id=cat_id)
        shop = shopRegistration.objects.get(user_id=id)

        view_prodt = Product.objects.filter(user_id=shop.id)
        context['view_prodt'] = view_prodt
        context['fish_view'] = fish_view
        return context



class Cart_singleview(TemplateView):
    template_name = 'customer/singleproduct_view.html'

    def dispatch(self, request, *args, **kwargs):
        pid = request.POST['id']
        qunty =request.POST['quantity']
        shop = Product.objects.get(pk=pid)
        price=shop.price
        Total= int(qunty)*int(price)
        shop.stock = int(shop.stock) - int(qunty)
        shop.save()
        shop_reg = shopRegistration.objects.get(id=shop.user_id)
        ca = Cart()
        ca.user = User.objects.get(id=self.request.user.id)
        ca.shop_id = shop_reg.id
        ca.product = Product.objects.get(pk=pid)
        ca.payment = 'null'
        ca.quantity=qunty
        ca.status = 'cart'
        ca.delivery = 'null'
        ca.total=Total
        ca.save()
        return redirect(request.META['HTTP_REFERER'])

# class Cart_buynow(TemplateView):
#     template_name = 'customer/singleproduct_view.html'
#
#     def dispatch(self, request, *args, **kwargs):
#         pid = request.GET['id']
#
#         ca = Cart()
#         shop = Product.objects.get(pk=pid)
#         shop_reg = shopRegistration.objects.get(id=shop.user_id)
#         ca.user = User.objects.get(id=self.request.user.id)
#         ca.shop_id = shop_reg.id
#         ca.product = Product.objects.get(pk=pid)
#         ca.payment = 'null'
#         ca.status = 'cart'
#         ca.delivery = 'null'
#         ca.save()
#         return render(request,'customer/checkout1.html')

class Cart_buynow(TemplateView):
    template_name = 'customer/singleproduct_view.html'

    def dispatch(self, request, *args, **kwargs):
        pid = request.GET['id']
        product = Product.objects.get(pk=pid)
        try:

            if Cart.objects.filter(product_id=product.id, user_id=self.request.user.id, status='buy'):
                return render(request, 'customer/checkout1.html', {'message': "already added"})

            else:

                ca = Cart()
                shop = Product.objects.get(pk=pid)
                shop_reg = shopRegistration.objects.get(id=shop.user_id)
                price = shop.price
                quantity = 1
                Total = quantity * int(price)
                shop.stock = int(shop.stock) - int(quantity)
                shop.save()
                ca.user = User.objects.get(id=self.request.user.id)
                ca.shop_id = shop_reg.id
                ca.product = Product.objects.get(pk=pid)
                ca.payment = 'null'
                ca.status = 'buy'
                ca.total=Total
                ca.quantity=quantity
                ca.delivery = 'null'
                ca.save()
                ctlr = Cart.objects.filter(status='buy')

                return render(request, 'customer/checkout1.html', {'message': "", 'ctlr': ctlr})
        except:

            ca = Cart()
            shop = Product.objects.get(pk=pid)
            shop_reg = shopRegistration.objects.get(id=shop.user_id)
            price = shop.price
            quantity = 1
            Total = quantity * int(price)
            shop.stock = int(shop.stock) - int(quantity)
            shop.save()
            ca.user = User.objects.get(id=self.request.user.id)
            ca.shop_id = shop_reg.id
            ca.product = Product.objects.get(pk=pid)
            ca.payment = 'null'
            ca.status = 'buy'
            ca.delivery = 'null'
            ca.total=Total
            ca.quantity=quantity
            ca.save()
            ctlr = Cart.objects.filter(status='buy')

            return render(request, 'customer/checkout1.html', {'message': "", 'ctlr': ctlr})

class ViewCart(TemplateView):
    template_name = 'customer/cart1.html'

    def get_context_data(self, **kwargs):
        context = super(ViewCart, self).get_context_data(**kwargs)
        # user = User.objects.get(id=self.request.user.id)
        id =self.request.GET['id']

        cr = self.request.user.id

        ct = Cart.objects.filter(status='cart', user_id=cr, delivery='null',shop_id=id)

        total = 0
        for i in ct:
            total = total + int(i.total)

        context['ct'] = ct
        context['asz'] = total

        return context

class RejectcartView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        cart = Cart.objects.get(id=id)
        cart.status = 'remove'
        cart.save()
        return redirect(request.META['HTTP_REFERER'])


class chpayment(TemplateView):
    def dispatch(self,request,*args,**kwargs):

        pid = self.request.user.id

        ch = Cart.objects.filter(user_id=pid,status='cart')


        print(ch)
        for i in ch:
            i.payment='paid'
            i.status='paid'
            i.delivery = 'paid'
            i.billstatus = "null"
            i.save()
        return render(request,'customer/customer_index.html',{'message': "payment successfull"})

class checkout(TemplateView):
    template_name = 'customer/checkout.html'
    def get_context_data(self, **kwargs):

         context = super(checkout,self).get_context_data(**kwargs)
         # user = User.objects.get(id=self.request.user.id)

         cr = self.request.user.id
         view_cust = Customer_Reg.objects.get(user_id=cr)

         ctr = Cart.objects.filter(status='cart',user_id=cr,delivery='null')

         total=0
         for i in ctr:
          total = total + int(i.total)
         print(total)
         context['view_cust'] = view_cust

         context['ctr'] = ctr
         context['asz'] = total
         return context

    def post(self, request, *args, **kwargs):
        firstname= request.POST['firstname']
        # lastname=request.POST['lastname']
        phonenumber=request.POST['phonenumber']
        email=request.POST['email']
        address=request.POST['address']

        chk = Checkout_details()
        chk.firstname=firstname
        # chk.lastname=lastname
        chk.phonenumber=phonenumber
        chk.email=email
        chk.address=address
        chk.save()
        return render(request, 'customer/payment.html', {'message': ""})



class BookingView(TemplateView):
    template_name = 'customer/booking.html'
    def get_context_data(self, **kwargs):
        context = super(BookingView,self).get_context_data(**kwargs)
        usid=self.request.user.id
        b = Cart.objects.filter(status='paid',user_id=usid,delivery='delivered')

        context['booking'] = b
        return context

class My_Profile(TemplateView):
    template_name = 'customer/my_profile.html'

    def get_context_data(self, **kwargs):
        context = super(My_Profile, self).get_context_data(**kwargs)
        usid = self.request.user.id

        view_cust = Customer_Reg.objects.get( user_id=usid)
        print(view_cust)

        context['view_cust'] = view_cust
        return context
    def post(self, request,*args,**kwargs):
        # fullname = request.POST['name']
        # last = request.POST['name1']


        if request.POST['profile'] == "pass":
         id = request.POST['id']
         password = request.POST['password']
         us = User.objects.get(pk=id)

         us.set_password(password)

         us.save()
        else:
         address = request.POST['address']
         id = request.POST['id']
         email = request.POST['email']
         name=request.POST['name']
         reg = Customer_Reg.objects.get(user=id)

         reg.address = address
         reg.save()
         us = User.objects.get(pk=id)
         us.username=email
         us.email = email
         us.first_name=name
         us.save()

        messages = "Update Successful."
        return render(request, 'customer/my_profile.html', {'messages': messages})





class Add_complaint(TemplateView):
    template_name = 'customer/add_complaint.html'

    def post(self, request, *args, **kwargs):
        user=User.objects.get(id=self.request.user.id)
        name= request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        com = Compalaint()
        com.user=user
        com.name=name
        com.email=email
        com.subject=subject
        com.message=message
        com.status = 'added'
        com.save()
        return render(request, 'customer/customer_index.html', {'message': "complaint added"})

class Complaint_replay(TemplateView):
    template_name = 'customer/complaint_replayview.html'

    def get_context_data(self, **kwargs):
        context = super(Complaint_replay,self).get_context_data(**kwargs)

        replay = Compalaint.objects.filter(status='replied')

        context['replay'] = replay
        return context


class Direct_checkout(TemplateView):
    template_name = 'customer/checkout1.html'


    def post(self, request, *args, **kwargs):
        firstname = request.POST['firstname']
        # lastname = request.POST['lastname']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        address = request.POST['address']

        chk = Checkout_details()
        chk.firstname = firstname
        chk.phonenumber = phonenumber
        chk.email = email
        chk.address = address
        chk.save()
        return render(request, 'customer/payment2.html', {'message': ""})

class Direct_payment(TemplateView):
    def dispatch(self,request,*args,**kwargs):

        pid = self.request.user.id

        ch = Cart.objects.filter(user_id=pid,status='buy')


        print(ch)
        for i in ch:
            i.payment='paid'
            i.status='paid'
            i.delivery = 'delivered'
            i.billstatus = "null"
            i.save()
        return render(request,'customer/payment2.html',{'message':" payment Successfull"})




