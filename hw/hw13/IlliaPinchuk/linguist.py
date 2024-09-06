from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.exc import NoResultFound

Base = declarative_base()
engine = create_engine('sqlite:///linguist.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Models

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    decks = relationship('Deck', back_populates='user', cascade="all, delete")

class Deck(Base):
    __tablename__ = 'decks'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='decks')
    cards = relationship('Card', back_populates='deck', cascade="all, delete")

class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    tip = Column(String)
    deck_id = Column(Integer, ForeignKey('decks.id'), nullable=False)

    deck = relationship('Deck', back_populates='cards')


# Functions

# User functions
def user_create(name, email, password):
    """Creates a new user and returns the User object."""
    user = User(name=name, email=email, password=password)
    session.add(user)
    session.commit()
    return user

def user_get_by_id(user_id):
    """Retrieves a user by their ID and returns the User object."""
    return session.query(User).filter_by(id=user_id).first()

def user_update_name(user_id, name):
    """Updates the name of a user and returns the User object."""
    user = user_get_by_id(user_id)
    if user:
        user.name = name
        session.commit()
    return user

def user_change_password(user_id, old_password, new_password):
    """Changes the password of a user and returns a Boolean indicating success or failure."""
    user = user_get_by_id(user_id)
    if user and user.password == old_password:
        user.password = new_password
        session.commit()
        return True
    return False

def user_delete_by_id(user_id):
    """Deletes a user by their ID and returns a Boolean value indicating success or failure."""
    user = user_get_by_id(user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False


# Deck functions
def deck_create(name, user_id):
    """Creates a new deck belonging to a user and returns the Deck object."""
    deck = Deck(name=name, user_id=user_id)
    session.add(deck)
    session.commit()
    return deck

def deck_get_by_id(deck_id):
    """Retrieves a deck by its ID and returns the Deck object."""
    return session.query(Deck).filter_by(id=deck_id).first()

def deck_update(deck_id, name):
    """Updates the name of a deck and returns the Deck object."""
    deck = deck_get_by_id(deck_id)
    if deck:
        deck.name = name
        session.commit()
    return deck

def deck_delete_by_id(deck_id):
    """Deletes a deck by its ID and returns a Boolean value indicating success or failure."""
    deck = deck_get_by_id(deck_id)
    if deck:
        session.delete(deck)
        session.commit()
        return True
    return False


# Card functions
def card_create(deck_id, word, translation, tip):
    """Creates a new flashcard and returns the Card object."""
    card = Card(deck_id=deck_id, word=word, translation=translation, tip=tip)
    session.add(card)
    session.commit()
    return card

def card_get_by_id(card_id):
    """Retrieves a flashcard by its ID and returns the Card object."""
    return session.query(Card).filter_by(id=card_id).first()

def card_filter(sub_word):
    """Retrieves all flashcards containing a substring in either the word, translation, or tip."""
    return session.query(Card).filter(
        (Card.word.contains(sub_word)) | 
        (Card.translation.contains(sub_word)) | 
        (Card.tip.contains(sub_word))
    ).all()

def card_update(card_id, word=None, translation=None, tip=None):
    """Updates the fields of a flashcard and returns the Card object."""
    card = card_get_by_id(card_id)
    if card:
        if word:
            card.word = word
        if translation:
            card.translation = translation
        if tip:
            card.tip = tip
        session.commit()
    return card

def card_delete_by_id(card_id):
    """Deletes a flashcard by its ID and returns a Boolean value indicating success or failure."""
    card = card_get_by_id(card_id)
    if card:
        session.delete(card)
        session.commit()
        return True
    return False


if __name__ == '__main__':
    Base.metadata.create_all(engine)
