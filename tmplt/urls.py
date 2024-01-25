from django.urls import path
from . import views
from django.conf.urls import handler404
from tmplt.views import Template404
handler404 = Template404
urlpatterns = [
    path("", views.Index.as_view(),name="index"),
    
    path("about", views.AboutViews.as_view(),name="about"),
    path("cart", views.CartViews.as_view(),name="cart"),
    path("category", views.CategoryViews.as_view(),name="category"),
    path("checkout", views.CheckoutViews.as_view(),name="checkout"),
    path("collection", views.CollectionViews.as_view(),name="collection"),
    path("contact", views.ContactViews.as_view(),name="contact"),
    path("dashboard", views.DashboardViews.as_view(),name="dashboard"),
    path("faq", views.FaqViews.as_view(),name="faq"),
    path("login", views.LoginViews.as_view(),name="login"),
    path("product/<slug:slug>/", views.SingleProductViews.as_view(),name="product_single"),
    path("profile", views.ProfileViews.as_view(),name="profile"),
    path("register", views.RegisterViews.as_view(),name="register"),
    path("review", views.ReviewViews.as_view(),name="review"),
    path("wishlist", views.WishlistViews.as_view(),name="wishlist"),
    path("search", views.SearchViews.as_view(),name="search"),
    #path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add-to-cart'),


    path('api/cart/', views.cart_api, name='cart_api'),
    
    
]