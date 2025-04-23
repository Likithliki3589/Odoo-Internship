from odoo import models, fields, api

class ModelOne(models.Model):
    _name = "model.one"
    _description = "Model One"

    seq = fields.Char(string="sequence")
    name = fields.Char(string="Name", help='You can add your name here', copy=False)
    age = fields.Integer(string="Age", default=18)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", required=True, copy=False)
    active = fields.Boolean("Active")
    description = fields.Text("Description", default="Test Description")
    date = fields.Date(string="Date", required=True)
    partner_ids = fields.Many2many('res.partner', string="Partner")
    product_ids = fields.Many2many('product.template', 'model_one_product_rel', 'model_one_id', 'product_id', string="product")
    model_one_line_ids = fields.One2many('model.one.lines', 'model_one_id', string="Product")
    sale_ids = fields.Many2many('sale.order','model_one_sale_rel','model_one_id','sale_id', string="Sale order")
    sale_id = fields.Many2one('sale.order', string="Sales")

    def write_values(self):
        #special commands for writing to relational fields
        #1. many2many fields
        products = self.env['product.template'].search([('list_price', '>', 200)], limit=1).id
        order = self.env['sale.order'].search([('id', '=', 26)], limit=1).id
        #self.write({'product_ids' : [[6, 0, products]]})                                        #replace existing values with new values - syntax : [6, 0, [IDs]]
        #self.write({'product_ids' : [[5]]})                                                     #unlink all records                      - syntax : [5]
        #self.write({'product_ids' : [[4, products]]})                                           #link valus to an existing record        - syntax : [4, ID]
        #self.write({'product_ids' : [[3, products]]})                                           #unlink a record (don't delete)          - syntax : [3, ID]
        #self.write({'sale_ids' : [[2, order]]})                                                 #unlinks and deletes the record          - syntax : [2, ID]
        #self.write({'product_ids' : [[0, 0, {'name': 'Test Product', 'list_price':200}]]})        
		
        #2. one2many fields 
        #self.write({'model_one_line_ids' : [[0, 0, {'name': 'Test 1', 'product_id':products, 'price': 250}]]})    
        #line = self.model_one_line_ids.filtered(lambda l : l.price == 300).id
        existing_line = self.env['model.one.lines'].search([('price', '=', 300)], limit=1).id
        #ex_line = self.env['model.one.lines'].search([('model_one_id', '=', False)], limit=1).id
        #self.write({'model_one_line_ids' : [[1, line, {'price': 350}]]}) 
        #self.write({'model_one_line_ids' : [[2, line]]})  
        #self.write({'model_one_line_ids' : [[3, line]]})  
        self.write({'model_one_line_ids' : [[4, existing_line]]})  
        #self.write({'model_one_line_ids' : [[4, ex_line]]})  
        #self.write({'model_one_line_ids' : [[6, 0, ex_line]]})     

    def helloworld(self):
        print("hello world")  

    def show_wizard(self):
	    return {
            'type': 'ir.actions.act_window',
            'name': 'My Sample Wizard',
            'res_model': 'sample.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('Zestybeanz.view_form_sample_wizard').id,
            'target': 'new',
            'context' : {'default_name': 'Likith'}
        }
    

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