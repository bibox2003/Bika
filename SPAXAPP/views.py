from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Product
from .forms import ProductForm

def index(request):
    return render(request, 'bika/index.html')

def about(request):
    return render(request, 'bika/about.html')

def shop(request):
    return render(request, 'bika/shop.html')

def cart(request):
    return render(request, 'bika/cart.html')

def checkout(request):
    return render(request, 'bika/checkout.html')

def project(request):
    return render(request, 'bika/project.html')

def service(request):
    return render(request, 'bika/service.html')

def team(request):
    return render(request, 'bika/team.html')

def testimonial(request):
    return render(request, 'bika/testimonial.html')

def forget(request):
    return render(request, 'bika/forget.html')


def register1(request):
    return render(request, 'BSS/src/register1.html')

def contact(request):
    return render(request, 'bika/contact-us.html')

def gallery(request):
    return render(request, 'bika/gallery.html')

def my_account(request):
    return render(request, 'bika/my-account.html')

def shop_detail(request):
    return render(request, 'bika/shop-detail.html')

def wishlist(request):
    return render(request, 'bika/wishlist.html')

def loginn(request):
    return render(request, 'bika/loginn.html')

def register(request):
    return render(request, 'bika/register.html')

def index1(request):
    return render(request, 'BSS/src/index1.html',)

def register(request):
    return render(request, 'BSS/src/register.html')

def chartjs(request):
    return render(request, 'BSS/src/chartjs.html')


def home(request):
    return render(request, 'home.html')

def chartjs(request):
    return render(request, 'hello.html')


def chartjs(request):
    return render(request, 'BSS/src/chartjs.html')

def overview(request):
    return render(request, 'BSS/src/overview.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'BSS/src/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'BSS/src/add_product.html', {'form': form})

def hello(request):
    return render(request, 'BSS/src/index1.html')

def profile_view(request):
    return render(request, 'profile.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})

def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'service_detail.html', {'service': service})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'BSS/src/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'BSS/src/order_detail.html', {'order': order})

def order_item_list(request):
    order_items = OrderItem.objects.all()
    return render(request, 'BSS/src/order_item_list.html', {'order_items': order_items})

def order_item_detail(request, order_item_id):
    order_item = get_object_or_404(OrderItem, pk=order_item_id)
    return render(request, 'BSS/src/order_item_detail.html', {'order_item': order_item})

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'BSS/src/store_list.html', {'stores': stores})

def add_store(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store_list')
    else:
        form = StoreForm()
    return render(request, 'BSS/src/add_store.html', {'form': form})

def store_detail(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    return render(request, 'store_detail.html', {'store': store})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'BSS/src/customer_list.html', {'customers': customers})

def customer_detail(request, name):
    customer = get_object_or_404(Customer, pk=name)
    return render(request, 'customer_detail.html', {'customer': customer})

def inventory_list(request):
    inventories = Inventory.objects.all()
    return render(request, 'BSS/src/inventory_list.html', {'inventories': inventories})

def inventory_detail(request, inventory_id):
    inventory = get_object_or_404(Inventory, pk=inventory_id)
    return render(request, 'inventory_detail.html', {'inventory': inventory})

def purchase_list(request):
    purchases = Purchase.objects.all()
    return render(request, 'BSS/src/purchase_list.html', {'purchases': purchases})

def purchase_detail(request, purchase_id):
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    return render(request, 'purchase_detail.html', {'purchase': purchase})

def sales_invoice_list(request):
    sales_invoices = sales_invoices.objects.all()
    return render(request, 'BSS/src/sales_invoice_list.html', {'sales_invoices': sales_invoices})

def sales_invoice_detail(request, invoice_id):
    sales_invoice = get_object_or_404(sales_invoice, pk=invoice_id)
    return render(request, 'sales_invoice_detail.html', {'sales_invoice': sales_invoice})

def expired_product_list(request):
    expired_products = ExpiredProduct.objects.all()
    return render(request, 'BSS/src/expired_product_list.html', {'expired_products': expired_products})

def expired_product_detail(request, expired_product_id):
    expired_product = get_object_or_404(ExpiredProduct, pk=expired_product_id)
    return render(request, 'expired_product_detail.html', {'expired_product': expired_product})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email from form
        password = request.POST.get('password')  # Get password from form
        
        # Authenticate user using email and password
        user = authenticate(request, username=email, password=password)
        
        if user is not None:  # Valid user
            login(request, user)  # Log in the user
            messages.success(request, "Login successful!")
            return redirect('index')  # Redirect to a dashboard or home page
        else:  # Invalid credentials
            messages.error(request, "Invalid email or password")
    
    return render(request, 'login.html')  # Re-render the login page
