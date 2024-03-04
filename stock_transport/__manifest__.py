#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock Transport',
    'description':'Transport Management System',
    'summary': 'Transport management system',
    'installable': True,
    'depends': ['fleet','stock_picking_batch'],
    'application': True,
    'license': 'OEEL-1',
    'version': '1.0',
    'data' : [
        'security/ir.model.access.csv',
        'views/fleet_views.xml',
        'views/inventory_views.xml',
    ]
}
