from odoo import models,fields

class modelOne(models.Model):
   _name = "model.one"
   _description = "Model One"

#fields
name = fields.Char(string="Name")
price = fields.Float(string="Standard price")
quantity = fields.Integer(string="Amoumt")
review = fields.Text(string="Review of The Model one")
is_Satisfied = fields.Boolan(string="satisfied/Not")
Check_in = fields.Data(sting="Check In")
served_time = fields.Datetime(string="Served Time")
types = fields.Selection([('dine_in','Dine In'),('delivery','Delivery')])
images = fields.Binary(string="Images")
blog = fields.Html(string="Blog")