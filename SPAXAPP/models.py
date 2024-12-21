from django.db import models  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.utils import timezone  # type: ignore
from django.utils.crypto import get_random_string

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    inventory_count = models.IntegerField()
    serial_no = models.CharField(max_length=100, unique=True, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    expiry_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    products = models.ManyToManyField(Product, related_name='suppliers')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order_id}"

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"OrderItem {self.order_item_id} from Order {self.order.order_id}"

class Shipment(models.Model):
    shipment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='shipments', null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    tracking_number = models.CharField(max_length=100, unique=True)
    shipped_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')],
        default='Pending'
    )

    def __str__(self):
        return f"Shipment {self.shipment_id} - {self.tracking_number}"

class Promotion(models.Model):
    promotion_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='promotions')
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.product.name} - {self.discount_percentage}% off"

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey('Service', on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.customer.username} - Rating {self.rating}"

class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message[:50]}"

class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_incurred = models.DateTimeField()
    category = models.CharField(
        max_length=50,
        choices=[
            ('Operational', 'Operational'),
            ('Maintenance', 'Maintenance'),
            ('Other', 'Other'),
        ],
        default='Other'
    )

    def __str__(self):
        return f"Expense {self.expense_id} - {self.description}"

class LoyaltyProgram(models.Model):
    program_id = models.AutoField(primary_key=True)
    customer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='loyalty_program')
    points = models.IntegerField(default=0)
    tier = models.CharField(
        max_length=50,
        choices=[
            ('Bronze', 'Bronze'),
            ('Silver', 'Silver'),
            ('Gold', 'Gold'),
            ('Platinum', 'Platinum')
        ],
        default='Bronze'
    )

    def __str__(self):
        return f"{self.customer.username} - {self.tier} Tier ({self.points} points)"

class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaints')
    description = models.TextField()
    status = models.CharField(
        max_length=50,
        choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved'), ('Closed', 'Closed')],
        default='Open'
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint {self.complaint_id} - {self.customer.username} ({self.status})"

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, related_name='stores')
    sensors = models.JSONField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"

class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase {self.purchase_id} - {self.product.name}"

class SalesInvoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    invoice_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Invoice {self.invoice_id} - {self.product.name} to {self.customer.username}"

class ExpiredProduct(models.Model):
    expired_product_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    expiry_date = models.DateTimeField()

    def __str__(self):
        return f"Expired {self.product.name} - {self.expiry_date.strftime('%Y-%m-%d')}"

class Customer(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define the auto-incrementing ID
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Automatically generate a unique Gmail address if not provided
        if not self.email:
            self.email = f"customer_{get_random_string(8)}@gmail.com"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.name}"  # Including ID in the string representation