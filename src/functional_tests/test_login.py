import os
import poplib
import re
import time

from django.core import mail
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest

TEST_EMAIL = "edith@example.com"
SUBJECT = "Your login link for Superlists"
POP3_SERVER = "pop.mail.yahoo.com"
POP3_TIMEOUT = 60


def retrieve_pop3_email(receiver_email, subject, pop3_server, pop3_password):
    email_id = None
    start = time.time()
    inbox = poplib.POP3_SSL(pop3_server)
    try:
        breakpoint()
        inbox.user(receiver_email)
        inbox.pass_(pop3_password)
        while time.time() - start < POP3_TIMEOUT:
            # get 10 newest messages
            count, _ = inbox.stat()
            for i in reversed(range(max(1, count - 10), count + 1)):
                print("getting msg", i)
                _, lines, __ = inbox.retr(i)
                lines = [l.decode("utf8") for l in lines]
                print(lines)
                if f"Subject: {subject}" in lines:
                    email_id = i
                    body = "\n".join(lines)
                    return body
            time.sleep(5)
    finally:
        if email_id:
            inbox.dele(email_id)
        inbox.quit()


class LoginTest(FunctionalTest):
    def test_login_using_magic_link(self):
        # Edith goes to the awesome superlists site
        # and notices a "Log in" section in the navbar for the first time
        # It's telling her to enter her email address, so she does
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys(
            TEST_EMAIL, Keys.ENTER
        )

        # A message appears telling her an email has been sent
        self.wait_for(
            lambda: self.assertIn(
                "Check your email",
                self.browser.find_element(By.CSS_SELECTOR, "body").text,
            )
        )

        # She checks her email and finds a message
        email = mail.outbox.pop()
        self.assertIn(TEST_EMAIL, email.to)
        self.assertEqual(email.subject, SUBJECT)

        # It has a URL link in it
        self.assertIn("Use this link to log in", email.body)
        url_search = re.search(r"http://.+/.+$", email.body)
        if not url_search:
            self.fail(f"Could not find url in email body:\n{email.body}")
        url = url_search.group(0)
        self.assertIn(self.live_server_url, url)

        # she clicks it
        self.browser.get(url)

        # she is logged in!
        self.wait_to_be_logged_in(email=TEST_EMAIL)

        # Now she logs out
        self.browser.find_element(By.CSS_SELECTOR, "#id_logout").click()

        # She is logged out
        self.wait_to_be_logged_out(email=TEST_EMAIL)
