from odoo import fields, api, models, _


class InheritProject(models.Model):
    _inherit = 'project.project'

    is_parent = fields.Boolean('Is Parent', default=False)
    parent_project = fields.Many2one('project.project', string='Parent Project')
    main_project = fields.Many2one('project.project', string='Main Project')
    lead_id = fields.Many2one('crm.lead', 'Lead')

    child_count = fields.Integer('Child Project')

    def compute_child_project(self):
        self.child_count = self.env['project.project'].search_count([('parent_project', '=', self.id)])

    def view_project(self):
        return {
            'name': "Project",
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'project.project',
            'domain': [('parent_project', '=', self.id)]
        }