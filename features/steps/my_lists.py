from behave import given, when, then
from functional_tests.management.commands.create_session import \
    create_pre_authenticated_session
from django.conf import settings


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

