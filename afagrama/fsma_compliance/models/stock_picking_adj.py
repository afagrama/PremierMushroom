from odoo import models, fields, api, _, tools
from odoo.exceptions import UserError
import datetime


# ______________Umar Aziz__________________________


class PickingPickingAdj(models.Model):
    _inherit = "stock.picking"

    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting', 'Waiting Another Operation'),
        ('confirmed', 'Waiting'),
        ('assigned', 'Ready'),
        ('done', 'PCQI Required'),
        ('pcqi', 'Finished'),
        ('cancel', 'Cancelled'),
    ], string='Status', compute='_compute_state',
        copy=False, index=True, readonly=True, store=True, track_visibility='onchange',
        help=" * Draft: not confirmed yet and will not be scheduled until confirmed.\n"
             " * Waiting Another Operation: waiting for another move to proceed before it becomes automatically available (e.g. in Make-To-Order flows).\n"
             " * Waiting: if it is not ready to be sent because the required products could not be reserved.\n"
             " * Ready: products are reserved and ready to be sent. If the shipping policy is 'As soon as possible' this happens as soon as anything is reserved.\n"
             " * Done: has been processed, can't be modified or cancelled anymore.\n"
             " * Cancelled: has been cancelled, can't be confirmed anymore.")

    pcqi_user_id = fields.Many2one(comodel_name="res.users", string="PCQI user", required=False, )
    pcqi_date = fields.Date(string="PCQI Date", required=False, )

    lab_type_id = fields.Many2one(comodel_name="lab.location.type", string="Lab Status", required=False)

    lab_submission_id = fields.Many2one(comodel_name="lab.submission.form", string="Lab Submission Form", required=False, )

    photo_upload = fields.Binary(string="Photo upload")

    is_allergen_pallet_tag = fields.Boolean(string="Allergen Clearly Stated on Pallet Tag")

    is_semi_trailer = fields.Boolean(string="Semi-Trailer")
    is_common_carrier = fields.Boolean(string="Common Carrier")
    is_ocean_container = fields.Boolean(string="Ocean Container")
    is_personal_vehicle = fields.Boolean(string="Personal Vehicle")

    is_foreign_odors = fields.Boolean(string="Foreign Odors")
    is_moisture = fields.Boolean(string="Moisture")
    is_pests = fields.Boolean(string="Pests")
    is_broken_glass = fields.Boolean(string="Broken Glass")
    is_substances_or_residues = fields.Boolean(string="Substances or residues that may compromise organic integrity")
    is_holes_in_sides = fields.Boolean(string="Holes in sides or bed that may compromise organic integrity")

    is_pallet_damage = fields.Boolean(string="Pallet Damage: broken/torn packaging")
    is_signs_of_contamination = fields.Boolean(string="Signs of contamination and infestation")

    is_number_of_broken_packaging = fields.Boolean(string="Number of broken/torn packaging")
    is_corrective_action = fields.Boolean(string="Corrective Action")

    is_photo = fields.Boolean(string="Photo")
    is_client_released_shipment = fields.Boolean(string="Client released shipment in writing")
    is_client_to_send_new_truck = fields.Boolean(string="Client to send new truck")

    is_allergen_pallet_tag_out = fields.Boolean(string="Allergen Clearly Stated on Pallet Tag")

    show_validate = fields.Boolean(
        compute='_compute_show_validate',
        help='Technical field used to compute whether the validate should be shown.')

    is_testable = fields.Boolean(string="Testable?", compute='_check_testable_product')

    @api.multi
    def _check_testable_product(self):
        for rec in self:
            if rec.move_lines:
                testable_obj = self.env.ref('fsma_compliance.route_warehouse0_testable')
                product_routes = rec.move_lines[0].product_id.route_ids
                if testable_obj in product_routes:
                    rec.is_testable = True
                else:
                    rec.is_testable = False

    def _put_in_pack(self):
        res = super(PickingPickingAdj, self)._put_in_pack()
        for pick in self:
            if res:
                # res.name = pick.name + "/PLT{:04}".format(len(pick.move_lines.move_line_ids))
                res.name = pick.name + "/" + self.env['ir.sequence'].next_by_code('stock.pallet.package') or _(
                    'Unknown Pack')
        return res

    @api.multi
    def set_to_pcqi(self):
        self.ensure_one()
        if not self.move_lines and not self.move_line_ids:
            raise UserError(_('Please add some lines to move'))
        for rec in self:
            rec.pcqi_user_id = rec.env.user.id
            rec.pcqi_date = datetime.datetime.now().strftime('%Y-%m-%d')
            rec.state = 'pcqi'

    @api.multi
    def lab_submission(self):
        self.ensure_one()
        if not self.move_lines and not self.move_line_ids:
            raise UserError(_('Please add some lines to move'))
        elif self.lab_submission_id:
            raise UserError(_('You added a lab submission form before for this Stock'))
        res = self.env['stock.production.lot'].search([('product_id', '=', self.move_lines[0].product_id.id)], limit=1)
        if not res:
            raise UserError(_('There is no Lot for selected product!.\n Make sure to create Lot for Product ({}) '
                              'you trying to add'.format(self.move_lines[0].product_id.name)))
        for rec in self:
            lab_type_test = self.env.ref('fsma_compliance.lab_type_test', False)
            internal_type_id = self.env.ref('stock.picking_type_internal', False)
            rec.lab_type_id = lab_type_test and lab_type_test.id
            view = self.env.ref('fsma_compliance.lab_submission_form_form_view')

            first_move_line = rec.move_lines and rec.move_lines[0] or False

            move_line_obj = self.env['stock.move.line']
            move_line_ids = []
            for x in first_move_line.move_line_ids:
                move_line_ids.append(move_line_obj.create({
                    'product_id': x.product_id.id,
                    'production_id': x.production_id.id,
                    'product_uom_qty': x.product_qty,
                    'qty_done': x.qty_done,
                    'lot_id': x.lot_id.id,
                    'location_id': x.location_dest_id.id,
                    'location_dest_id': lab_type_test.lab_location_id.id,
                    'product_uom_id': x.product_uom_id.id,
                }))

            first_mline_copy = self.env['stock.move'].create({
                'name': first_move_line.product_id.name,
                'product_id': first_move_line.product_id.id,
                'product_uom': first_move_line.product_uom.id,
                'location_id': first_move_line.location_dest_id.id,
                'location_dest_id': lab_type_test.lab_location_id.id,
                'move_line_ids': [(4, x.id) for x in move_line_ids]
            })

            wiz = self.env['lab.submission.form'].create({
                'product_id': first_move_line and first_move_line.product_id.id,
                'stock_id': rec.id,
                'lot_id': res.id})
            inventory_to_testing = self.env['stock.picking'].create({
                'location_dest_id': lab_type_test and lab_type_test.lab_location_id.id,
                'location_id': rec.location_id.id,
                'origin': rec.origin,
                'move_type': 'direct',
                'picking_type_id': internal_type_id and internal_type_id.id,
                'move_lines': [(4, first_mline_copy.id)],
                'scheduled_date': fields.Datetime.now()})

            for move_line_id in move_line_ids:
                move_line_id.picking_id = inventory_to_testing.id
            first_mline_copy.picking_put_in_pack()

            if inventory_to_testing.state == 'assigned':
                inventory_to_testing.button_validate()
            rec.lab_submission_id = wiz.id
            return {
                'name': _('Lab Submission'),
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'lab.submission.form',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'current',
                'res_id': wiz.id,
            }

    @api.depends('move_type', 'move_lines.state', 'move_lines.picking_id')
    @api.one
    def _compute_state(self):
        ''' State of a picking depends on the state of its related stock.move
        - Draft: only used for "planned pickings"
        - Waiting: if the picking is not ready to be sent so if
          - (a) no quantity could be reserved at all or if
          - (b) some quantities could be reserved and the shipping policy is "deliver all at once"
        - Waiting another move: if the picking is waiting for another move
        - Ready: if the picking is ready to be sent so if:
          - (a) all quantities are reserved or if
          - (b) some quantities could be reserved and the shipping policy is "as soon as possible"
        - Done: if the picking is done.
        - Cancelled: if the picking is cancelled
        '''
        if not self.move_lines:
            self.state = 'draft'
        elif any(move.state == 'draft' for move in self.move_lines):  # TDE FIXME: should be all ?
            self.state = 'draft'
        elif all(move.state == 'cancel' for move in self.move_lines):
            self.state = 'cancel'
        elif all(move.state in ['cancel', 'done'] for move in self.move_lines):
            self.state = 'done'
        else:
            relevant_move_state = self.move_lines._get_relevant_state_among_moves()
            if relevant_move_state == 'partially_available':
                self.state = 'assigned'
            else:
                self.state = relevant_move_state

    @api.multi
    @api.depends('state', 'is_locked')
    def _compute_show_validate(self):
        for picking in self:
            if self._context.get('planned_picking') and picking.state == 'draft':
                picking.show_validate = False
            elif picking.state not in ('draft', 'confirmed', 'assigned', 'pcqi') or not picking.is_locked:
                picking.show_validate = False
            else:
                picking.show_validate = True

    @api.multi
    def print_hold_pallet(self):
        return self.env.ref('fsma_compliance.action_hold_pallet_tag_pdf').report_action(self)


class ProductionLotInherit(models.Model):
    _inherit = 'stock.production.lot'

    @api.model_cr
    def init(self):
        self._cr.execute("ALTER TABLE %s DROP CONSTRAINT %s" % ('stock_production_lot', 'stock_production_lot_name_ref_uniq'))