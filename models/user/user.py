import uuid
from dataclasses import dataclass, field
from typing import Dict, List

from flask import flash, redirect, url_for

from models.model import Model
import models.user.errors as UserErrors
from common.utils import Utils


@dataclass
class User(Model):
    collection: str = field(init=False, default='users')
    email: str
    password: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    @classmethod
    def find_by_email(cls, email: str) -> "User":
        try:
            return cls.find_one_by('email', email)
        except TypeError:
            raise UserErrors.UserNotFoundError('A user with this email was not found.')

    # Password will be hashed using the passlib module in the common file.
    @classmethod
    def register_user(cls, email: str, password: str) -> bool:
        if not Utils.email_is_valid(email):
            # This shouldn't really be called because the form validation should catch if it is an email type
            raise UserErrors.InvalidEmailError('The email does not have the right format.')
        try:
            cls.find_by_email(email)
            raise UserErrors.UserAlreadyRegisteredError('The registering email already exists.')
        except UserErrors.UserNotFoundError:
            User(email, Utils.hash_password(password)).save_to_mongo()

        return True

    @classmethod
    def is_login_valid(cls, email: str, password: str) -> bool:
        user = cls.find_by_email(email)

        if not Utils.check_hashed_password(password, user.password):
            raise UserErrors.IncorrectPasswordError('Password was incorrect!')

        return True

    def json(self) -> Dict:
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password
        }