from odoo import fields, api, models, _
from odoo.exceptions import ValidationError


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    order_line = fields.One2many('sale.order.line', 'order_id', string='Order Lines',
                                 states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True,
                                 auto_join=True, domain=[('parent_order_line', '=', False)])
    count_project = fields.Integer('Project Count', compute='compute_project_count')

    def request_order(self):
        pass

    # function to get projects in sale order
    def compute_project_count(self):
        self.count_project = self.env['project.project'].search_count([('lead_id', '=', self.opportunity_id.id)])

    def view_project(self):
        # here we are passing the view for smart button
        return {
            'name': "Project",
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'project.project',
            'domain': [('lead_id', '=', self.opportunity_id.id)]
        }


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    lead_id = fields.Many2one('crm.lead')
    stage = fields.Selection(string='Stage', selection=[('lost', 'Lost'), ('award', 'Awarded'), ('expired', 'Expired'),
                                                        ('hold', 'Hold')], default='lost', required=True)
    order_id = fields.Many2one('sale.order', string='Order Reference', required=False, ondelete='cascade', index=True,
                               copy=False)
    order_line_ids = fields.One2many('sale.order.line', 'parent_order_line', copy=False)
    parent_order_line = fields.Many2one('sale.order.line', ondelete='cascade', copy=False)
    project_id = fields.Many2one('project.project', 'Project Id')
    confirm_type = fields.Char(string="Confirm Contract Type")

    parent_opp = fields.Char('Parent Opportunity')
    v_poc = fields.Char('vConstruct POC')
    service = fields.Char('Service Vertical')
    conf_cont_val = fields.Char(string="Confirm Contract Value")
    customer_poc = fields.Selection([('1', '1'),
                                     ('2', '2')], string="Customer POC")
    pr_submit_date = fields.Date('Proposal Submitted Date')
    drp = fields.Char(string='DPR Phase Code')
    price_list = fields.Char('PriceList ($/Hr)')
    work_req = fields.Char('Work Request')
    unique_key = fields.Char('Unique Key')
    comp = fields.Char('Component')
    business_unit = fields.Char('vConstruct BU')
    awarded_date = fields.Date('Awarded Date')
    start_date = fields.Date(string="Estimated Start Date")
    end_date = fields.Date(string="Estimated End Date")

    change_order = fields.Char('Change Order')
    invoice_date = fields.Date('Invoice Till Date')
    invoice_to_do = fields.Char('Invoice To Do')

    # on clicking view button in sale_order_line a form opens
    def open_order_line(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Open Line',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': self._name,
            'res_id': self.id,
            'target': 'new',
            'context': {'order_id': self.order_id.id}
        }

