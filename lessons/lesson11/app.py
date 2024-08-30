# coding: utf_8

from models import Order, User


# Створення користувача
user1 = User("Ольга", "olga@example.com")


# Створення замовлення
order1 = Order(user1, "Смартфон", 2, 8000)

# Перевірка інформації про користувача та замовлення
print(user1.get_user_info())
print(order1.get_order_details())
user2 = User("Ольга", "olga2@example.com")
order2 = Order(user2, "Смартфон", 2, 8000)
user2.update_email("1515")
user2.update_email("1515@4.ua")
user2.update_email("test@test.ua")