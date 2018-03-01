from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare, float_round


# ______________Umar Aziz__________________________


class mrpProductionAdj(models.Model):
    _inherit = "mrp.production"

    is_label_matches_product = fields.Boolean(string="Label Matches Product",)
    is_scale_calibration = fields.Boolean(string="Scale Calibration",)
    is_metal_detector_calibration = fields.Boolean(string="Metal Detector Calibration",)

    ATP_swabs = fields.Selection(string="ATP Swabs", selection=[('pass', 'Pass'), ('fail', 'Fail'), ], required=False, )
    ATP_upload = fields.Binary(string="ATP upload",)

    finish_yield = fields.Char(string="Finish Yield", required=False, )
    finished_weight = fields.Char(string="Finished Weight", required=False, )
    shrinkage_overage = fields.Char(string="Shrinkage/Overage %", required=False, )
    reject_explanation = fields.Char(string="Reject(s) explanation", required=False, )

    actions = fields.Text(string="Actions", required=False, )
    comments = fields.Text(string="Comments", required=False, )
