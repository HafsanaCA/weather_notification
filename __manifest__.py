{
    'name': 'Weather Notification',
    'version': '1.0',
    'summary': 'This module will show a popup of weather when we click on the systray cloud icon.',
    'author': 'Hafsana CA',
    'depends': ['base'],
    'data': [

    ],
    'assets': {
        'web.assets_backend': [
            'weather_notification/static/src/js/systray_icon.js',
            'weather_notification/static/src/xml/systray_icon.xml',

        ]
    },

    'installable': True,
    'application': False,
}