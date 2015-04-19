# -*- coding: utf-8 -*-
from openerp import models, fields


class CustomEvent(models.Model):
    """
        Class that inherits event.event to add variables
    """
    _inherit = "event.event"

    # add meal_types
    #meal_types = fields.One2many('event_participation.meal_type', 'event_id', string="Available Meals")