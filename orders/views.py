from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm 
from cart.cart import Cart 

def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
			if cart.coupon:
				order.coupon = cart.coupon
				order.discount = cart.coupon.discount
			order.save()
			for item in cart:
				OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
			cart.clear()
			return render(request, 'orders/order/created.html', {'order':order})
	else:
		form = OrderCreateForm()
	return render(request, 'orders/order/create.html', {'cart':cart, 'form':form})

def admin_order_detail(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	return render(request, 'admin/orders/order/detail.html', {'order': order})