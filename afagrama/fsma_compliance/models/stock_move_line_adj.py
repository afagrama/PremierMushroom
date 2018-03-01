from odoo import models, fields, api

# ______________Umar Aziz__________________________


class StockMoveLineAdj(models.Model):
    _inherit = "stock.move.line"
    _order = "result_package_id asc, id"

    lot_ref = fields.Char(string="Vendor Lot#", related="lot_id.ref", required=False, )
