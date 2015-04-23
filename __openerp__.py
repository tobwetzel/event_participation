# -*- coding: utf-8 -*-
{
    'name': "Event Participation",

    'summary': """
        Adds participation information on event registrations""",

    'description': """
        This modul introduces participants. A participant is a partner that has registered for an event.
        A participant contains the following information:
            - link to user
            - link to event
            - type of participant (speaker, visitor...)
            - type of meal (normal, vegan...)
            - details about track participation
    """,

    'author': "Tobias Wetzel",
    'website': "https://github.com/tobwetzel/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'event',
                'website_event_track'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'static/src/xml/templates.xml',
        'static/src/xml/register_form.xml',
        'views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}