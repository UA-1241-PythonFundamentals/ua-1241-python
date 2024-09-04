from linguist import (
    user_create, user_get_by_id, user_update_name, user_change_password, user_delete_by_id,
    deck_create, deck_get_by_id, deck_update, deck_delete_by_id,
    card_create, card_get_by_id, card_filter, card_update, card_delete_by_id
)

# Test the User model
user = user_create('Alice', 'alice@example.com', 'password123')
assert user.name == 'Alice'
assert user.email == 'alice@example.com'

user_from_db = user_get_by_id(user.id)
assert user_from_db.name == 'Alice'

user_updated = user_update_name(user.id, 'Alice Updated')
assert user_updated.name == 'Alice Updated'

assert user_change_password(user.id, 'password123', 'newpassword123')
assert not user_change_password(user.id, 'wrongpassword', 'newpassword123')

assert user_delete_by_id(user.id)

# Test Deck and Card models
user = user_create('Bob', 'bob@example.com', 'password123')
deck = deck_create('My First Deck', user.id)
assert deck.name == 'My First Deck'

card = card_create(deck.id, 'hello', 'привіт', 'Greeting')
assert card.word == 'hello'
assert card.translation == 'привіт'

cards_filtered = card_filter('прив')
assert len(cards_filtered) == 1

card_updated = card_update(card.id, word='Hi', translation='привіт')
assert card_updated.word == 'Hi'

assert card_delete_by_id(card.id)
assert deck_delete_by_id(deck.id)
assert user_delete_by_id(user.id)
