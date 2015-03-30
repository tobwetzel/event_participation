# -*- coding: utf-8 -*-
from openerp import http
from openerp.http import request

class EventParticipant(http.Controller):
    @http.route('/event_participant/information/', type='http', auth='public', website=True)
    def get_information(self, **post):
        cr, uid, context = request.cr, request.uid, request.context
        return request.website.render("website_sale.checkout")

#     @http.route('/event_participant/event_participant/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_participant.listing', {
#             'root': '/event_participant/event_participant',
#             'objects': http.request.env['event_participant.event_participant'].search([]),
#         })

#     @http.route('/event_participant/event_participant/objects/<model("event_participant.event_participant"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_participant.object', {
#             'object': obj
#         })