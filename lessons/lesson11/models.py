# coding: utf_8
import re

from loger_config import logging

def validate_email(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        logging.info(f"create User {self.get_user_info()}")

    def update_email(self, new_email):
        if validate_email(new_email):
            logging.error(f"email is not valid {new_email}")
        else:
            msg = f"update email User {self.get_user_info()}"
            self.email = new_email
            msg += f"to {new_email}"
            logging.info(msg)

    def get_user_info(self):
        return f"user: {self.name}, Email: {self.email}"
    

class Order:
    def __init__(self, user, product, quantity, price_per_unit):
        self.user = user
        self.product = product
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        logging.info(f"create Order {self.get_order_details()}")
    
    def get_total_price(self):
        return self.quantity * self.price_per_unit
    
    def get_order_details(self):
        return f"Користувач: {self.user.name}, Товар: {self.product}, Кількість: {self.quantity}, Загальна вартість: {self.get_total_price()} грн"