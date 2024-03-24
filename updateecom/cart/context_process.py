from.cart import Cart
# cart/context_processors.py

'''from .views import get_cart_items

def cart(request):
    # Retrieve cart items using the get_cart_items function
    cart_items = get_cart_items(request)
    return {'cart_items': cart_items}'''

#create context processor so our cart can work on all pages in site
'''def recursive_function(n):
    # Base case: Termination condition
    if n == 0:
        return 0
    # Recursive case: Call the function with a smaller input
    else:
        return n + recursive_function(n - 1)'''

def cart(request):
	#return the default data from our cart
	return{'cart':Cart(request)}
'''def cart(request):
    # Your cart logic here
    cart_items = get_cart_items(request)
    return {'cart_items': cart_items}'''
