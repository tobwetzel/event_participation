# -*- coding: utf-8 -*-
from openerp import http
from openerp.http import request
from openerp import SUPERUSER_ID
from openerp.addons.website_sale.controllers import main
import logging
import models

class EventParticipant(http.Controller):
    @http.route('/event_participation/information/', type='http', auth='public', website=True)
    def get_information(self, **post):
        cr, uid, context = request.cr, request.uid, request.context

        values = {}
        values["meals"] = {"Vegetarian": {"cost": 0.00}, "Vegan": {"cost", 20.00}, "Wheat/Gluten-free": {"cost": 10.50}}
        #values["tracks"] = [{"name": "security", "minitracks": [{"name": "cybersecurity", "date": "xyz", "duration": "5"}, "information security"]}, {"name": "social media", "minitracks": ["introduction", "blablabla"]}, {"name": "big data", "minitracks": ["analisys", "so cool"]}, {"name": "innovation", "minitracks": ["brand new"]}, {"name": "research", "minitracks": []}]

        values["tracks"] =  [{"name": "Security",
					"events_full_day": [{"name": "Rapid Screening Technologies, Deception, Detection and Credibility Assessment (2 days) (S) "}],
					"events_slots":[{"morning": "Cybersecurity in Action (S)", "afternoon": "information security"}]},
					{"name": "Big Data",
					"events_full_day": [{"name": "Real-Time Big Data Analytics (W)"}],
					"events_slots": [{"morning": "Introduction to Big Data and Its Technology (T)", "afternoon": "Big Data  Analytics (T)"},
									{"morning": "Introduction to Text Mining in Virtual Team Research (T)", "afternoon": "Visual Mining and Analysis of Social Media (T)"},
									{"morning": "", "afternoon": "Business Analytics and Big Data: Resources for Next Generation of Knowledge Workers (W)"}]},
					{"name": "Social Media & Networks",
					"events_full_day": [{"name": "Social Media Research: Tools and Methods / Results from Analyses of Social Media Data; Continuing Challenges (W)"}],
					"events_slots": [{"morning": "Introduction to Social Network Analysis (T)", "afternoon": "Collective Intelligence and Crowdsourcing (W)"},
									{"morning": "Community Systems Design (T)", "afternoon": "Cross Cultural Communication in Accessible Global Virtual Teams (W)"}]},
					{"name": "Innovation & Sustainability",
					"events_full_day": [{"name": "Emerging Technical Frontiers for Service Innovation (S)"},
                                        {"name": "Innovating Together: Co-creation and Co-production of Public Services (S)"},
                                        {"name": "Sustainable Energy and Computing (S)"}],
					"events_slots": [{"morning": "Information Technology and Innovation (S)", "afternoon": "Wireless Innovation and Services Beyond 2020 (W)"}]},
					{"name": "E-Health",
					"events_full_day": [{"name": "Learning Health Systems (1.5 days) (S)"}],
					"events_slots": []},
					{"name": "Teaching & Research Methods",
					"events_full_day": [],
					"events_slots":[{"morning": "Philosophy of Technology for Information Systems Scholars (T)", "afternoon": "Interaction Design for Specifying Business Requirements (T)"},
                                    {"morning": "Cloud Computing and Decision Analytics (T)", "afternoon": "Teaching with Tableau (W)"},
                                    {"morning": "Biomedical/Clinical Natural Language Processing (T)", "afternoon": "Get Your First Experience with Serious Games and Game Design Thinking"},
                                    {"morning": "Academic Integrity Research: Can We Change the Culture? (W)", "afternoon": "Design Science in Action: Exemplars from Information Systems Privacy Artifacts in IS Research (S)"},
									{"morning": "Writing Review and Meta-analysis Papers in Information Systems (W)", "afternoon": ""}]}
					]

        return request.website.render("event_participation.all_the_info", values)


class ExtendedSaleController(main.website_sale):

    @http.route(['/shop/checkout'], type='http', auth="public", website=True)
    def checkout(self, **post):

        _logger = logging.getLogger(__name__)
        _logger.debug("HELLO")
        _logger.debug(post)

        cr, uid, context = request.cr, request.uid, request.context

        order = request.website.sale_get_order(force_create=1, context=context)

        _logger.debug(order.product_id.event_ticket_ids.event_id)

        if order.product_id.event_ticket_ids.event_id:
            _logger.debug("is event ticket")

            if post.has_key("has_participation_information"):

                has_participation_info = post["has_participation_information"]

                if has_participation_info:
                    _logger.debug("has participation info")
                    return super(ExtendedSaleController, self).checkout()
            else:
                _logger.debug("has no participation info")
                return request.redirect("/event_participation/information")

        else:
            return super(ExtendedSaleController, self).checkout()

    def checkout_values(self, data=None):

        _logger = logging.getLogger(__name__)

        if not data:

            cr, uid, context, registry = request.cr, request.uid, request.context, request.registry

            values = super(ExtendedSaleController, self).checkout_values()

            #orm_meals = registry.get('event_participation.meal_type')
            #_logger.debug(orm_meals)

            #track_obj = request.registry.get('event.event')
            #track = track_obj.browse(request.cr, SUPERUSER_ID, track.id, context=request.context)

            #meal_ids = orm_meals.search(cr, SUPERUSER_ID, [], context=context)
            #_logger.debug(meal_ids)
            #meals = orm_meals.browse(cr, SUPERUSER_ID, meal_ids, context)
            #_logger.debug(meals)

            #meal = models.Participant()
            #_logger.debug(meal)

            #meal = models.ParticipantType()
            #_logger.debug(meal)

            #meal = models.MealType()
            #_logger.debug(meal)
            #meals = models.MealType.get_all_meal_types(self)
            #meals = models.MealType.search([])
            #_logger.debug(meal.get_all_meal_types())
            #meals = meal.search([])
            #_logger.debug(meals)

            #values["meals"] = registry['event_participation.meal_type'].search([])

            values["meals"] = {"normal": {"cost": 0.00}, "vegan": {"cost", 20.00}, "diet": {"cost": 10.50}}
            values["tracks"] = [{"name": "security", "minitracks": [{"name": "cybersecurity", "date": "xyz", "duration": "5"}, "information security"]}, {"name": "social media", "minitracks": ["introduction", "blablabla"]}, {"name": "big data", "minitracks": ["analisys", "so cool"]}, {"name": "innovation", "minitracks": ["brand new"]}, {"name": "research", "minitracks": []}]
            #values["tracks"] = {"security": {"minitracks": ["cybersecurity", "information security", ]}, "social media": {}, "big data": {}, "innovation": {}, "research": {}}

            return values

        else:
            return super(ExtendedSaleController, self).checkout_values()

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