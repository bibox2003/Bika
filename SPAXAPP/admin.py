from django.contrib import admin # type: ignore
from .models import (
    UserProfile,
    Product,
    Service,
    Order,
    Store,
    Customer,
    Inventory,
    Purchase,
    SalesInvoice,
    ExpiredProduct,
    OrderItem,
    
)

# Register models in the admin site
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)
admin.site.register(Store)
admin.site.register(Inventory)
admin.site.register(Purchase)
admin.site.register(SalesInvoice)
admin.site.register(ExpiredProduct)

