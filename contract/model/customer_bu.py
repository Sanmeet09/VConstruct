from odoo import fields, api, models, _


class CustomerBU(models.Model):
    _name = 'customer.bu'
    _inherit = 'mail.thread'
    _rec_name = 'vc_customer_project'
    _description = 'Details of all the CRM'

    vc_customer_uid = fields.Char('vconstruct Project Number')
    vc_customer_contract = fields.Char('vconstruct Contract ')
    vc_customer_project = fields.Char('vconstruct Project Name')
    vc_customer_work_auth = fields.Char('vconstruct Work Auth. No')
    vc_customer_msa = fields.Char('vconstruct MSA No')
    vc_customer_msa_date = fields.Char('MSA Date')
    vc_contractor_name = fields.Char('Name')
    vc_customer_address = fields.Char('Customer Address')

    # consultant
    vc_cons_name = fields.Char('Name')
    vc_cons_address = fields.Char('Address')
    vc_project = fields.Char('vconstruct Project')

    vc_customer_categories = fields.Char('Categories')
    vc_customer_contract_value_amount = fields.Char('Confirmed Contract Value / Amount')
    vc_customer_contract_value_total = fields.Char('Confirmed Contract Value ( Total Amount)')
    vc_customer_action = fields.Char('Action Items')
    vc_customer_dpr_unit = fields.Char('DPR Unit/ Group/ Affiliate')

    vc_customer_effective_date = fields.Char('Contract Effective Date')
    vc_contract_signatory = fields.Char('vconstruct Contract Signatory')
    customer_contract_signatory = fields.Char('Customer Contract Signatory')
    vc_customer_alt = fields.Char('ALT #')
    vc_alternate_desc = fields.Char('ALTERNATE.Description')
    vc_alternate_amount = fields.Char('ALTERNATE.Amount')
    vc_reimbursed_amount = fields.Char('reimbursed a maximum amount')
    vc_unit_rate = fields.Char('Unit Rates.Unit')
    vc_unit_rate_desc = fields.Char('Unit Rates.Description')
    vc_unit_rate_amount = fields.Char('Unit Rates.Amount')
    vc_company_name = fields.Char('Company Name')
    vc_contact = fields.Char('Contact')
    vc_phone = fields.Char('Phone')
    vc_scope_of_work = fields.Char('Scope of Work')
    vc_exclusion = fields.Char('Exclusions.Description')
    vc_customer_acceptance = fields.Char('Customer Acceptance Process')
    vc_lump_amount = fields.Char('Lump Sum Amount')
    vc_cost_reimbursable = fields.Char('Cost-Reimbursable, Not-to-Exceed (NTE):')
    vc_cost_reimbursable_max_price = fields.Char('Cost-Reimbursable with a Guaranteed Maximum Price (GMP):')
    vc_unit_rate_exceed = fields.Char('Unit Rate, Not-to-Exceed (NTE):')
    vc_attachement = fields.Char('Attachement')

    customer_bu_ids = fields.One2many('customer.bu.line', 'customer_bu_id', 'Customer ids')
    vc_alternative_ids = fields.One2many('customer.alternative.line', 'vc_alternative', 'alternative')
    vc_billing_ids = fields.One2many('customer.billing.line', 'vc_billing', 'billing')
    vc_unit_rate_ids = fields.One2many('customer.unit.line', 'vc_unit_rate_id', 'unit')
    vc_contractor_ids = fields.One2many('sub.contractors.line', 'vc_contractor_id', 'sub')


class CustomerBuLine(models.Model):
    _name = 'customer.bu.line'

    customer_bu_id = fields.Many2one('customer.bu', 'customer id')

    vc_item = fields.Char('ITEM #')
    vc_customer_service = fields.Char('VCONSTRUCT SERVICE TYPE')
    vc_phase_code = fields.Char('PHASE CODE')
    vc_customer_compensation = fields.Char('COMPENSATION TYPE')
    vc_customer_scope = fields.Char('DESCRIPTION')
    vc_scope_amount = fields.Char('$ AMOUNT')


class CustomerAlternativeLine(models.Model):
    _name = 'customer.alternative.line'

    vc_alternative = fields.Many2one('customer.bu', 'alternative')

    #     alternatives fields
    vc_alt = fields.Char('ALT #')
    vc_alt_desc = fields.Char('ALTERNATE DESCRIPTION')
    vc_customer_service_alt = fields.Char('VCONSTRUCT SERVICE TYPE')
    vc_alternate_deduct = fields.Char('ADD/DEDUCT')
    vc_scope_amount_alt = fields.Char('$ AMOUNT')


class CustomerBillingLine(models.Model):
    _name = 'customer.billing.line'

    vc_billing = fields.Many2one('customer.bu', 'billing')

    vc_category = fields.Char('CATEGORY')
    vc_hour_rate = fields.Char('HOURLY RATE')


class CustomerUnitLine(models.Model):
    _name = 'customer.unit.line'

    vc_unit_rate_id = fields.Many2one('customer.bu', 'unit')

    vc_unit = fields.Char('UNIT #')
    vc_unit_desc = fields.Char('UNIT DESCRIPTION')
    vd_unit_price = fields.Char('$/UNIT')


class SubContractorsLine(models.Model):
    _name = 'sub.contractors.line'

    vc_contractor_id = fields.Many2one('customer.bu', 'SUB contractors')
    vc_company_name = fields.Char('COMPANY NAME')
    vc_contact = fields.Char('CONTACT')
    vc_phonr = fields.Char('PHONE')
    vc_scope_of_work = fields.Char('SCOPE OF WORK')
