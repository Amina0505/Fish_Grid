from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from Fishgrid_app.models import Categ, Product, shopRegistration, Feedback, Cart


class IndexView(TemplateView):
    template_name = 'shop/shop_index.html'

class Add_category(TemplateView):
    template_name='shop/add_category.html'

    def post(self, request, *args, **kwargs):
        name=request.POST['name']
        categ=Categ()
        categ.name=name
        categ.save()
        return redirect(request.META['HTTP_REFERER'])


class Addproduct(TemplateView):
    template_name ='shop/add_product.html'

    def get_context_data(self, **kwargs):
        context = super(Addproduct, self).get_context_data(**kwargs)
        category = Categ.objects.all()
        context['category'] = category
        return context

    def post(self, request,*args,**kwargs):

        user = User.objects.get(pk=self.request.user.id)

        name = request.POST['name']
        shop = shopRegistration.objects.get(user_id=self.request.user.id)

        category = request.POST['category']
        price = request.POST['price']
        stock=request.POST['stock']
        desc = request.POST['desc']
        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)

        se = Product()

        se.user_id = shop.id
        se.name = name
        se.stock=stock
        se.shop=user
        se.image=filesss
        se.catg_id = category
        se.price = price
        se.desc = desc

        se.save()

        return redirect(request.META['HTTP_REFERER'], {'message': "product successfully added "})




class Shop_productview(TemplateView):
    template_name ='shop/view_product.html'

    def get_context_data(self, **kwargs):

        context = super(Shop_productview,self).get_context_data(**kwargs)

        view_pr = Product.objects.filter(shop_id=self.request.user.id)

        context['view_pr'] = view_pr
        return context



class Delete_product(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Product.objects.get(id=id).delete()

        return render(request,'shop/shop_index.html',{'message':"Photo Removed"})


class Feedback_view(TemplateView):
    template_name ='shop/view_feedback.html'

    def get_context_data(self, **kwargs):

        context = super(Feedback_view,self).get_context_data(**kwargs)

        view_fe = shopRegistration.objects.get(user_id=self.request.user.id)
        feed=Feedback.objects.filter(shop_id=view_fe.id)
        context['feed'] = feed
        return context




class View_booking(TemplateView):
    template_name ='shop/view_booking.html'

    def get_context_data(self, **kwargs):

        context = super(View_booking,self).get_context_data(**kwargs)

        view_book = shopRegistration.objects.get(user_id=self.request.user.id)
        feed=Cart.objects.filter(shop_id=view_book.id)
        context['feed'] = feed
        return context



