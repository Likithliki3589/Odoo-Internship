from odoo import models, fields , api
from odoo.exceptions import ValidationError
class Food(models.Model):
	_name = "food.food"
	_description = "Model For Food"
	_rec_name = "partner_id"


	# fields
	name = fields.Char(string="Name")
	partner_id = fields.Many2one('res.partner',string="Name")
	price = fields.Float(string="Standard Price")
	quantity = fields.Integer(string="Amount")
	review = fields.Text(string="Review Of The Food")
	is_satisfied = fields.Boolean(string="Satisfied/Not")
	check_in = fields.Date(string="Check In")
	served_time = fields.Datetime(string="Served Time")
	types = fields.Selection([('dine_in','Dine In'),('delivery','Delivery')])
	images = fields.Binary(string="Images")
	blog = fields.Html(string="Blog")
	sale_order_id = fields.Many2one('sale.order',string="Sale Order")
	invoice_id = fields.Many2one('account.move',string="Related Invoice")

	_sale_created = fields.Boolean(string="Sale Order Created")

	def create_sale_order(self):
		sale_order = self.env['sale.order'].create([{
			'partner_id':23
			}])
		self._sale_created = True
		return sale_order


	def create_invoice(self):
		pass
	def create_contacts(self):
		pass
	def create_purchase_order(self):
		pass

	# ORM Methods
	# Create
	# Extend     = Extending base logic + Custom logic (base+custom)
	# Override   = Is Removing all the base Function and Setting Your logic

	@api.model
	def create(self,vals):

		print("Before RES")
		print("Self is ===",self)
		print("Vals is ===",vals)

		res = super(Food,self).create(vals)

		print("After RES")
		print("Self is ===",self)
		print("Vals is ===",vals)
		print("RES is ===",res)

		if res.is_satisfied == False: # checking the is_satisfield is true or not
			res.is_satisfied = True   # assingning it true

		return res
	
	def write(self,vals):
		
		print("Before RES")
		print("Self is ===",self)
		print("Vals is ===",vals)
		print("Before  RES=== ",self.review)

		print("==========================")
		res = super(Food,self).write(vals)

		print("After RES")
		print("Self is ===",self)
		print("Vals is ===",vals)
		print("RES is ===",res)
		print("After Res  === ",self.review)
		return res
	

	def unlink(self):
		for i in self:
			if i.is_satisfied == True:
				raise ValidationError("You cannot delete a Satisfied Records")
		res = super(Food, self).unlink()

		return res