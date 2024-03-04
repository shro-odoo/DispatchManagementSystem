#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Settings',
    'description':'Settings',
    'summary': 'Settings',
    'installable': True,
    'depends': ['stock','base'],
    'application': True,
    'license': 'OEEL-1',
    'auto_install' : True,
    'version': '1.0',
    'data' : [
        'views/res_config_settings_views.xml',
    ]
}

