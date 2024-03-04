from odoo import api, fields, models

class Dock(models.Model):
    _name = 'stock.dock'
    _description = 'Dock'
   
    name = fields.Char(string='Name', required=True)


    



    







