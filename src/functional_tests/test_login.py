import os
import poplib
import re
import time

from django.core import mail
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest

SUBJECT = "Your login link for Superlists"


class LoginTest(FunctionalTest):
    def wait_for_email(self, test_email, subject):
        if not self.test_server:
            email = mail.outbox.pop()
            self.assertIn(test_email, email.to)
            self.assertEqual(email.subject, subject)
            return email.body

        email_id = None
        start = time.time()
        inbox = poplib.POP3_SSL("pop.mail.yahoo.com")
        try:
            inbox.user(test_email)
            inbox.pass_(os.environ["YAHOO_PASSWORD"])
            while time.time() - start < 60:
                # get 10 newest messages
                count, _ = inbox.stat()
                for i in reversed(range(max(1, count - 10), count + 1)):
                    print("getting msg", i)
                    _, lines, __ = inbox.retr(i)
                    lines = [l.decode("utf8") for l in lines]
                    if f"Subject: {subject}" in lines:
                        email_id = i
                        body = "\n".join(lines)
                        return body
                time.sleep(5)
        finally:
            if email_id:
                inbox.dele(email_id)
            inbox.quit()

    def test_login_using_magic_link(self):
        # Edith goes to the awesome superlists site
        # and notices a "Log in" section in the navbar for the first time
        # It's telling her to enter her email address, so she does
        if self.test_server:
            test_email = "edith.testuser@yahoo.com"
        else:
            test_email = "edith@example.com"

        self.browser.get(self.live_server_url)
        self.browser.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys(
            test_email, Keys.ENTER
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
        self.browser.find_element(By.LINK_TEXT, "Log out").click()

        # She is logged out
        self.wait_to_be_logged_out(email=TEST_EMAIL)
