from odoo import models, fields, api

# ______________Umar Aziz__________________________
SSOP_SELECTION = [('acceptable_inspection', 'Acceptable inspection'), ('deviation_noted', 'Deviation noted requires Corrective Action'), ]
WAREHOUSE_SELECTION = [('one', '#1'), ('two', '#2'), ]


class SSOPOperationCheck(models.Model):
    _name = 'ssop.operation.check'
    _inherit = ['mail.thread']

    name = fields.Char(string="Name", required=False, readonly=True)
    warehouse = fields.Selection(WAREHOUSE_SELECTION, string="Warehouse", default="one")
    # _________________ page cCMP ___________________

    illness = fields.Selection(SSOP_SELECTION, string="Illness", required=False, default="acceptable_inspection")
    clean_garments = fields.Selection(SSOP_SELECTION, string="Clean Garments", required=False, default="acceptable_inspection")
    eating_or_drinking = fields.Selection(SSOP_SELECTION, string="Eating or Drinking", required=False, default="acceptable_inspection")
    wash_hands = fields.Selection(SSOP_SELECTION, string="Wash Hands", required=False, default="acceptable_inspection")
    food_beverages = fields.Selection(SSOP_SELECTION, string="Food, Beverages", required=False, default="acceptable_inspection")

    jewelry_policy = fields.Selection(SSOP_SELECTION, string="Jewelry Policy", required=False, default="acceptable_inspection")
    sanitizers_operation = fields.Selection(SSOP_SELECTION, string="Sanitizers Operation", required=False, default="acceptable_inspection")
    sash_facilities_supplied = fields.Selection(SSOP_SELECTION, string="Wash Facilities Supplied", required=False, default="acceptable_inspection")
    change_rooms = fields.Selection(SSOP_SELECTION, string="Change Rooms", required=False, default="acceptable_inspection")
    pest_control = fields.Selection(SSOP_SELECTION, string="Pest Control", required=False, default="acceptable_inspection")
    uniform = fields.Selection(SSOP_SELECTION, string="Uniform", required=False, default="acceptable_inspection")

    # _________________ page Process ___________________

    receiving = fields.Selection(SSOP_SELECTION, string="Receiving", required=False, default="acceptable_inspection")
    allergen_control = fields.Selection(SSOP_SELECTION, string="Allergen Control", required=False, default="acceptable_inspection")
    shipping = fields.Selection(SSOP_SELECTION, string="shipping", required=False, default="acceptable_inspection")

    effective_EMP = fields.Selection(SSOP_SELECTION, string="Effective EMP", required=False, default="acceptable_inspection")
    FM_control = fields.Selection(SSOP_SELECTION, string="FM Control", required=False, default="acceptable_inspection")

    # _________________ page Facility ___________________

    Mop_and_broom = fields.Selection(SSOP_SELECTION, string="Mop and Broom", required=False, default="acceptable_inspection")
    security = fields.Selection(SSOP_SELECTION, string="Security", required=False, default="acceptable_inspection")
    water_delivery = fields.Selection(SSOP_SELECTION, string="Water Delivery", required=False, default="acceptable_inspection")
    floors_and_drains = fields.Selection(SSOP_SELECTION, string="Floors and Drains", required=False, default="acceptable_inspection")
    Walls_doors_and_ceiling = fields.Selection(SSOP_SELECTION, string="Walls, Doors and Ceiling", required=False, default="acceptable_inspection")
    exterior_dock = fields.Selection(SSOP_SELECTION, string="Exterior Dock", required=False, default="acceptable_inspection")
    inspect_hardware = fields.Selection(SSOP_SELECTION, string="Inspect Hardware", required=False, default="acceptable_inspection")
    dock_area = fields.Selection(SSOP_SELECTION, string="Dock Area", required=False, default="acceptable_inspection")

    dock_doors = fields.Selection(SSOP_SELECTION, string="Dock Doors", required=False, default="acceptable_inspection")
    sweep_front = fields.Selection(SSOP_SELECTION, string="Sweep Front", required=False, default="acceptable_inspection")
    HVAC_Filter_replacement = fields.Selection(SSOP_SELECTION, string="HVAC Filter Replacement", required=False, default="acceptable_inspection")
    fire_safelty = fields.Selection(SSOP_SELECTION, string="Fire Safelty", required=False, default="acceptable_inspection")
    waste_mngt = fields.Selection(SSOP_SELECTION, string="Waste Mngt", required=False, default="acceptable_inspection")
    warehouse_floors = fields.Selection(SSOP_SELECTION, string="Warehouse Floors", required=False, default="acceptable_inspection")
    foreign_material = fields.Selection(SSOP_SELECTION, string="Foreign Material", required=False, default="acceptable_inspection")

    # _________________ page Facility Lights ___________________

    food_processing_areas = fields.Selection(SSOP_SELECTION, string="Food Processing Areas", required=False, default="acceptable_inspection")
    inspection_stations = fields.Selection(SSOP_SELECTION, string="Inspection Stations", required=False, default="acceptable_inspection")
    storage_areas = fields.Selection(SSOP_SELECTION, string="Storage Areas", required=False, default="acceptable_inspection")

    light_fittings_are_clean = fields.Selection(SSOP_SELECTION, string="Light Fittings are Clean", required=False, default="acceptable_inspection")
    light_fixtures = fields.Selection(SSOP_SELECTION, string="Light Fixtures", required=False, default="acceptable_inspection")
    light_fittings_breakage = fields.Selection(SSOP_SELECTION, string="Light Fittings Breakage", required=False, default="acceptable_inspection")

    # _________________ page Equipment ___________________

    forklift = fields.Selection(SSOP_SELECTION, string="Forklift", required=False, default="acceptable_inspection")
    lockout = fields.Selection(SSOP_SELECTION, string="Lockout", required=False, default="acceptable_inspection")
    blade_sharpness = fields.Selection(SSOP_SELECTION, string="Blade Sharpness", required=False, default="acceptable_inspection")
    knife_blade = fields.Selection(SSOP_SELECTION, string="Knife Blade", required=False, default="acceptable_inspection")

    blade_disposal = fields.Selection(SSOP_SELECTION, string="Blade Disposal", required=False, default="acceptable_inspection")
    cutters_and_knives_location = fields.Selection(SSOP_SELECTION, string="Cutters and Knives Location", required=False, default="acceptable_inspection")
    breakroom = fields.Selection(SSOP_SELECTION, string="Breakroom", required=False, default="acceptable_inspection")
    key_control = fields.Selection(SSOP_SELECTION, string="Key Control", required=False, default="acceptable_inspection")
    haz_comm = fields.Selection(SSOP_SELECTION, string="Haz Comm", required=False, default="acceptable_inspection")

    # _________________ page other ___________________

    first_aid = fields.Selection(SSOP_SELECTION, string="First Aid", required=False, default="acceptable_inspection")
    shelf_stable_packaged_goods = fields.Selection(SSOP_SELECTION, string="Shelf Stable Packaged Goods", required=False, default="acceptable_inspection")
    hazardous_chemicals = fields.Selection(SSOP_SELECTION, string="Hazardous Chemicals", required=False, default="acceptable_inspection")

    scales = fields.Selection(SSOP_SELECTION, string="Scales", required=False, default="acceptable_inspection")
    safety_meeting = fields.Selection(SSOP_SELECTION, string="Safety Meeting", required=False, default="acceptable_inspection")
    toolbox_talks = fields.Selection(SSOP_SELECTION, string="Toolbox Talks", required=False, default="acceptable_inspection")
    UPS = fields.Selection(SSOP_SELECTION, string="UPS", required=False, default="acceptable_inspection")

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('op.check')
        return super(SSOPOperationCheck, self).create(vals)
