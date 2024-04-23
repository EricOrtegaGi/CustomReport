# report.py
from odoo import models

class ReportSaleOrder(models.AbstractModel):
    _name = 'report.sale.report_saleorder'
    _description = 'Sales Order Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        return {
            'doc_ids': docs.ids,
            'doc_model': 'sale.order',
            'docs': docs,
            'num_articles': docs.num_articles,
            'preferred_email': docs.preferred_email,
        }