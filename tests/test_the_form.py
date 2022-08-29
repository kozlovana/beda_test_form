import allure
import time
from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium.webdriver import Keys
from .attach import add_screenshots, add_logs, add_html


def test_fill_form():
    with allure.step("Open browser page"):
        browser.open('https://sdc.beda.software/#/demo-1').driver.maximize_window()

    with allure.step("Choose Questionnaire and launch Patient"):
        # Open Menu control
        menu_control = s('[class^=Menu_control]')
        menu_control.click()

        # Fill Questionnaire container
        questionnaire_dropdown_container = s('[class^="Menu_reactResourceSelect"]')
        questionnaire_dropdown_input = questionnaire_dropdown_container.element('input')
        questionnaire_dropdown_value_element = questionnaire_dropdown_container.element("[class$=singleValue]")

        questionnaire_dropdown_input.type('demo-3').press_tab()

        questionnaire_dropdown_value_element.should(have.text('demo-3'))
        time.sleep(4)

        # Fill LaunchPatient container
        launch_patient_dropdown_container = s('[class^="ResourceSelect_reactResourceSelect"]')
        launch_patient_dropdown_input = launch_patient_dropdown_container.element('input')
        launch_patient_dropdown_value_element = launch_patient_dropdown_container.element("[class$=singleValue]")

        launch_patient_dropdown_input.type('patient-2')
        time.sleep(2)
        launch_patient_dropdown_input.press_tab()

        launch_patient_dropdown_value_element.should(have.text('patient-2'))

        # Click Apply Config button
        apply_config_button = s("[class*=Menu_submitButton]")
        apply_config_button.click()
        time.sleep(5)

    with allure.step("Insert name"):
        first_name_input = s('[name^="Demographics.items.first-name"]')
        first_name_input.click()
        first_name_input.send_keys(Keys.COMMAND + "a")
        first_name_input.send_keys(Keys.BACKSPACE)
        first_name_input.type('Anna')
        time.sleep(2)

        middle_name_input = s('[name^="Demographics.items.middle-name"]')
        middle_name_input.click()
        middle_name_input.send_keys(Keys.COMMAND + "a")
        middle_name_input.send_keys(Keys.BACKSPACE)
        middle_name_input.type('Elisabeth')
        time.sleep(2)

        last_name_input = s('[name^="Demographics.items.last-name"]')
        last_name_input.click()
        last_name_input.send_keys(Keys.COMMAND + "a")
        last_name_input.send_keys(Keys.BACKSPACE)
        last_name_input.type('Johnson').press_tab()
        time.sleep(2)

        # Click Apply button
        apply_button = s("[class*=app-button]")
        apply_button.click()
        time.sleep(8)

    with allure.step("Check new name"):
        # Open Menu Control
        menu_control.click()

        # Check containers
        questionnaire_dropdown_value_element.should(have.text('demo-3'))
        launch_patient_dropdown_value_element.should(have.text('patient-2'))
        time.sleep(3)

        # Close Menu Control
        menu_control.click()

        # Check names
        first_name_input.should(have.value('Anna'))
        middle_name_input.should(have.value('Elisabeth'))
        last_name_input.should(have.value('Johnson'))

    add_screenshots(browser)
    add_logs(browser)
    add_html(browser)
