from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    _name = 'stock.picking'
   
    volume = fields.Float(compute='_compute_volume', store=True)

    @api.depends('move_line_ids.quantity','product_id.volume','product_id')
    def _compute_volume(self):
     for record in self: 
        record.volume = 0.0
        for product in record.move_line_ids:  
                record.volume += product.product_id.volume * product.quantity
        