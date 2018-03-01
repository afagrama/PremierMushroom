from odoo import models, fields, api

# ______________Umar Aziz__________________________


class SupplierManagement(models.Model):
    _name = 'supplier.management'
    _inherit = ['mail.thread']

    name = fields.Char(string="Name", required=False, readonly=True)

    vendor_id = fields.Many2one(comodel_name="res.partner", string="Vendor", required=False)

    organic_certification = fields.Binary(string="Organic Cert. File", required=False, )
    organic_Cert_issue_date = fields.Date(string="Organic Cert. Issue Date", required=False, )
    organic_cert_exp_date = fields.Date(string="Organic Cert. Exp. Date", required=False, )
    fs_cert = fields.Char(string="Food Safety Cert.", required=False, )
    fs_cert_file = fields.Binary(string="Food Safety Cert.", required=False, )
    fs_cert_exp_date = fields.Date(string="Food Safety Cert. Exp. Date", required=False, )
    third_parity_audit_date = fields.Char(string="3rd Party Audit Date", required=False, )
    third_parity_report = fields.Date(string="3rd Party Report Reviewed", required=False, )
    annual_approval_date = fields.Date(string="Annual Approval Date", required=False, )
    comments = fields.Text(string="Comments", required=False, )

    specs = fields.Boolean(string="Specs", required=False, )
    allergen_statement = fields.Boolean(string="Allergen Statement", required=False, )
    gluten_cert_exp_date = fields.Date(string="Gluten Cert. Exp Date", required=False, )
    vendor_questionnaire = fields.Boolean(string="Vendor Questionnaire", required=False, )
    nutrition_data = fields.Boolean(string="Nutrition Data", required=False, )
    aflatoxin_statement = fields.Boolean(string="Aflatoxin Statement", required=False, )
    letter_of_guarantee = fields.Boolean(string="Letter of Guarantee", required=False, )
    letter_of_guarantee_date = fields.Date(string="Letter of Guarantee", required=False, )
    reg_compliance_review = fields.Boolean(string="Reg. Compliance Review", required=False, )

    product_ids = fields.Many2many(comodel_name="product.product", string="Product")

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('supplier.management')
        return super(SupplierManagement, self).create(vals)



class ResPartnerAdj(models.Model):
    _inherit = 'res.partner'

    supplier_id = fields.Many2one(comodel_name="supplier.management", string="Supplier Management", required=False, )
