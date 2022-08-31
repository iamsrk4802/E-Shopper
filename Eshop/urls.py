from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from mainApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('cart/',views.cartDetails),
    path('checkout/',views.checkoutDetails),
    path('contact/',views.contactDetails),
    path('login/',views.loginDetails),
    path('product/<int:num>/',views.productDetails),
    path('shop/<str:cat>/<str:br>/',views.shopDetails),
    path('signup/',views.signupUser),
    path('profile/',views.profile),
    path('logout/',views.logout),
    path('addproduct/',views.addProduct),
    path('deleteproduct/<int:num>/',views.deleteProduct),
    path('editproduct/<int:num>/',views.editProduct),
    path('deletecart/<int:num>/',views.deleteCart),
    path('confirm/',views.confirm),
    path('wishlist/<int:num>/',views.wishlistDetails),
    path('wishlist/',views.wishlistBuyer),
    path('deletewishlist/<int:num>/',views.wishlistDelete),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
