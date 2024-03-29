# -*- coding: utf-8 -*-
{
    'name': "Formatos CFDI",

    'description': """
        Modifica formatos de factura 3.3 y recibo electronico de pago.
    """,

    'author': "SIE Center / Angeles Gervacio",
    'website': "http://www.siecenter.com.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
   
    'version': '15.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','l10n_mx_edi'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/payment.xml',
        'views/account_move.xml',
        'views/account_payment_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
