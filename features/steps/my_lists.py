from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from django.conf import settings

from functional_tests.base import wait
from functional_tests.management.commands.create_session import \
    create_pre_authenticated_session


@wait
def wait_for_list_item(context, item_text):
    context.test.assertIn(
        item_text,
        context.browser.find_element_by_css_selector('#id_list_table').text
    )


@given('I am a logged-in user')
def given_i_am_logged_in(context):
    session_key = create_pre_authenticated_session(email='edith@example.com')
    ## to set a cookie we need to first visit the domain.
    ## 404 pages load the quickest!
    context.browser.get(context.get_url("/404_no_such_url/"))
    context.browser.add_cookie(dict(
        name=settings.SESSION_COOKIE_NAME,
        value=session_key,
        path='/',
    ))


@when('I create a list with first item "{first_item_text}"')
def create_a_list(context, first_item_text):
    context.browser.get(context.get_url('/'))
    context.browser.find_element_by_id('id_text').send_keys(first_item_text)
    context.browser.find_element_by_id('id_text').send_keys(Keys.ENTER)
    wait_for_list_item(context, first_item_text)


@when('I add an item "{item_text}"')
def add_an_item(context, item_text):
    context.browser.find_element_by_id('id_text').send_keys(item_text)
    context.browser.find_element_by_id('id_text').send_keys(Keys.ENTER)
    wait_for_list_item(context, item_text)


@then('I will see a link to "{link_text}"')
@wait
def see_a_link(context, link_text):
    context.browser.find_element_by_link_text(link_text)


@when('I click the link to "{link_text}"')
def click_link(context, link_text):
    context.browser.find_element_by_link_text(link_text).click()
