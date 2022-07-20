from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class CrmProject(models.Model):
    _inherit = "crm.lead"

    # All Relational Fields
    project_id = fields.Many2one('project.project', 'Project Id')
    order_line = fields.One2many('sale.order.line', 'lead_id')
    crm_ids = fields.One2many('custom.crm.lead.line', 'crm_id', 'CRM ids')

    # Project Information Fields (CMIC)
    u_id = fields.Char(string="vConstruct UID")
    cmic_project = fields.Char('CMIC Project Name')
    cmic_project_no = fields.Char('CMIC Project Number')
    opportunity_name = fields.Char('Opportunity Name')
    opportunity_no = fields.Char('Opportunity Number')

    # Customer Information Fields
    customer_gp = fields.Char(string="Customer Group")
    sub_gp = fields.Char(string="Customer Sub-Group")
    customer_addr = fields.Char(string="Customer Address")
    customer_opportunity = fields.Char(string="Customer Opportunity")
    # custom_job_co = fields.Integer(string="Customer Job Code")
    customer_job_code = fields.Char(string="Customer Job Code")
    ssg = fields.Char(string="SSG/Non SSG")
    billable_currency = fields.Char('Billable Currency')
    total_conf_value = fields.Char(string=" Total Confirm Contract Value")

    # Other Information fields
    project_name = fields.Char('Project Name')
    sez_unit = fields.Selection([('1', '1'),
                                 ('2', '2')], string="vConstruct SEZ Unit")
    action_item = fields.Char('Action Items')
    action_due_date = fields.Char('Action Item Due Date')
    award_date = fields.Date(string='Awarded Date')

    # API field
    api_fields = fields.Selection(selection=[('cosential', 'Cosential'), ('cmmic', 'CMMIC'), ('manual', 'Manual')],
                                  string="API Data")

    # Scope Information Notebook
    business_unit = fields.Char(string="vConstruct BU")
    # vc_poc = fields.Char(string="vConstruct POC", required=True)
    v_poc = fields.Char('vConstruct POC')
    customer_poc = fields.Selection([('1', '1'),
                                     ('2', '2')], string="Customer POC")
    service = fields.Char('Service Vertical')
    awarded_date = fields.Date('Awarded Date')
    start_date = fields.Date(string="Estimated Start Date")
    end_date = fields.Date(string="Estimated End Date")
    work_req = fields.Char('Work Request')
    price_list = fields.Char('PriceList ($/Hr)')

    # Budget Information inside order_line
    # conf_cont_type = fields.Selection([('1', '1'),
    #                                    ('2', '2')], string="Confirm Contract Type")
    conf_type = fields.Char(string="Confirm Contract Type")
    drp = fields.Char(string='DPR Phase Code')
    conf_cont_value = fields.Char('Confirm Contract Value')

    # Jira fields
    unique_key = fields.Char('Unique Key')
    comp = fields.Char('Component')

    # fields inside Cosential page in notebook
    crm_project_number = fields.Char('DPR Project Number')
    crm_dpr_region = fields.Char('DPR Region')
    crm_dpr_business = fields.Char('DPR Business Unit')
    crm_preconstruction = fields.Date('Preconstruction Start Date')
    crm_preconstruction_end = fields.Date('Preconstruction End Date')
    crm_construction_start = fields.Date('Construction Start Date')
    crm_construction_end = fields.Date('Construction End Date')
    crm_project_volume = fields.Date('Total Project Volume')
    crm_core_market = fields.Char('Core Market')

    # integer field for counting project
    project_count = fields.Integer('Lead Count', compute='compute_project_count')

    # count the number of project created
    def compute_project_count(self):
        self.project_count = self.env['project.project'].search_count([('lead_id', '=', self.id)])

    # view all the project inside smart button
    def view_project(self):
        # here we are passing the view for smart button
        return {
            'name': "Project",
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'project.project',
            'domain': [('lead_id', '=', self.id)]
        }

        # header button function to Create a project

    def create_project(self):
        if not self.project_id:
            main_project = self.env['project.project'].create({
                'name': self.name,
                'partner_id': self.partner_id.id,
                'lead_id': self.id
            })
            self.project_id = main_project.id
        for rec in self.order_line:
            if rec.stage == 'award':
                if not rec.project_id:
                    is_project = True if rec.order_line_ids else False
                    ordr_id = self.env['project.project'].create({
                        'name': self.name + '/ ' + rec.product_id.name,
                        'partner_id': self.partner_id.id,
                        'is_parent': is_project,
                        'main_project': self.project_id.id,
                        'lead_id': self.id
                    })
                    rec.project_id = ordr_id.id
                for child_rec in rec.order_line_ids:
                    if not child_rec.project_id:
                        child_project = self.env['project.project'].create({
                            'name': self.name + '/ ' + rec.product_id.name + '/ ' + child_rec.product_id.name,
                            'partner_id': self.partner_id.id,
                            'parent_project': child_rec.parent_order_line.project_id.id,
                            'main_project': self.project_id.id,
                            'lead_id': self.id
                        })
                        child_rec.project_id = child_project.id
                        child_rec.parent_order_line.project_id.is_parent = True

    # function for api_fields
    def get_lead_name(self):
        if not self.api_fields:
            raise ValidationError('Please Select The Option')
        api_data = {
            'name': _(self.api_fields.title()),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'context': {'create': False},
            'target': 'new',
        }
        if self.api_fields == 'manual':
            api_data.update({'res_model': 'manual.leads'})
        else:
            api_data.update({'res_model': 'manual.api.wizards'})
        return api_data

    # This function create a record in sale.order when stage is awarded
    @api.model
    def create(self, vals):
        res = super(CrmProject, self).create(vals)
        sow = res.order_line.filtered(lambda rec: rec.stage == 'award')
        if sow:
            order_id = self.env['sale.order'].create(
                {'partner_id': res.partner_id.id,
                 'opportunity_id': res.id,
                 'origin': res.name,
                 'order_line': [(4, line.id) for line in sow]
                 })
            res.write({'order_ids': [(4, order_id.id)]})
        return res

    def write(self, vals):
        res = super(CrmProject, self).write(vals)
        sow = self.order_line.filtered(lambda rec: rec.stage == 'award' and not rec.order_id)
        if sow and not self.order_ids:
            order_id = self.env['sale.order'].create(
                {'partner_id': self.partner_id.id,
                 'opportunity_id': self.id,
                 'origin': self.name,
                 'order_line': [(4, line.id) for line in sow]
                 })
            self.write({'order_ids': [(4, order_id.id)]})
        elif sow and vals.get('order_line'):
            self.order_ids.write({'order_line': [(4, line.id) for line in sow]})
        return res


# class for child /sub opportunity page in notebook
class CustomCrmLeadLine(models.Model):
    _name = 'custom.crm.lead.line'

    crm_id = fields.Many2one('crm.lead', 'CRM id')

    create_crm_date = fields.Datetime('Created On')
    opportunity_crm = fields.Char('Opportunity')
    partner_id = fields.Many2one('res.partner', 'Customer')
    country_id = fields.Many2one('res.country', 'Country')
    team_id = fields.Many2one('crm.team', 'Sales Team')
    total_revenue_crm = fields.Integer('Total Revenue')
