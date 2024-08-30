import uuid

class User:
    def __init__(self, username, email, password):
        self.user_id = uuid.uuid4()  # Generate a unique ID
        self.username = username
        self.email = email
        self.password = password  # In practice, never store plain text passwords

    def __str__(self):
        return f"User(id={self.user_id}, username={self.username}, email={self.email})"
    def __repr__(self):
        return f"({self.user_id}, {self.email})"

    def to_dict(self):
        """Convert the User object to a dictionary."""
        return {
            'user_id': str(self.user_id),  # Convert UUID to string
            'username': self.username,
            'email': self.email,
            'password': self.password
        }


# Generate ten users
USERS = []
for i in range(10):
    username = f"user_{i+1}"
    email = f"user_{i+1}@example.com"
    password = f"password{i+1}"
    user = User(username, email, password)
    USERS.append(user)


if __name__ == '__main__':
    # Display generated users
    for user in USERS:
        print(user)
