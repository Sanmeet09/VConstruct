from odoo import fields, api, models, _


class CustomerSubGroup(models.Model):
    _name = 'customer.sub.group'

    customer_sub = fields.Char('Customer Sub Group')
