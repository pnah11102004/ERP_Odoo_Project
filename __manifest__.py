{
    'name': 'Báo cáo đơn hàng - tồn kho - v2',
    'version': '2.13',
    'description': """
        - Màn hình Thống kê Đơn hàng: Xem đơn hàng với các bộ lọc (trạng thái, thời gian, sản phẩm, khách hàng và thành phố) và biểu đồ thống kê.
        - Màn hình Báo cáo Tồn kho: Xem số lượng sản phẩm còn lại trong kho.
    """,
    'summary': """
        Module cung cấp màn hình thống kê đơn hàng và báo cáo tồn kho.
    """,
    'author': 'LamTuanThinh22521408',
    'website': '',
    'category': 'Reporting',
    'depends': ['sale_management', 'stock', 'board', 'uom'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_statistics_views.xml',
        'views/inventory_report_views.xml',
        'views/report_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
