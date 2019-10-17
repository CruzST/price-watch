# price-watch

## Pre-loaded users
user1@fakemail.com | 1234

thenewguy@gmail.com | 1234

## About
Application to practice use of Python and flask. The price watch application allows users to create an account and add/remove alerts for products from approved websites. Users simply copy and paste a link with the item they want to monitor and the price limit of their choice.

The prices are extracred from the webpage using beautifulSoup4.  An admin account is used to add/removed stores from the list.  Adding a store to the list requires some knowledge of a browsers html inspector.  As a note, some websites don't allow for parsing.

When the alert.py file is run, users where their prices have been reached will be emailed via mailgun.  (Due to mailgun constraints, the user emails provided are not real and therefore cannot receive emails as emails must be pre approved on the mailgun account).

All information is stored on a mongoDB cloud, queries to the database are made using pymongo.  The front-end was created with jinja2. User passwords are stored as a hash in the database using passlib.
