from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    num_articles = fields.Integer(string='Numero de articulos', compute='_compute_num_articles')
    preferred_email = fields.Char('Preferred Email')

    def _compute_num_articles(self):
        for order in self:
            order.num_articles = len(order.order_line)

    def action_view_report(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sales Order Report',
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'domain': [('id', '=', self.id)],
            'context': dict(self.env.context),
        }