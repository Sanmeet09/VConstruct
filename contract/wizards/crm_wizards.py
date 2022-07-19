from odoo import fields, models, api, _


class ManualApiWizards(models.TransientModel):
    _name = "manual.api.wizards"

    name = fields.Char(string="Name")
