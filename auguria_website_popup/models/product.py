# -*- coding: utf-8 -*-
# Copyright (C) 2022 - Auguria (<https://www.auguria.fr>).

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)
from odoo.addons.http_routing.models.ir_http import slug


class ProductInherit(models.Model):
    _inherit = 'product.template'

    adulte_content = fields.Boolean(string='Adulte product')


#category e-commerce
class ProductPublicCategoryInherit(models.Model):
    _inherit = 'product.public.category'

    adult_content = fields.Boolean(string='Adult product')

#category e-commerce
class ProductPublicattributeInherit(models.Model):
    _inherit = 'product.attribute.category'

    adult_content = fields.Boolean(string='Adult product')
