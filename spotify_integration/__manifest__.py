# -*- coding: utf-8 -*-
{
    'name': "Spotify Integration",

    'summary': """Spotify integration with odoo""",

    'description': """ 
    Spotify integration with odoo version 14
    """,

    'author': "Juanca Perdomo",
    'website': "",

    'category': 'Specific Industry Applications',

    'version': '1.0',

    'application': False,
    'depends': ['base', ],
    'data': [
        'security/ir.model.access.csv',
        'data/musical_genres_data.xml',
        'views/spotify_views.xml',
        'views/menu_items.xml',

    ],
}
