{
    'name': 'FSMA Compliance',
    'category': 'PCQI',
    "version": "11.0.0.0.1",
    'author': 'Teqbeat',
    'description': """
    
    """,
    'depends': ['stock', 'purchase', 'sale', 'base'],
    'data': [
        'data/fsma_sequence_data.xml',

        'data/stock_sequence_data.xml',
        'data/stock_location_data.xml',

        'security/fsma_compliance_security.xml',
        'security/ir.model.access.csv',

        'report/inventory_report_views.xml',
        'report/csa_inbound_report.xml',
        'report/csa_outbound_report.xml',
        'report/hold_pallet_report.xml',

        'report/quality_report_views.xml',
        'report/foreign_material_report.xml',
        'report/lab_submission_report.xml',
        'report/production_daily_operation_report.xml',
        'report/production_pre_operation_report.xml',
        'report/restroom_maintenance_log_report.xml',
        'report/ssop_operational_checklist_report.xml',
        'report/supplier_management_report.xml',
        'report/lab_pallet_tags_report.xml',

        'views/production_pre_operation_view.xml',
        'views/restroom_maintenance_view.xml',
        'views/ssop_op_check_view.xml',
        'views/production_daily_operation.xml',
        'views/supplier_management_view.xml',
        'views/foreign_material_view.xml',
        'views/lab_submission_form_view.xml',
        'views/res_partner_adj_view.xml',

        'views/product_adj_view.xml',
        'views/stock_move_line_adj_view.xml',
        'views/stock_picking_adj_view.xml',
        'views/mrp_production_adj_view.xml',
        'views/production_adj_lot_view.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
