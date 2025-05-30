{
    'name': 'Weather Notification',
    'version': '1.0',
    'summary': """ The User Weather Notification Odoo app is an extension module 
     that integrates weather forecasting functionality into the Odoo ERP 
     system """,
    'author': 'Hafsana CA',
    'depends': ['web'],
    'data': [
            'views/res_users_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'weather_notification/static/src/js/systray_icon.js',
            'weather_notification/static/src/xml/systray_icon.xml',
        ]
    },
    'external_dependencies': {
            'python': ['geocoder'],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
