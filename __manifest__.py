# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital Manager',
    'version': '1.0',
    'category': '',
    'sequence': 10,
    'summary': 'create odoo Hospital Managermodule and security',
    'description': "",
    'website': '',
    'depends': [
        'base',
        'mail',
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/patient.xml',


    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}