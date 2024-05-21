{
    "name": "Sale Order Custom",
    "version": "1.0",
    "author": "Eric Ortega",
    "application": True,
    "depends": ["base", "sale"],
    "data": [
        "views/sale_order_views.xml",
        "views/sale_order_menus.xml",
        "reports/report_sale_order_custom.xml",
        "reports/sale_order_report_extension.xml",
        "security/ir.model.access.csv",
        "reports/sale_order_reports.xml"
    ],
    "installable": True,
    'license': 'LGPL-3',
}