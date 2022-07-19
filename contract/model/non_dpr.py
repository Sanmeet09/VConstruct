from odoo import models, fields, api, _


class NonDpr(models.Model):
    _name = "non.dpr"

    vconstruct_project_name = fields.Char(string="vConstruct Project Name")

    contract_type = fields.Selection([('1', '1'),
                                      ('2', '2')], string="Contract Type")

    conf_cont_val = fields.Integer(string="Confirmed Contract Amount")
    cont_amt_word = fields.Char(string="Contract Amount in Words")
    dpr_unt = fields.Char(string="DPR Unit/ Group/ Affiliate")
    cust_addr = fields.Char(string="Customer Address")
    cont_ef_date = fields.Char(string="Contract Effective Date")
    vconstruct_cont_sign = fields.Char(string="vConstruct Contract Signatory")
    cust_cont_sign = fields.Char(string="Customer Contract Signatory")

    # field for DETAILED DESCRIPTION OF VCONSTRUCT SERVICES
    detail_desc_vconst = fields.Html(string="DETAILED DESCRIPTION OF VCONSTRUCT SERVICES")

    scope_of_work = fields.Char(string="Scope of Work")
    input_req = fields.Char(string="Inputs Required")
    assmp_made = fields.Char(string="Assumptions Made")
    public_holiday_list = fields.Char(string="Public Holiday List")

    # fields related about bank
    bank_name = fields.Char(string="Bank Name")
    bank_addr = fields.Char(string="Bank Address")
    account_name = fields.Char(string="Account Name")
    aba_routing = fields.Char(string="ABA Routing")
    bank_account = fields.Char(string="Bank Account")
    bank_cont_name = fields.Char(string="Bank Contact Name")
    tel_num = fields.Char(string="Telephone Number")

    unit_rate_id = fields.One2many('unit.rate.line', 'parent_id', 'unit rate id')
    inc_desc_id = fields.One2many('inc.desc.line', 'parent_id', 'inc desc id')
    esc_desc_id = fields.One2many('esc.desc.line', 'parent_id', 'esc desc id')
    cost_break_id = fields.One2many('cost.breakdown.line', 'parent_id', 'cost breakdown id')


# Unit Rates one to many table
class UnitRate(models.Model):
    _name = "unit.rate.line"

    parent_id = fields.Many2one('non.dpr', 'Non DPR ID')

    unit_rate_unit = fields.Char(string="Unit")
    unit_rate_description = fields.Char(string="Description")
    unit_rate_amount = fields.Integer(string="Amount")


# Inclusions.Description one to many table
class InclusionsDesc(models.Model):
    _name = "inc.desc.line"

    parent_id = fields.Many2one('non.dpr', 'Non DPR ID')

    inc_desc = fields.Char(string="Inclusions Description")


# Exclusions Description one to many table
class ExclusionsDesc(models.Model):
    _name = "esc.desc.line"

    parent_id = fields.Many2one('non.dpr', 'Non DPR ID')

    esc_desc = fields.Char(string="Exclusions Description")


# cost breakdowm one to many table
class CostBreakdown(models.Model):
    _name = 'cost.breakdown.line'

    parent_id = fields.Many2one('non.dpr', 'Non DPR ID')
    sr_no = fields.Integer(string='Sr. No.')
    scope_desc = fields.Text(string="Scope Description")
    vconstruct_service_type = fields.Selection([('1', '1'),
                                                ('2', '2')], string="vConstruct Service type")
    comp_type = fields.Selection([('1', '1'),
                                  ('2', '2')], string="Compensation Type")
    cost_value = fields.Integer('Cost')
    conf_cont_val_total_amount = fields.Integer(string="Confirmed Contract Value ( Total Amount)")
