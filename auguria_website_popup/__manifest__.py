# -*- coding: utf-8 -*-
# Copyright (C) 2022 - Auguria (<https://www.auguria.fr>).
{
    "name": "Popup +18 Alert Website",
    "version": "14.0.0",
    'author': 'Auguria SAS',
    'license': 'LGPL-3',
    'website': 'https://www.auguria.fr',
    "category": "Website",
    "summary": """
show a +18 popup on website, message popup,
smart alert, message alert alcohol website,
simple popup, website popup,popup alert,
Work portfolio, Disclaimer Content, Any information Odoo
""",
    "description": """
This module useful to show a popups, advertisement banner,
New Product Information, Alert Message, Warning, Notifications,
Work portfolio, alcohol banner.
""",
    "depends": ["base", "website", "portal", "website_sale", "website_sale_comparison"],
    "data": [
        
              "views/popup.xml",
              "views/assets.xml",
              "views/layout.xml",
              "views/res_config_settings_view.xml",
              "views/website_view.xml",
              "views/product_inherit_view.xml",

            ],
    "application": True,
    "images": ["static/description/background.png",],              
    "auto_install":False,
    "installable" : True,
    'support': 'contact@auguria.fr',
    "price": 150,
    "currency": "EUR"   
}
