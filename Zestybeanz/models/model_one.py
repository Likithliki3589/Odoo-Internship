from odoo import models, fields, api

class ModelOne(models.Model):
    _name = "model.one"
    _description = "Model One"

    seq = fields.Char(string="Sequence")

    name = fields.Char(string="Name", help='You can add your name here', copy=False)
    age = fields.Integer(string="Age", default=18)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", required=True, copy=False)
    active = fields.Boolean("Active")
    description = fields.Text("Description", default="Test Description")
    date = fields.Date(string="Date", required=True)
    partner_ids = fields.Many2many('res.partner', string="Partner")
    product_ids = fields.Many2many('product.template', 'model_one_product_rel', 'model_one_id', 'product_id', string="product")
    model_one_line_ids = fields.One2many('model.one.lines', 'model_one_id', string="Product")
    sale_ids = fields.Many2many('sale.order','model_one_sale_rel','model_one_id','sale_id', string="Sale")


    @api.model
    def create(self,vals):
        print('----------', self.env['ir.sequence'])
        vals['seq'] = self.env['ir.sequence'].next_by_code('sequence.model.one')
        res = super(ModelOne,self).create(vals)
        return res
   
class ModelOneLines(models.Model):
	
	_name = "model.one.lines"
	_description = "Model One Lines"
	
	name = fields.Char(string="Name", help='You can add your name here')
	price = fields.Float(string="Price")
	product_id = fields.Many2one('product.template', string="Product")
	model_one_id = fields.Many2one('model.one', string="Model One", domain="[('gender', '=', 'female'),('age', '>', 18)]")  	