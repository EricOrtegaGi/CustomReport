from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_items = fields.Integer(compute='_compute_total_items', string='Nombre d\'articles', readonly=True)
    preferred_email = fields.Char(string='Correu Preferencial')

    @api.depends('order_line')
    def _compute_total_items(self):
        for order in self:
            order.total_items = sum(line.product_uom_qty for line in order.order_line)
