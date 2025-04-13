from odoo import models, fields, api

class LogisticsShipment(models.Model):
    _name = 'logistics.shipment'
    _description = 'Logistics Shipment'

    name = fields.Char(string='Shipment ID', required=True, copy=False, readonly=True, default=lambda self: 'New')
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    origin = fields.Char(string='Origin')
    destination = fields.Char(string='Destination')
    delivery_date = fields.Date(string='Delivery Date')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered')
    ], string='Status', default='draft')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('logistics.shipment') or 'New'
        return super().create(vals)
