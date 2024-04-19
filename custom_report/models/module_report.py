from odoo import fields, models
from odoo import tools

class ModuleReport(models.Model):
    _name = 'custom.report'
    _description = "Module Report"
    #_rec_name = 'module_field'
    _auto = False
    
    total_price = fields.Float('Total Price', readonly=True)
    comercial = fields.Char('Comercial', readonly=True)
    state = fields.Char()   #fields.Selection([('New','En Tractament'),('OfferAccepted', 'Oferta Acceptada'),('Sold', 'Venuda'),('Canceled', 'Cancel·lada')],copy=False, readonly=True)
    
    
    def _select(self):
        return """
            SELECT SUM(epo.price) AS total_price, rp.name as comercial, ep.state, ep.id               
        """
    
    def _group_by(self):
        return """
            GROUP BY rp.name, ep.state
        """
        
    def _from(self):
        return """
            FROM estate_property ep
                LEFT JOIN res_users ru ON ep.salesperson_id = ru.id
                LEFT JOIN res_partner rp ON ru.partner_id = rp.id
                LEFT JOIN estate_property_offer epo ON ep.id = epo.property_id
        """

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
            SELECT
                %s
            FROM
                %s
            GROUP BY 
                %s
        )""" % (self._table, self._select(), self._from(), self._group_by())
    