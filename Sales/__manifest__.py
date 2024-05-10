{
    'name': 'Modulo de ventas personalizado',
    'application': True,
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Personalizacion del modulo de ventas',
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
        'views/custom_sale_order_view.xml',
        'views/report_saleorder_document.xml',
    ],
    'installable': True,
}
