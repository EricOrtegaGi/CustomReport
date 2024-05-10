from odoo import api, fields, models
from odoo import tools


class SalesModuleReport(models.Model):
    _name = 'sales.module.report'
    _description = "Sales Module Report"
    _auto = False

    num_articles = fields.Integer('Numero de articulos', readonly=True)
    preferred_email = fields.Char('Preferred Email', readonly=True)

    def print_report(self):
        return self.env.ref('custom_report.report_template').report_action(self)

    def _select(self):
        return """
            SELECT
                so.id,
                COUNT(sol.id) AS num_articles,
                rp.email AS preferred_email
        """

    def _from(self):
        return """
            FROM sale_order so
            JOIN sale_order_line sol ON so.id = sol.order_id
            JOIN res_partner rp ON so.partner_id = rp.id
        """

    def _group_by(self):
        return """
            GROUP BY so.id, rp.email
        """

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""
            CREATE or REPLACE VIEW %s as (
                %s
                %s
                %s
            )
        """ % (self._table, self._select(), self._from(), self._group_by()))