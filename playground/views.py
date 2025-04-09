from django.shortcuts import render
from django.db.models import Q, F, Value, Func, Count, Max, Min, Avg, Sum, ExpressionWrapper, DecimalField
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order, Customer
from tags.models import TaggedItem

# Create your views here.
def say_hello(request):
    try:
        # products = Product.objects.filter(unit_price__range=(20, 30))
        # products2 = Product.objects.filter(inventory__lt=10, unit_price__lt=20) #returns queryset
        # queryset_qobjects = Product.objects.filter(Q(inventory_lt=10) | ~Q(unit_price__lt=20))
        # queryset_fobjects = Product.objects.filter(inventory=F('collection_id')) #comparing 2 fields
        # queryset_orderby = Product.objects.order_by('unit_price', '-title')
        # queryset_distinct = Product.objects.values('id') #dictionary objects
        # queryset = Product.objects.only('id', 'title') #instances of the product class
        # select_related (1) (n-->1)
        # select_prefetch_related (n) (n-->n)
        # latest_orders = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
        # result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))
        
        # queryset = Customer.objects.annotate(
        #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
        # )

        # queryset = Customer.objects.annotate(
        #     full_name=Concat('first_name', Value(' '), 'last_name')
        # )

        # discounted_price = ExpressionWrapper(
        #     F('unit_price') * Value(0.8),
        #     output_field=DecimalField()
        # )

        # queryset = Product.objects.annotate(
        #     discounted_price=discounted_price
        # )

        tagged_item = TaggedItem.objects.get_tags_for(Product, 1)

    except ObjectDoesNotExist:
        pass

    return render(request, 'hello.html', {'item': list(tagged_item)})