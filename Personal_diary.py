import sqlite3
import bcrypt
from datetime import datetime
# Connect to SQLite database (or create it)
conn = sqlite3.connect("personal_diary.db")
cursor = conn.cursor()

# Create users and diary_entries tables if they don't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS diary_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    entry TEXT,
    date TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
''')
conn.commit()

# Function to hash the password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Function to check the password
def check_password(hashed, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed)

# Function to sign up a new user
def sign_up():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    hashed_password = hash_password(password)
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please try again.")

# Function to log in a user
def log_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    if user and check_password(user[1], password):
        print("Logged in successfully!")
        return user[0]  # Return user_id
    else:
        print("Invalid username or password.")
        return None

# Function to add a new diary entry
def add_entry(user_id):
    entry = input("Write your diary entry: ")
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO diary_entries (user_id, entry, date) VALUES (?, ?, ?)", (user_id, entry, date_str))
    conn.commit()
    print("Entry added successfully!")

# Function to view all diary entries for the logged-in user
def view_entries(user_id):
    cursor.execute("SELECT date, entry FROM diary_entries WHERE user_id = ?", (user_id,))
    entries = cursor.fetchall()
    
    if entries:
        print("\n--- Your Diary Entries ---\n")
        for date, entry in entries:
            print(f"{date}\n{entry}\n")
    else:
        print("No entries found!")

# Main function to handle user choices
def main():
    print("Welcome to the Personal Diary App!")
    
    while True:
        print("\n1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == "1":
            sign_up()
        elif choice == "2":
            user_id = log_in()
            if user_id:
                while True:
                    print("\n1. Write a new entry")
                    print("2. View all entries")
                    print("3. Log Out")
                    
                    user_choice = input("Choose an option (1/2/3): ")
                    
                    if user_choice == "1":
                        add_entry(user_id)
                    elif user_choice == "2":
                        view_entries(user_id)
                    elif user_choice == "3":
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

# Close the database connection when done
conn.close()
