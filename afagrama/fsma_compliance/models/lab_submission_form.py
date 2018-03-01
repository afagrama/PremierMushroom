from odoo import models, fields, api, _

# ______________Umar Aziz__________________________
STATE_SELECTION = [
    ('wt_results', 'Waiting Test Results'),
    ('pass', 'Pass'),
    ('fail', 'Fail'),
]


class LabSubmissionForm(models.Model):
    _name = 'lab.submission.form'
    _inherit = ['mail.thread']

    name = fields.Char(string="Name", required=False, readonly=True)
    product_id = fields.Many2one(comodel_name="product.product", string="Product", required=False, )
    stock_id = fields.Many2one(comodel_name="stock.picking", string="Receipt", required=True, )
    lot_id = fields.Many2one(comodel_name="stock.production.lot", string="Lot/Serial", required=False, )

    test_result = fields.Binary(string="Test Result")
    state = fields.Selection(STATE_SELECTION, string="", required=False, default="wt_results")
    destroy_cause = fields.Char(string="Cause", required=False, )

    salmonella_spp = fields.Boolean(string="Salmonella spp.")
    staphylococcus_aureus = fields.Boolean(string="Staphylococcus aureus")
    yeast_and_mold = fields.Boolean(string="Yeast and Mold")
    gluten = fields.Boolean(string="Gluten")
    microbial_identification = fields.Boolean(string="Microbial Identification")
    others = fields.Boolean(string="Others")
    special_instructions = fields.Text(string="Special Instructions", required=False, )

    aerobic_plate_count = fields.Boolean(string="Aerobic Plate Count")
    cl_ostridium_spp = fields.Boolean(string="CLostridium spp.")
    coli_form = fields.Boolean(string="Coli form")
    e_coli = fields.Boolean(string="E.Coli")
    e_coli_O157_H7 = fields.Boolean(string="E.Coli O157:H7")
    Listeria_spp = fields.Boolean(string="Listeria spp.")
    Listeria_monocytogenes = fields.Boolean(string="Listeria Monocytogenes")

    lab_type_id = fields.Many2one(comodel_name="lab.location.type", string="Lab Status", required=False,
                                  default=lambda self: self.env.ref('fsma_compliance.lab_type_test', False))

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('lab.sub')
        return super(LabSubmissionForm, self).create(vals)


    @api.multi
    def lab_destroy(self):
        view = self.env.ref('fsma_compliance.test_result_action_wizard_view')
        default_destroy_location = self.env.ref('fsma_compliance.lab_type_reject', False)
        return {
            'name': _('Fail Cause'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'test.result.action',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'type': 'ir.actions.act_window',
            'context': {
                'default_lab_id': self.id,
                'default_stock_id': self.stock_id.id,
                'default_lab_type_id': default_destroy_location and default_destroy_location.id,
                'action_result': 'fail',
                },
        }

    @api.multi
    def lab_to_waiting(self):
        for rec in self:
            default_test_location = self.env.ref('fsma_compliance.lab_type_test', False)
            rec.state = 'wt_results'
            rec.lab_type_id = default_test_location and default_test_location.id
            if rec.stock_id:
                rec.stock_id.lab_type_id = default_test_location and default_test_location.id

    @api.multi
    def lab_pass(self):
        view = self.env.ref('fsma_compliance.test_result_action_wizard_view')
        default_pass_location = self.env.ref('fsma_compliance.lab_type_clean', False)
        return {
            'name': _('Inventory Location'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'test.result.action',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'type': 'ir.actions.act_window',
            'context': {
                'default_lab_id': self.id,
                'default_stock_id': self.stock_id.id,
                'default_lab_type_id': default_pass_location and default_pass_location.id,
                'action_result': 'pass',
            },
        }


class CauseOfDestroy(models.TransientModel):
    _name = 'test.result.action'

    name = fields.Char(string="Fail Cause", required=False, )
    lab_id = fields.Many2one(comodel_name="lab.submission.form", string="Lab Submission", required=False, )
    stock_id = fields.Many2one(comodel_name="stock.picking", string="Stock", required=False, )
    lab_type_id = fields.Many2one(comodel_name="lab.location.type", string="Lab Type", required=False)

    @api.multi
    def confirm_action(self):
        for rec in self:
            rec.stock_id.lab_type_id = rec.lab_type_id.id
            rec.lab_id.lab_type_id = rec.lab_type_id and rec.lab_type_id.id or False
            if rec._context.get('action_result') == 'fail':
                rec.lab_id.destroy_cause = rec.name
                rec.lab_id.state = 'fail'
            else:
                rec.lab_id.state = 'pass'


class LabLocationType(models.Model):
    _name = 'lab.location.type'

    color = fields.Integer('Color')
    name = fields.Char(string="Lab Type", required=False, readonly=True)
    lab_location_id = fields.Many2one(comodel_name="stock.location", string="Lab Location", required=True, )

    count_lab_test = fields.Integer(string="", compute="_compute_lab_count")
    count_lab_clean = fields.Integer(string="", compute="_compute_lab_count")
    count_lab_production = fields.Integer(string="", compute="_compute_lab_count")
    count_lab_reject = fields.Integer(string="", compute="_compute_lab_count")

    count_pcqi_inventory = fields.Integer(string="", compute="_compute_lab_count")


    def _compute_lab_count(self):
        # TDE TODO count lab type can be done using previous two
        lab_test = self.env.ref('fsma_compliance.lab_type_test')
        lab_clean = self.env.ref('fsma_compliance.lab_type_clean')
        lab_production = self.env.ref('fsma_compliance.lab_type_production')
        lab_reject = self.env.ref('fsma_compliance.lab_type_reject')
        domains = {
            'count_lab_test': [('lab_type_id', '=', lab_test.id)],
            'count_lab_clean': [('lab_type_id', '=', lab_clean.id)],
            'count_lab_production': [('lab_type_id', '=', lab_production.id)],
            'count_lab_reject': [('lab_type_id', '=', lab_reject.id)],
        }
        for field in domains:
            data = self.env['lab.submission.form'].read_group(domains[field], ['lab_type_id'], ['lab_type_id'])
            count = {
                x['lab_type_id'][0]: x['lab_type_id_count'] for x in data if x['lab_type_id']
            }
            for record in self:
                record[field] = count.get(record.id, 0)
                # ___________________ PCQI ________________________
                record['count_pcqi_inventory'] = self.env['stock.picking'].search_count([('state', '=', 'pcqi')])

    @api.multi
    def get_lab_submission_action_kanban(self):
        return self._get_action('fsma_compliance.lab_submission_action_kanban')

    def _get_action(self, action_xmlid):
        # TDE TODO check to have one view + custo in methods
        action = self.env.ref(action_xmlid).read()[0]
        if self:
            action['display_name'] = self.display_name
        return action
