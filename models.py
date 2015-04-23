# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ExtendedRegistration(models.Model):
    _inherit = "event.registration"

    track_ids = fields.Many2many('event.track', string="Attending")


class ExtendedTrack(models.Model):
    _inherit = "event.track"

    attendees = fields.Many2many('event.registration', string="Attending")


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
    #meal = fields.Many2one('event_participation.meal_type', string="Chose to eat")


#class MealType(models.Model):
    #_name = 'event_participation.meal_type'

    #name = fields.Char(string="Name", required=True)
    #event_id = fields.Many2one('event.event', string="Event")
    #cost = fields.Float(string="Additional Cost")

    #def get(self):
        #return self

    #def get_all_meal_types(self):
        #return self.search([])

    #def get_meal_types_for_event(self, event_id):
        #return self.search("event_id", "=", event_id)


class ParticipantType(models.Model):
    """
        Every participant is assigned a participant type.
    """
    _name = 'event_participation.participant_type'

    name = fields.Char(required=True)