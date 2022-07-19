from odoo import fields, models, api, _


class ManualLeads(models.Model):
    _name = 'manual.leads'

    name = fields.Char(string="Name")

    def data_pass(self):
        data = self.env['crm.lead'].browse(self._context.get('active_id'))
        data.update({'name': self.name})
