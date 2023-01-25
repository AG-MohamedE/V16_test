# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Duplicate Sale and Purchase Order Line',
    'version': '15.0.0.0',
    'category': 'Sales',
    'license': 'LGPL-3',
    'summary': 'Duplicate sale order line duplicate purchase order line',
    'description': """
        
            Easy to duplicate sale and purchase order line in odoo,

    """,
    'author': 'Auguria SAS',
    'website': 'https://www.auguria.fr',
    'depends': ['base', 'sale_management', 'purchase_stock'],
    'data': [
        'views/sale_purchase_view.xml'
    ],
    'installable': True,
    'support': 'contact@auguria.fr',
    'application': True,
}
