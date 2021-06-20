# OOP SHOPPING CART
class Cart:
	def __init__(self):
		self.items = []

	def show_items(self):
		print(self.items)

	def add_quantity(self, item_added):
		self.items.append(item_added)
		print("\n-- * You added " + str(self.items) + " * --\n")

	def remove_quantity(self):
		for item_obj in self.items:
			if item_to_remove.lower() == item_obj.name.lower():
				self.items.remove(item_obj)
				break

	def view_cart(self):
		print('='*40)
		if not self.items:
			print("\nItem(s) in cart --  No Item(s)  --")
		else:
			display_cart = []
			for obj in self.items:
				if obj.name not in [i['name'] for i in display_cart]:
					display_cart.append({
						'name': obj.name,
						'price': obj.price
					})
			for idx, item in enumerate(display_cart):
				print(f"{idx+1}: {item['name']} {[i.name for i in self.items].count(item['name'])} x ${item['price']}")
		print('='*40)
		print(f"Total: ${sum([i.price for i in self.items]):,.2f}")

class Item:
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def __repr__(self):
		return f'Item {self.name} ${self.price}'

class ShoppingCart:
	@classmethod
	def run(self):
		cart = Cart()

		print("WELCOME TO THE SHOP")
		instructions = print("""
		Type 'add' to add an item.
		Type 'view' to see your cart.
		Type 'del' to remove the last item you added fromm the cart.
		Type 'checkout' to purchase your items.""")
		active = True
		while active: # Starts shopping loop
			cart.view_cart()
			choice = input("\nWhat would you like to do? 'add', 'view', 'del', 'checkout': ") # Takes input for options
		
			if choice == 'add': # Shows user availible items	
				# if anything but a float is placed in  price input, return, try again or something of that nature
				add_item = input("\nType the name of the item to add it: ") # Allows user to add item to cart
				add_price = input("\nHow much is it? ")
				while True:
					try:
						add_price = float(add_price)
						break
					except:
						print("Try again")
						add_price = input("\nHow much is it? ")

				product = Item(add_item, float(add_price))
				cart.add_quantity(product)

			# elif choice == 'view': # User can view cart
			# 	(Cart()).view_cart()
		
			elif choice == 'del': # User can del most recent addition to the cart
				cart.remove_quantity() # cart.pop()
		
			else: # User can checkout and end loop/ program
				if choice == 'checkout':
					active = False
					print("\n-- Thanks for shopping with us! --")
					cart.view_cart()

ShoppingCart.run()
