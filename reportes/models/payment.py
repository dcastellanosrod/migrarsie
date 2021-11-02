# -*- coding: utf-8 -*-

import base64
from odoo import models, fields, api, _
from datetime import datetime

from lxml import etree



class account_payment(models.Model):
    _inherit = "account.payment"


    clave_conf = fields.Char(string='Clave de Confirmación')
    fecha_pago = fields.Datetime(string='Fecha de Pago', default=datetime.today())

    @api.model
    def l10n_mx_edi_get_payment_data_etree(self, cfdi):
        '''Get the Complement node from the cfdi.
        :param cfdi: The cfdi as etree
        :return: the Payment node
        '''
        if not hasattr(cfdi, 'Complemento'):
            return None
        attribute = '//pago10:Pago'
        namespace = {'pago10': 'http://www.sat.gob.mx/Pagos'}
        node = cfdi.Complemento.xpath(attribute, namespaces=namespace)
        return node

class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    clave_conf = fields.Char(string='Clave de Confirmación')
    fecha_pago = fields.Datetime(string='Fecha de Pago', default=datetime.now().replace(hour=12,minute=0,second=0))

    def _prepare_payment_vals(self, invoice):
        res = super(AccountPaymentRegister, self)._prepare_payment_vals(invoice)
        res.update({
            'clave_conf': self.clave_conf,
            'fecha_pago': self.fecha_pago,
        })
        return res