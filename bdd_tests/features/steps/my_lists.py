from behave import given, when, then
from functional_tests.management.commands.create_session import create_pre_authenticated_session
from django.conf import settings
HOME = "http://localhost:8081"


@given('I am a logged-in user')
def given_i_am_logged_in(context):
    session_key = create_pre_authenticated_session(email='edith@example.com')
    ## to set a cookie we need to first visit the domain.
    ## 404 pages load the quickest!
    context.browser.get(context.server_url + "/404_no_such_url/")
    context.browser.add_cookie(dict(
        name=settings.SESSION_COOKIE_NAME,
        value=session_key,
        path='/',
    ))


@when('I create a list with first item "{first_item_text}"')
def create_a_list(context, first_item_text):
    context.browser.get(context.server_url)
    context.browser.find_element_by_id('id_text').send_keys(first_item_text)
    context.browser.find_element_by_id('id_text').send_keys('\n')


@when('I add an item "Immanentize Eschaton"')
def step_impl(context):
    assert False

@when('I create a list with first item "Buy milk"')
def step_impl(context):
    assert False

@then('I will see a link to "My lists"')
def step_impl(context):
    assert False

@when('I click the link to "My lists"')
def step_impl(context):
    assert False

@then('I will see a link to "Reticulate Splines"')
def step_impl(context):
    assert False

@then('I will see a link to "Buy milk"')
def step_impl(context):
    assert False

@when('I click the link to "Reticulate Splines"')
def step_impl(context):
    assert False

@then('I will be on the "Reticulate Splines" list page')
def step_impl(context):
    assert False
