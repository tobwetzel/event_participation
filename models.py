# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Participant(models.Model):
    """
        Model of a participant. Is linked to a partner and an event.
        Contains information about track participation, meal type and participant type.
    """

    _name = 'event_participation.participant'

    partner_id = fields.Many2one('res.partner', string="Partner Reference", required=True)
    event_id = fields.Many2one('event.event', string="Participating in", required=True)
    tracks = fields.Many2many('event.track', string="Attending")
    type = fields.Many2one('event_participation.type', string="Is of type", required=True)
    meal = fields.Many2one('event_participation.meal_type', string="Chose to eat")


class MealType(models.Model):
    """
        Model that contains information about a meal type.
        A meal type is assigned to every participant.
    """
    _name = 'event_participation.meal_type'

    name = fields.Char(string="Name", required=True)
    event_id = fields.Many2one('event.event', string="Event")
    cost = fields.Float(string="Additional Cost")


class ParticipantType(models.Model):
    """
        Every participant is assigned a participant type.
    """
    _name = 'event_participation.type'

    name = fields.Char(required=True)