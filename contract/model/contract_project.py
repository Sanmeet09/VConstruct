from odoo import api, fields, models


class ContractProject(models.Model):
    _name = "contract.project"
    _rec_name = "vcon_dpr_project_name"

    def change_contract(self):
        for rec in self:
            rec.vcon_contract_project_state = 'submitted'

    vcon_contract_project_state = fields.Selection([
        ('ready_doc_generation', 'Ready for Document Generation'),
        ('submitted', 'Submitted'),
        ('submitted_after_revision', 'Submitted after Revision'),
        ('executed', 'Executed'),
    ], string="Status", default='ready_doc_generation')

    vcon_issuing_contractor = fields.Char(string="Issuing Contractor")
    vcon_issuing_contractor_signatory = fields.Char(string="Issuing Contractor Signatory")
    vcon_dpr_phase_code_vdc = fields.Char(string="DPR Phase Code (VDC)")
    vcon_dpr_phase_code_pcm = fields.Char(string="DPR Phase Code (PCM)")
    vcon_dpr_phase_code_asp = fields.Char(string="DPR Phase Code (ASP)")

    vcon_project_no = fields.Char(string="vconstruct UID (project no)")
    vcon_contract = fields.Char(string="vconstruct Contract")
    vcon_project_name = fields.Char(string="vconstruct Project Name")
    vcon_work_auth_no = fields.Char(string="vconstruct Work Auth. No")
    vcon_msa = fields.Char(string="vconstruct MSA (Odoo Lead No)")
    vcon_vendor = fields.Char(string="Vendor")
    vcon_service_type = fields.Char(string="vContruct Service type")
    vcon_scope_of_work = fields.Char(string="Scope of Work")
    vcon_scope_description = fields.Char(string="Scope Description (contract description)")
    vcon_scope_categories = fields.Char(string="Categories")
    vcon_compensation_type = fields.Char(string="Compensation type")
    vcon_confirmed_contract_type = fields.Selection([('1', '1'),
                                                     ('2', '2')], string="Confirmed Contract Type")
    vcon_confirmed_contract_value = fields.Char(string="Confirmed Contract Value / Amount")
    vcon_confirmed_contract_value_total = fields.Char(string="Confirmed Contract Value ( Total Amount)")

    vcon_contract_effective_date = fields.Date(string="Contract Effective Date")
    vcon_contract_signatory = fields.Char(string="vconstruct Contract Signatory")
    vcon_requestor = fields.Char(string="vContruct Requestor")
    vcon_customer_contract_signatory = fields.Char(string="Customer Contract Signatory")
    vcon_dpr_project_name = fields.Char(string="DPR Project Name")
    vcon_dpr_project_no = fields.Char(string="DPR Project No")
    vcon_alternate_description = fields.Char(string="ALTERNATE.Description")
    vcon_alternate_add_deduct = fields.Char(string="ALTERNATE.Add/Deduct")
    vcon_alternate_amount = fields.Char(string="ALTERNATE.Amount")
    vcon_reimbursed_max_amount = fields.Char(string="reimbursed a maximum amount")
    vcon_unit_rates_unit = fields.Char(string="Unit Rates.Unit")
    vcon_unit_rates_description = fields.Char(string="Unit Rates.Description")
    vcon_unit_rates_amount = fields.Char(string="Unit Rates.Amount")
    vcon__lower_company_name = fields.Char(string="Company Name")
    vcon_lower_contact = fields.Char(string="Contact")
    vcon_lower_phone = fields.Char(string="Phone")
    vcon_lower_scope_of_work = fields.Char(string="Scope of Work")
    vcon_detailed_desc_services = fields.Char(string="DETAILED DESCRIPTION OF VCONSTRUCT SERVICES (Use Internal Notes)")
    vcon_inclusion_description = fields.Char(string="Inclusions.Description")
    vcon_exclusion_description = fields.Char(string="Exclusions.Description")
    # vcon_customer_acceptance_process = fields.Char(string="Customer Acceptance Process")
    vcon_prime_contract_clauses_sub = fields.Char(string="Prime Contract Clauses (Sub Contract)")
    vcon_prime_contract_clauses_other = fields.Char(string="Prime Contract Clauses (Other Pertinent)")
    # vcon_additional_insured_parties = fields.Char(string="ADDITIONAL INSURED PARTIES")
    vcon_attachement = fields.Char(string="Attachement")
    vcon_contract_deta_desc = fields.Html(string="DETAILED DESCRIPTION OF VCONSTRUCT SERVICES")
    vcon_contract_reimbursable_expenses = fields.Html(string="REIMBURSABLE EXPENSES")
    vcon_customer_acceptance_process = fields.Html(string="Customer Acceptance Process")
    vcon_prime_contract_clauses = fields.Html(string="PRIME CONTRACT CLAUSES")
    vcon_additional_insured_parties = fields.Html(string="ADDITIONAL INSURED PARTIES")
    vcon_scope = fields.Char(string="Scope")
    vcon_date_service_start = fields.Date(string="Date Services to Start")

    vcon_contract_amount_ids = fields.One2many("contract.amount", "vcon_contract_project_id", string="CONTRACT AMOUNT")
    vcon_contract_alternate_ids = fields.One2many("contract.alternate", "vcon_contract_project_id", string="ALTERNATE")
    vcon_contract_billing_rates_ids = fields.One2many("contract.rates", "vcon_contract_project_id",
                                                      string="BILLING RATES FOR SERVICES TO BE PROVIDED")
    vcon_contract_unit_rates_ids = fields.One2many("contract.unit.rates", "vcon_contract_project_id",
                                                   string="UNIT RATES")
    vcon_contract_scope_work_ids = fields.One2many("contract.scope.work", "vcon_contract_project_id",
                                                   string="LOWER TIER SUBCONTRACTORS")
    vcon_contract_inclusions_ids = fields.One2many("contract.inclusion", "vcon_contract_project_id",
                                                   string="INCLUSIONS")
    vcon_contract_exclusions_ids = fields.One2many("contract.exclusion", "vcon_contract_project_id",
                                                   string="EXCLUSIONS")


