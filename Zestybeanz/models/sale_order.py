from odoo import models, fields, api


class SaleOrder(models.Model):
	
	_inherit = "sale.order"
	
	model_one_id = fields.Many2one('model.one', string="Model One")
	description = fields.Text("Description", default="Test Description")