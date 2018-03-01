from odoo import models, fields, api

# ______________Umar Aziz__________________________
PRE_SELECTION = [('acceptable_inspection', 'Acceptable inspection'), ('deviation_noted', 'Deviation noted requires Corrective Action'), ]


class ProductionPreOperation(models.Model):
    _name = 'prod.pre.operation'
    _inherit = ['mail.thread']

    name = fields.Char(string="Name", required=False, readonly=True)
    sanitary_procedure = fields.Selection(PRE_SELECTION, string="Sanitary Procedure", default="acceptable_inspection")
    food_contact_surfaces = fields.Selection(PRE_SELECTION, string="Food contact surfaces", required=False, default="acceptable_inspection")
    spray_equipment_with_water = fields.Selection(PRE_SELECTION, string="Spray equipment with water", required=False, default="acceptable_inspection")
    store_cleaning_materials = fields.Selection(PRE_SELECTION, string="Label and Store cleaning materials", required=False, default="acceptable_inspection")
    ATP_swab = fields.Selection(PRE_SELECTION, string="ATP Swab", required=False, default="acceptable_inspection")
    transport_equipment = fields.Selection(PRE_SELECTION, string="Transport equipment", required=False, default="acceptable_inspection")
    labeling_cleaners = fields.Selection(PRE_SELECTION, string="Labeling Cleaners", required=False, default="acceptable_inspection")
    examine_surfaces = fields.Selection(PRE_SELECTION, string="Examine Surfaces", required=False, default="acceptable_inspection")
    sanitizing_equipment = fields.Selection(PRE_SELECTION, string="Sanitizing Equipment", required=False, default="acceptable_inspection")
    remove_debris = fields.Selection(PRE_SELECTION, string="Remove Debris", required=False, default="acceptable_inspection")
    non_food_contact_surfaces = fields.Selection(PRE_SELECTION, string="Non food contact surfaces", required=False, default="acceptable_inspection")

    inspect_for_missing_parts = fields.Selection(PRE_SELECTION, string="Inspect for missing parts", required=False, default="acceptable_inspection")
    cover_all_electrical_components = fields.Selection(PRE_SELECTION, string="Cover all electrical components", required=False, default="acceptable_inspection")
    inspect_pre_operational = fields.Selection(PRE_SELECTION, string="Inspect pre-operational equipment", required=False, default="acceptable_inspection")
    apply_cleaner = fields.Selection(PRE_SELECTION, string="Apply Cleaner", required=False, default="acceptable_inspection")
    scrubbing_equipment = fields.Selection(PRE_SELECTION, string="Scrubbing Equipment", required=False, default="acceptable_inspection")
    approved_sanitizer = fields.Selection(PRE_SELECTION, string="Approved Sanitizer", required=False, default="acceptable_inspection")
    spray_equipment = fields.Selection(PRE_SELECTION, string="Spray equipment/utensils with water", required=False, default="acceptable_inspection")
    use_appropriate_tools = fields.Selection(PRE_SELECTION, string="Use appropriate tools", required=False, default="acceptable_inspection")
    bulk_product = fields.Selection(PRE_SELECTION, string="Bulk product and packaging storage", required=False, default="acceptable_inspection")
    re_assemble_equipment = fields.Selection(PRE_SELECTION, string="Re-assemble equipment", required=False, default="acceptable_inspection")
    unacceptable_results = fields.Selection(PRE_SELECTION, string="Unacceptable results", required=False, default="acceptable_inspection")
    # _________________ page environmental ___________________

    wipe_production_room_worktables = fields.Selection(PRE_SELECTION, string="Wipe production room work tables", required=False, default="acceptable_inspection")
    hang_hose = fields.Selection(PRE_SELECTION, string="Hang hose", required=False, default="acceptable_inspection")
    sweep_mop_production_floors = fields.Selection(PRE_SELECTION, string="Sweep and mop production floors", required=False, default="acceptable_inspection")
    wipe_down_any_dust = fields.Selection(PRE_SELECTION, string="Wipe Down any Dust", required=False, default="acceptable_inspection")

    sweep_mats_and_mop = fields.Selection(PRE_SELECTION, string="Sweep mats and mop as needed", required=False, default="acceptable_inspection")
    wipe_down_wash_sinks_daily = fields.Selection(PRE_SELECTION, string="Wipe down all hand wash sinks daily", required=False, default="acceptable_inspection")
    damp_mop_floor_wipe_walls = fields.Selection(PRE_SELECTION, string="Damp mop floor and wipe walls", required=False, default="acceptable_inspection")

    # _________________ page other ___________________

    allergen_preventive_controls = fields.Selection(PRE_SELECTION, string="Allergen Preventive Controls", required=False, default="acceptable_inspection")
    empty_trash_bins = fields.Selection(PRE_SELECTION, string="Empty trash bins", required=False, default="acceptable_inspection")
    wipe_production_room = fields.Selection(PRE_SELECTION, string="Wipe Production Room", required=False, default="acceptable_inspection")
    wash_trash_bins = fields.Selection(PRE_SELECTION, string="Wash trash bins", required=False, default="acceptable_inspection")
    in_house_monitoring = fields.Selection(PRE_SELECTION, string="In-house monitoring", required=False, default="acceptable_inspection")

    good_manufacturing_practices = fields.Selection(PRE_SELECTION, string="Good Manufacturing Practices", required=False, default="acceptable_inspection")
    sanitize_conveyor_belt = fields.Selection(PRE_SELECTION, string="Sanitize conveyor belt", required=False, default="acceptable_inspection")
    sanitize_all_parts = fields.Selection(PRE_SELECTION, string="Sanitize all parts", required=False, default="acceptable_inspection")
    disassemble_clean_and_sanitize = fields.Selection(PRE_SELECTION, string="Disassemble, clean and sanitize", required=False, default="acceptable_inspection")

    @api.multi
    def do_print_prod_pre_op(self):
        return self.env.ref('fsma_compliance.action_production_pre_operation_pdf').report_action(self)

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('pre.op')
        return super(ProductionPreOperation, self).create(vals)



