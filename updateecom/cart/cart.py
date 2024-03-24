from tempapp.models import Product

class Cart():
	"""docstring for ClassName"""
	def __init__(self, request):
		#super(ClassName, self).__init__()
		self.session = request.session
#get the current session key if it exists	
		cart=self.session.get('session_key')
		#if the user is new, no session key! create one
		if 'session_key' not in request.session:
			cart=self.session['session_key']={}
		#make sure cart is available on all pages of site
		self.cart=cart
	def add(self,product):
		product_id=str(product.id)
		#Logic
		if product_id in self.cart:
			pass
		else:
			self.cart[product_id]={'price':str(product.price)}
		self.session.modified=True
	def __len__(self):
		return len(self.cart)
	def get_prods(self):
		#get ids from cart
		product_ids=self.cart.keys()
		#use ids to lookup productss in database model
		products=Product.objects.filter(id__in=product_ids)
		#return those looked up products
		return products
	def get_quants(self):
		quantities=self.cart_add
		return quantities
	def update(self,product,quantity):
		product_id=str(product)
		product_qty=int(quantity)
		#Get cart
		ourcart= self.cart
		# update dictionary
		ourcart[product_id]=product_qty
		self.session.modified=True
		thing=self.cart_add
		return thing
	def delete(self, product):
		product_id=str(product)
		#delete from dictionary/cart
		if product_id in self.cart:
			del self.cart[product_id]
		self.session.modified=True
