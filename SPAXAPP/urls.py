from django.urls import path  # type: ignore
from . import views  # Import views from the current app
from .views import user_login

# Define all URL patterns
urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('home/', views.home, name='home'),  # Home alternative route
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('project/', views.project, name='project'),  # Project page
    path('service/', views.service, name='service'),  # Service page
    path('team/', views.team, name='team'),  # Team page
    path('testimonial/', views.testimonial, name='testimonial'), # Testimonials page
    path('loginn/', views.loginn, name='loginn'),  # Team page
    path('register1/', views.register1, name='register1'),
    path('forget/', views.forget, name='forget'), # Testimonials page
    path('index1/', views.index1, name='index1'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/add/', views.add_product, name='add_product'),
    path('stores/', views.store_list, name='store_list'),
    path('stores/add/', views.add_store, name='add_store'),
    path('stores/<int:store_id>/', views.store_detail, name='store_detail'),
    path('services/', views.service_list, name='service_list'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order_items/', views.order_item_list, name='order_item_list'),
    path('order_items/<int:order_item_id>/', views.order_item_detail, name='order_item_detail'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('inventories/', views.inventory_list, name='inventory_list'),
    path('inventories/<int:inventory_id>/', views.inventory_detail, name='inventory_detail'),
    path('purchases/', views.purchase_list, name='purchase_list'),
    path('purchases/<int:purchase_id>/', views.purchase_detail, name='purchase_detail'),
    path('sales_invoices/', views.sales_invoice_list, name='sales_invoice_list'),
    path('sales_invoices/<int:invoice_id>/', views.sales_invoice_detail, name='sales_invoice_detail'),
    path('register/', views.register, name='register'),
    path('charts/', views.chartjs, name='chartjs'),
    path('overview/', views.overview, name='overview'),
    path('expired_products/', views.expired_product_list, name='expired_product_list'),
    path('expired_products/<int:expired_product_id>/', views.expired_product_detail, name='expired_product_detail'),
    path('login/', user_login, name='login'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/add/', views.add_product, name='add_product'),
    path('shop', views.shop, name='shop'),
    path('shop-detail', views.shop_detail, name='shop-detail'),
    path('stores/<int:store_id>/', views.store_detail, name='store_detail'),
    path('services/', views.service_list, name='service_list'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('my-account/', views.my_account, name='my-account'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact-us/', views.contact, name='contact-us'),
]
handler404 = 'SPAXAPP.views.page_not_found'
handler404 = 'SPAXAPP.views.custom_404'