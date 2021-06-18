from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jsm.pages.agent_pages import Login
from util.conf import JSM_SETTINGS


def app_specific_action_log_level_web_action(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_agent_app_custom_action_log_level_web_action")
    def measure():
        @print_timing("selenium_agent_app_custom_action:log_level_web_action")
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/secure/LogLevel.jspa")
            page.wait_until_visible((By.ID, "log-level-main-panel"))

        sub_measure()

    measure()


def app_specific_action_customer_issues_history_panel_web_action(webdriver, datasets):
    page = BasePage(webdriver)
    if datasets['custom_issues']:
        issue_key = datasets['custom_issue_key']

    @print_timing("selenium_agent_app_custom_action_customer_issues_history_panel_web_action")
    def measure():
        @print_timing("selenium_agent_app_custom_action:customer_issues_history_panel_web_action")
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/browse/CAOERVMVED-6")
            page.wait_until_visible((By.ID, "tcfj-twitter-tickets_heading"))

        sub_measure()

    measure()


def app_specific_action_link_twitter_account_web_action(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_agent_app_custom_action_link_twitter_account_web_action")
    def measure():
        @print_timing("selenium_agent_app_custom_action:link_twitter_account_web_action")
        def sub_measure():
            page.go_to_url(f"{JSM_SETTINGS.server_url}/secure/TwitterAccountWebAction.jspa?projectKey=CAOERVMVED")
            page.wait_until_visible((By.ID, "link-twitter-account-container"))

        sub_measure()

    measure()
