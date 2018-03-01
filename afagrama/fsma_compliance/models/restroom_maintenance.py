from odoo import models, fields, api

# ______________Umar Aziz__________________________
BATH_SELECTION = [('checked', 'Checked'), ('filled', 'Filled'), ]
STATE_SELECTION = [('draft', 'Draft'), ('PCQI_required', 'PCQI Required'), ('complete', 'Complete'), ]


class RestroomMaintenance(models.Model):
    _name = 'restroom.maintenance'
    _inherit = ['mail.thread']

    name = fields.Char(string="Name", required=False, readonly=True)
    bathroom_num = fields.Integer(string="Bathroom #", required=False, )

    toilets_Cleaned = fields.Boolean(string="Toilets Cleaned")
    mirrors_cleaned = fields.Boolean(string="Mirrors Cleaned")
    sinks_cleaned = fields.Boolean(string="Sinks Cleaned")
    floors_mopped = fields.Boolean(string="Floors Mopped")
    floors_swept = fields.Boolean(string="Floors Swept")

    state = fields.Selection(STATE_SELECTION, string="Status", required=False, )

    toilet_paper = fields.Selection(BATH_SELECTION, string="Toilet paper", required=False, )
    paper_towels = fields.Selection(BATH_SELECTION, string="Paper towels", required=False, )
    seat_covers = fields.Selection(BATH_SELECTION, string="Seat Covers", required=False, )
    soap_dispenser = fields.Selection(BATH_SELECTION, string="Soap Dispenser", required=False, )
    trash = fields.Selection(BATH_SELECTION, string="Trash", required=False, )

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('restroom.log')
        return super(RestroomMaintenance, self).create(vals)



