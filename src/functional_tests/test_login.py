import os
import re
from pathlib import Path

from django.core import mail
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest

TEST_EMAIL = "edith@example.com"
SUBJECT = "Your login link for Superlists"
POP3_SERVER = "pop.mail.yahoo.com"
POP3_TIMEOUT = 60


class LoginTest(FunctionalTest):
    def retrieve_email_from_file(self, sent_to, subject, emails_dir):
        latest_emails_file = sorted(Path(emails_dir).iterdir())[-1]
        latest_email = latest_emails_file.read_text().split("-" * 80)[-1]
        self.assertIn(subject, latest_email)
        self.assertIn(sent_to, latest_email)
        return latest_email

    def retrieve_email_from_django_outbox(self, sent_to, subject):
        email = mail.outbox.pop()
        self.assertIn(sent_to, email.to)
        self.assertEqual(email.subject, subject)
        return email.body

    def wait_for_email(self, sent_to, subject):
        """
        Retrieve email body,
        from a file if the right env var is set,
        or get it from django.mail.outbox by default
        """
        if email_file_path := os.environ.get("EMAIL_FILE_PATH"):
            return self.wait_for(
                lambda: self.retrieve_email_from_file(sent_to, subject, email_file_path)
            )
        else:
            return self.retrieve_email_from_django_outbox(sent_to, subject)

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
        email_body = self.wait_for_email(TEST_EMAIL, SUBJECT)

        # It has a URL link in it
        self.assertIn("Use this link to log in", email_body)
        if not (url_search := re.search(r"http://.+/.+$", email_body, re.MULTILINE)):
            self.fail(f"Could not find url in email body:\n{email_body}")
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
