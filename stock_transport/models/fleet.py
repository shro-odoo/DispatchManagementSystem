from odoo import api, fields, models

class Fleet(models.Model):
    _name = 'fleet.vehicle.model.category'
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Float(string='Max Weight(kg)')
    max_volume = fields.Float(string='Max Volume(m³)')

    @api.depends('name','max_weight','max_volume')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if record.max_weight or record.max_volume:
                name += f"({record.max_weight}kg,{record.max_volume}m³)"
            record.display_name = name
            

    







