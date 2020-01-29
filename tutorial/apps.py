# -*- coding: utf-8 -*-
"""
App configuration for the Tutorials app.
"""
from django.apps import AppConfig


class TutorialConfig(AppConfig):
    """
    Tutorial app config.
    """
    name = 'tutorial'

    def ready(self):
        from .quickstart import signals
