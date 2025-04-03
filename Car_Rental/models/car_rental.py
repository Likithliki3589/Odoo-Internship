from odoo import models, fields

class CarRental(models.Model):
    _name = 'car.rental'
    _description = 'Car Rental'
    
    car_name = fields.Char(string='Car Name', required=True)
    car_model = fields.Char(string='Car Model', required=True)
    wheel_type = fields.Selection([
        ('alloy', 'Alloy'),
        ('steel', 'Steel'),
        ('chrome', 'Chrome'),
        ('carbon', 'Carbon')
    ], string='Wheel Type', required=True)
    body_color = fields.Char(string='Body Color', required=True)
    available = fields.Boolean(string='Available', default=True)
    seat_count = fields.Integer(string='Seat Count', required=True)
    amount = fields.Float(string='Amount per Day', required=True)