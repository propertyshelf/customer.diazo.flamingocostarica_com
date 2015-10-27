*** Settings ***

Resource  keywords.robot

Suite Setup  Setup
Suite Teardown  Teardown


*** Test cases ***

Show how to activate the add-on
    Enable autologin as  Manager
    Go to  ${PLONE_URL}/prefs_install_products_form
    Page should contain element  id=customer.diazo.flamingocostarica_com
    Assign id to element
    ...  xpath=//*[@id='customer.diazo.flamingocostarica_com']/parent::*
    ...  addons-customerdiazoflamingocostaricacom
    Assign id to element
    ...  xpath=//*[@id='customer.diazo.flamingocostarica_com']/ancestor::form
    ...  addons-enabled

    Highlight  addons-customerdiazoflamingocostaricacom
    Capture and crop page screenshot
    ...  setup_select_add_on.png
    ...  id=addons-enabled
