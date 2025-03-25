from odoo import models, fields

class modelOne(models.Model):

 _name = "model.one"
 _description = "model One"

#fields
name = fiedls.Char(string="Name")
price = fields.Float(string="Standard price")
quantity = fields.Integer(string="Integer")
review = fields.Text(string="Review of The model one")
is_Satisfied = fields.Boolan(string="satisfied/Not")
Check_in = fileds.Data(sting="Check In")
served_time = fields.Datetime(string)