class ContractAmount(models.Model):
    _name = "contract.amount"

    vcon_contract_project_id = fields.Many2one("contract.project")
    vcon_ca_description = fields.Char(string="DESCRIPTION")
    vcon_ca_service_type = fields.Selection([('1', '1'),
                                             ('2', '2')], string="VCONSTRUCT SERVICE TYPE")
    vcon_ca_compensation_type = fields.Selection([('1', '1'),
                                                  ('2', '2')], string="COMPENSATION TYPE")
    vcon_ca_amount = fields.Float(string="$ AMOUNT")


class ContractAlternate(models.Model):
    _name = "contract.alternate"

    vcon_contract_project_id = fields.Many2one("contract.project")
    vcon_cal_description = fields.Char(string="Description")
    vcon_cal_add_deduct = fields.Char(string="Add/Deduct")
    vcon_cal_amount = fields.Float(string="Amount ($)")


class ContractRates(models.Model):
    _name = "contract.rates"

    vcon_contract_project_id = fields.Many2one("contract.project")
    vcon_contract_category_id = fields.Many2one("product.category", string="CATEGORY")
    vcon_contract_hourly_rate = fields.Float(string="HOURLY RATE")


class ContractUnitRates(models.Model):
    _name = "contract.unit.rates"

    vcon_contract_project_id = fields.Many2one("contract.project")
    vcon_contract_unit = fields.Float(string="UNIT #")
    vcon_contract_unit_desc = fields.Char(string="UNIT DESCRIPTION")
    vcon_contract_unit_rate = fields.Float(string="$/UNIT")


class ContractScopeWork(models.Model):
    _name = "contract.scope.work"

    vcon_contract_project_id = fields.Many2one("contract.project")
    vcon_contract_csw_com_name = fields.Many2one("res.company", string="Company Name")
    vcon_contract_csw_contact = fields.Char(string="Contact")
    vcon_contract_csw_phone = fields.Char(string="Phone")
    vcon_contract_csw_scope_of_work = fields.Char(string="Scope of work")


class ContractInclusion(models.Model):
    _name = "contract.inclusion"

    vcon_contract_project_id = fields.Many2one("contract.project")
    vcon_contract_ci_desc = fields.Char(string="DESCRIPTION")


class ContractExclusion(models.Model):
    _name = "contract.exclusion"

    vcon_contract_project_id = fields.Many2one("contract.project")
    vcon_contract_ce_desc = fields.Char(string="DESCRIPTION")
