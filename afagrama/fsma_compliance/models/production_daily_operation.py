from odoo import models, fields, api

# ______________Umar Aziz__________________________
DAILY_SELECTION = [('acceptable_inspection', 'Acceptable inspection'),
                   ('deviation_noted', 'Deviation noted requires Corrective Action'), ]


class ProductionDailyOperation(models.Model):
    _name = 'production.daily.operation'
    _inherit = ['mail.thread']

    name = fields.Char(string="Name", required=False, readonly=True)

    # _________________ page cGMP ___________________

    poor_health = fields.Selection(DAILY_SELECTION, string="Poor Health", required=False, default="acceptable_inspection")
    designated_uniform = fields.Selection(DAILY_SELECTION, string="Designated uniform", required=False,
                                          default="acceptable_inspection")
    handle_with_care = fields.Selection(DAILY_SELECTION, string="Handle with care", required=False,
                                        default="acceptable_inspection")
    use_sanitizer = fields.Selection(DAILY_SELECTION, string="Use Sanitizer", required=False,
                                     default="acceptable_inspection")
    outer_garments_requirements = fields.Selection(DAILY_SELECTION, string="Outer Garments requirements", required=False,
                                                   default="acceptable_inspection")

    no_smoking = fields.Selection(DAILY_SELECTION, string="No smoking", required=False,
                                  default="acceptable_inspection")
    designated_area_for_meds = fields.Selection(DAILY_SELECTION, string="Designated area for meds", required=False,
                                                default="acceptable_inspection")
    supply_products = fields.Selection(DAILY_SELECTION, string="Supply products", required=False,
                                       default="acceptable_inspection")
    hand_wash_facilities = fields.Selection(DAILY_SELECTION, string="Hand wash facilities", required=False,
                                            default="acceptable_inspection")

    # _________________ page SSOP ___________________

    prevent_contamination = fields.Selection(DAILY_SELECTION, string="Prevent Contamination", required=False,
                                             default="acceptable_inspection")
    equipment_are_cleaned_and_sanitized = fields.Selection(DAILY_SELECTION, string="Equipment are cleaned and sanitized",
                                                           required=False,
                                                           default="acceptable_inspection")

    # _________________ page Equipment ___________________

    wipe_dry_equipment = fields.Selection(DAILY_SELECTION, string="Wipe Dry equipment", required=False,
                                          default="acceptable_inspection")
    ensure_sanitizing_conveyor_belt = fields.Selection(DAILY_SELECTION, string="Ensure Sanitizing conveyor belt",
                                                       required=False, default="acceptable_inspection")
    maintain_inventory = fields.Selection(DAILY_SELECTION, string="Maintain Inventory", required=False,
                                          default="acceptable_inspection")
    malfunctioning_pieces = fields.Selection(DAILY_SELECTION, string="Malfunctioning pieces", required=False,
                                          default="acceptable_inspection")

    disassemble_clean_sanitize = fields.Selection(DAILY_SELECTION, string="Disassemble, clean & sanitize.",
                                                  required=False, default="acceptable_inspection")
    disassemble_parts_and_sanitize = fields.Selection(DAILY_SELECTION, string="Disassemble parts and sanitize",
                                                      required=False,
                                                      default="acceptable_inspection")
    remove_debris = fields.Selection(DAILY_SELECTION, string="Remove debris", required=False,
                                     default="acceptable_inspection")

    # _________________ page other ___________________

    prevent_cross_contact = fields.Selection(DAILY_SELECTION, string="Prevent Cross contact", required=False,
                                             default="acceptable_inspection")
    maintain_log = fields.Selection(DAILY_SELECTION, string="Maintain Log", required=False,
                                    default="acceptable_inspection")
    maintain_H2O2 = fields.Selection(DAILY_SELECTION, string="Maintain H2O2", required=False,
                                     default="acceptable_inspection")
    CIP_procedures = fields.Selection(DAILY_SELECTION, string="CIP Procedures", required=False,
                                      default="acceptable_inspection")
    clean_sanitize_equipment = fields.Selection(DAILY_SELECTION, string="Clean and Sanitize equipment", required=False,
                                                default="acceptable_inspection")
    pallets = fields.Selection(DAILY_SELECTION, string="Pallets", required=False,
                               default="acceptable_inspection")

    production_supplies = fields.Selection(DAILY_SELECTION, string="Production Supplies", required=False,
                                           default="acceptable_inspection")
    maintain_bags = fields.Selection(DAILY_SELECTION, string="Maintain bags", required=False,
                                     default="acceptable_inspection")
    hygiene_practices_and_procedures = fields.Selection(DAILY_SELECTION, string="hygiene practices, and procedures",
                                                        required=False, default="acceptable_inspection")
    identify_issues = fields.Selection(DAILY_SELECTION, string="Identify issues", required=False,
                                       default="acceptable_inspection")

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('prod.op')
        return super(ProductionDailyOperation, self).create(vals)


