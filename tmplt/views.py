
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.db.models import Prefetch
from django.contrib import messages  # Import the messages module
#from blurb.models import Category, Image, Market, Prices, Products, Reviews,SubCategory, SubsubCategory
from rest_framework.decorators import api_view
from rest_framework.response import Response
import openai
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404, redirect
#from .forms import SearchForm
from django.views import View
from django.http import HttpResponse
import json

from category.models import Category
from orders.models import Order, OrderedProduct
from products.models import Product, ProductReviews
from django.contrib.auth.models import User, auth

from wishcart.models import Cart

# Create your views here.
class Index(TemplateView):
    template_name = "tmplt/furniture.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.all()
        # context['markets'] = Market.objects.all()
        # print(context,"hello")
        
        # # try:
        # #     search_category = Keyword.objects.filter(user = self.request.user).last()
        # #     context['recomends'] = Item.objects.filter(category__name=search_category.keyword,status='Free')
        # # except:
        # #     return context
        # products_by_market = {}
        # for market in context['markets']:
        #     products = Products.objects.filter(market=market).prefetch_related(
        #         Prefetch('product_image', queryset=Image.objects.all()),
        #         Prefetch('prices', queryset=Prices.objects.all()),
        #         Prefetch('reviews', queryset=Reviews.objects.all())
        #     )
        #     products_by_market[market.name] = products

        # context['products_by_market'] = products_by_market
        # print(context,"hiii")
        return context
def Template404(request, exception):
    return render(request, '404.html', status=404)
class AboutViews(TemplateView):
    template_name = "tmplt/about-page.html"
class CartViews(TemplateView):
    template_name = "tmplt/cart.html"
class CategoryViews(TemplateView):
    template_name = "tmplt/category-page(6-grid).html"
class CheckoutViews(TemplateView):
    template_name = "tmplt/checkout.html"
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            # Extract form data from the request
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            address = request.POST.get("address")
            phone_number = request.POST.get("phone")
            # Extract other form fields similarly
            
            # Assuming ordered_product_ids is a list of IDs of OrderedProduct instances
            ordered_product_ids = request.POST.getlist("ordered_product_ids")
            ordered_products = OrderedProduct.objects.filter(id__in=ordered_product_ids)
            
            # Calculate the total amount based on ordered products
            total_amount = sum(product.product.price * product.quantity for product in ordered_products)
            
            # Create the order
            order = Order.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                address=address,
                phone_number=phone_number,
                amount=total_amount
            )
            
            # Add ordered products to the order
            order.ordered_product.set(ordered_products)
            
            # Redirect or render a success page
            return redirect('index')
        
        # If not a POST request, render the checkout page
        return super().get(request, *args, **kwargs)
class CollectionViews(TemplateView):
    template_name = "tmplt/collection.html"
class ContactViews(TemplateView):
    template_name = "tmplt/contact.html"
class DashboardViews(TemplateView):
    template_name = "tmplt/dashboard.html"
class FaqViews(TemplateView):
    template_name = "tmplt/faq.html"
class LoginViews(TemplateView):
    template_name = "tmplt/login.html"
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        print(username.split("@")[0])
        print(password)
        user = auth.authenticate(username=username.split("@")[0],password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return redirect('login')
class SingleProductViews(TemplateView):
    template_name = "tmplt/product-page(no-sidebar).html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs.get('slug')
        context['product'] = get_object_or_404(Product, slug=slug)
        context['categories'] = Category.objects.all()
        return context
    def post(self, request, *args, **kwargs):
        # Assuming you have imported ProductReviews and User models
        user = self.request.user
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        text = request.POST.get('text')
        title = request.POST.get('title')

        # Check if a review for this product by the user already exists
        existing_review = ProductReviews.objects.filter(user=user, product=product).first()

        if existing_review:
            # Update existing review
            existing_review.title = title
            existing_review.text = text
            existing_review.save()
        else:
            # Create a new review
            new_review = ProductReviews.objects.create(user=user, product=product, title=title, text=text)

        return redirect('product_single', slug=product.slug)
class ProfileViews(TemplateView):
    template_name = "tmplt/profile.html"
class RegisterViews(TemplateView):
    template_name = "tmplt/register.html"
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        name= request.POST['name']
        username = request.POST['username']
        print(username)
        print(password)
        try:
            user = User.objects.get(username=username)
        except:
            user= None
        print(user)
        if user is None:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=name
            )
            
            return redirect('login')
        else:
             return redirect('signup')
class ReviewViews(TemplateView):
    template_name = "tmplt/review.html"
class WishlistViews(TemplateView):
    template_name = "tmplt/wishlist.html"
class SearchViews(TemplateView):
    template_name = "tmplt/search.html"
class ShopListView(TemplateView):
    template_name = 'tmplt/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()  # Retrieve all products
        return context
# class Index(TemplateView):
#     template_name = "tmplt/furniture.html"
    


# myapp/views.py
# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from wishcart.models import Cart
from .serializers import CartSerializer, CartSerializer1
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET', 'POST'])
def cart_api(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        user = request.user  # Assuming the user is authenticated
        product_id = request.data.get('product')  # Assuming product ID is sent in request data
        existing_cart = Cart.objects.filter(user=user, product=product_id).first()
        if existing_cart:
            # If the same user and product already exist in the cart, update the quantity
            existing_cart.quantity += int(request.data.get('quantity', 1))
            existing_cart.save()
            serializer = CartSerializer1(existing_cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # If not, create a new cart entry
            serializer = CartSerializer1(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

