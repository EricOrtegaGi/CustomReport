# report.py
from odoo import models


class ReportSaleOrder(models.AbstractModel):
    _name = 'report.sale.report_saleorder'
    _description = 'Sales Order Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        report_values = []
        for doc in docs:
            report_values.append({
                'doc_ids': doc.ids,
                'doc_model': 'sale.order',
                'docs': doc,
                'num_articles': doc.num_articles,
                'preferred_email': doc.preferred_email,
            })
        return report_values
