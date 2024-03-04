from odoo import api, fields, models 

class Inventory(models.Model):
    _name = 'stock.picking.batch'
    _inherit = 'stock.picking.batch'

    vehicle = fields.Many2one('fleet.vehicle', string='Vehicle', required=False)
    vehicle_category = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')
    weight = fields.Float(compute='_compute_weight', store=True)
    volume = fields.Float(compute='_compute_volume', store=True)
    dock_id = fields.Many2one('stock.dock', string="Dock")
    lines = fields.Integer(compute='_compute_lines', string='Lines', store=True)
    transfer = fields.Integer(compute='_compute_transfer', string='Transfer', store=True)

    @api.depends('move_line_ids', 'vehicle_category')
    def _compute_weight(self):
     for record in self:
        total_weight = 0.0
        for line in record.move_line_ids:
            if line.product_id and line.product_id.weight:
                total_weight += line.product_id.weight * line.quantity
        max_weight = record.vehicle_category.max_weight or 1.0  
        record.weight = (total_weight / max_weight) * 100

    @api.depends('move_line_ids', 'vehicle_category')
    def _compute_volume(self):
     for record in self: 
        total_volume = 0.0
        for line in record.move_line_ids:  
            if line.product_id and line.product_id.volume:
                total_volume += line.product_id.volume * line.quantity
        max_volume = record.vehicle_category.max_volume or 1.0
        record.volume = (total_volume / max_volume) * 100
        
    @api.depends('vehicle_category', 'dock_id')
    def _compute_display_name(self):
     for record in self:
        name = f"{record.dock_id.name}:{record.vehicle_category.max_weight}kg {record.vehicle_category.max_volume}m³"
        record.display_name = name

    @api.depends('picking_ids')
    def _compute_transfer(self):
        for record in self:
            record.transfer = len(record.picking_ids)
    
    @api.depends('move_line_ids')
    def _compute_lines(self):
        for record in self:
            record.lines = len(record.move_line_ids)

