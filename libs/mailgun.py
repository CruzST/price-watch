# Due to costs, In order to actually send an email, the recipient MUST be an approved email on mailgun.

from requests import Response, post
import os
from typing import List


class MailgunException(Exception):
    def __init__(self, message: str):
        self.message = message


class Mailgun:
    FROM_TITLE = "Price Watch Application"
    FROM_EMAIL = "do-not-reply@sandbox55caaad532764badbde2b727ec98c0cd.mailgun.org"

    @classmethod
    def send_mail(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        api_key = os.environ.get('MAILGUN_API_KEY', None)
        mailgun_domain = os.environ.get('MAILGUN_DOMAIN', None)

        if api_key is None:
            raise MailgunException('Failed to load mailgun API key.')
        if mailgun_domain is None:
            raise MailgunException('Failed to load mailgun Domain.')

        response = post(
            f"{mailgun_domain}/messages",
            auth=("api", api_key),
            data={"from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                  "to": email,
                  "subject": subject,
                  "text": text,
                  "html": html})
        if response.status_code != 200:
            print(response.json())
            raise MailgunException('An error occurred while sending email')
        return response
