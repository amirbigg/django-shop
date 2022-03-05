

CART_SESSION_ID = 'cart'

class Cart:
	def __int__(self, request):
		self.session = request.session
		cart = self.session.get(CART_SESSION_ID)
		if not cart:
			cart = self.session[CART_SESSION_ID] = {}
		self.cart = cart

	def add(self, product, quantity):
		product_id = str(product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity':0, 'price':str(product.price)}
		self.cart[product_id]['quantity'] += quantity
		self.save()

	def save(self):
		self.session.modified = True
