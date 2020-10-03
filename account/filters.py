import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="order_date1", lookup_expr='gte')
	end_date = DateFilter(field_name="order_date1", lookup_expr='lte')

	class Meta:
		model = Order
		fields = ['receiver_name','order_number']