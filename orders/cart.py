

CART_SESSION_ID = 'cart'

class Cart:
	def __int__(self, request):
		self.session = request.session
		cart = self.session.get(CART_SESSION_ID)
		if not cart:
			cart = self.session[CART_SESSION_ID] = {}
		self.cart = cart

