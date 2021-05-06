import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


# def app_specific_action_auto_update_configuration(webdriver, datasets):
#     page = BasePage(webdriver)
#
#     @print_timing("selenium_app_custom_action_auto_update_configuration")
#     def measure():
#         page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/admin/ftp")
#         page.wait_until_visible((By.ID, "admin"))
#     measure()


def app_specific_action_language_configuration(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_language_configuration")
    def measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/admin/resx")
        page.wait_until_visible((By.ID, "lang-config-title-body"))
    measure()


def app_specific_action_otj_client(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action_otj_client")
    def measure():
        page.go_to_url(f"{JIRA_SETTINGS.server_url}/secure/AdminOutlook.jspa")
        page.wait_until_visible((By.ID, "download-button"))
    measure()


