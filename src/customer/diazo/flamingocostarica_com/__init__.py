# -*- coding: utf-8 -*-
"""Propertyshelf Flamingo Costa Rica Theme."""

# python imports
import logging

# zope imports
from zope.i18nmessageid import MessageFactory

# local imports
from customer.diazo.flamingocostarica_com import config

logger = logging.getLogger(config.PROJECT_NAME)
_ = MessageFactory('customer.diazo.flamingocostarica_com')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
