# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Contract',
    'version': '1.1',
    'summary': 'Contract',
    'sequence': 10,
    'description': """ """,
    'category': '',
    'website': 'https://www.odoo.com/app/',
    'depends': ["base", "crm", "sale", "project", 'mail', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/crm_wizards.xml',
        'views/contract_project_view.xml',
        'views/inherit_crm_view.xml',
        'views/non_dpr_view.xml',
        'views/customer_bu_view.xml',
        'views/sale_order_inherit.xml',
        'views/project_project_inherit.xml',
        'views/manual_leads.xml',
        'views/customer_sub_group.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
