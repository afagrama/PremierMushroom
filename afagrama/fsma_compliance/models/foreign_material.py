from odoo import models, fields, api

# ______________Umar Aziz__________________________
MATERIAL_SELECTION = [('pass', 'Pass'), ('fail', 'Fail'), ]
LOG_SELECTION = [('AMS', 'AMS'), ('action_pac', 'Action Pac'), ]


class ForeignMaterial(models.Model):
    _name = 'foreign.material'
    _inherit = ['mail.thread']

    name = fields.Char(string="Name", required=False, readonly=True)
    log = fields.Selection(LOG_SELECTION, string="Log : ", required=False, default="AMS")
    product_id = fields.Many2one(comodel_name="product.product", string="Product", required=False, )
    lot_id = fields.Many2one(comodel_name="stock.production.lot", string="Lot #", required=False, )
    manufacturing_order_id = fields.Many2one(comodel_name="mrp.production", string="Manufacturing Order", required=False, )
    date_and_time = fields.Datetime(string="Date & Time", required=False, )

    # ________________ LOG Action Pac ______________

    blue_card_stain_2_0mm = fields.Selection(MATERIAL_SELECTION, string="BLUE CARD- Stainless 2.0 mm", required=False, )
    yellow_card_nonferrous_1_5mm = fields.Selection(MATERIAL_SELECTION, string="YELLOW CARD- Non-Ferrous 1.5 mm", required=False, )
    red_card_ferrous_1_2mm = fields.Selection(MATERIAL_SELECTION, string="RED CARD- Ferrous 1.2 mm", required=False, )

    # ________________ LOG AMS ______________

    blue_card_stain_5_556mm = fields.Selection(MATERIAL_SELECTION, string="BLUE CARD- Stainless 5.556 mm", required=False, )
    yellow_card_ferrous_2_5mm = fields.Selection(MATERIAL_SELECTION, string="YELLOW CARD- Ferrous 2.5 mm", required=False, )
    red_card_nonferrous_5_5mm = fields.Selection(MATERIAL_SELECTION, string="RED CARD- Non-Ferrous 5.5 mm", required=False, )

    findings = fields.Char(string="Findings", required=False, )
    corrective_action = fields.Char(string="CORRECTIVE ACTION", required=False,
                                    help="*Remove bag from line, X through label&date, Place on HOLD "
                                         "until end of run, Note on Daily Production Log")
    metal_object_retained = fields.Char(string="METAL OBJECT RETAINED", required=False, help="label, seal,&give to QC")
    rejects = fields.Integer(string="Rejects", required=False, )
    poundage_destroyed = fields.Float(string="Poundage Destroyed", required=False, )
    detection_method = fields.Char(string="Detection Method", required=False, )
    evidence = fields.Char(string="Evidence", required=False, )

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('foreign.material')
        return super(ForeignMaterial, self).create(vals)

