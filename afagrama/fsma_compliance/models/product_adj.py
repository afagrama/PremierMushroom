from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare, float_round


# ______________Umar Aziz__________________________


class ProductTemplate(models.Model):
    _inherit = "product.template"

    country_ids = fields.Many2many(comodel_name="res.country", string="Countries Of Origin")
