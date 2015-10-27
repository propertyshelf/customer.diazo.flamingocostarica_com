# -*- coding: utf-8 -*-
"""Post install import steps for customer.diazo.flamingocostarica_com."""


def is_not_current_profile(context):
    return context.readDataFile(
        'customerdiazoflamingocostaricacom_marker.txt'
    ) is None


def post_install(context):
    """Post install script."""
    if is_not_current_profile(context):
        return
    # Do something during the installation of this package
