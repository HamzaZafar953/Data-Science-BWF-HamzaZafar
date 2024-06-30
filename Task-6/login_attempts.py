class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.login_attempts = 0  
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


# Create an instance of User

user1 = User('Hamza Zafar', 'hamzazafar@example.com')


# Increment login attempts

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()


# Print the current value of login_attempts

print(f"Login attempts for {user1.username}: {user1.login_attempts}")


# Reset login attempts

user1.reset_login_attempts()


# Print login_attempts to verify it was reset to 0

print(f"After reset, login attempts for {user1.username}: {user1.login_attempts}")
