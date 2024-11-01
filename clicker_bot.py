import pyautogui
import time
import random
import requests

# List of URLs for different question databases

question_databases = [
    "https://opentdb.com/api.php?amount=1&category=18&type=multiple",  # Science: Computers
    "https://opentdb.com/api.php?amount=1&category=9&type=multiple",   # General Knowledge
    "https://opentdb.com/api.php?amount=1&category=10&type=multiple",  # Entertainment: Books
    "https://opentdb.com/api.php?amount=1&category=11&type=multiple",  # Entertainment: Film
    "https://opentdb.com/api.php?amount=1&category=12&type=multiple",  # Entertainment: Music
    "https://opentdb.com/api.php?amount=1&category=17&type=multiple",  # Science & Nature
    "https://opentdb.com/api.php?amount=1&category=21&type=multiple",  # Sports
    "https://opentdb.com/api.php?amount=1&category=22&type=multiple",  # Geography
    "https://opentdb.com/api.php?amount=1&category=23&type=multiple",  # History
    "https://opentdb.com/api.php?amount=1&category=24&type=multiple",  # Politics
    "https://opentdb.com/api.php?amount=1&category=25&type=multiple",  # Art
    "https://opentdb.com/api.php?amount=1&category=26&type=multiple",  # Celebrities
    "https://opentdb.com/api.php?amount=1&category=27&type=multiple",  # Animals
    "https://opentdb.com/api.php?amount=1&category=28&type=multiple",  # Vehicles
    "https://opentdb.com/api.php?amount=1&category=29&type=multiple",  # Entertainment: Comics
    "https://opentdb.com/api.php?amount=1&category=30&type=multiple",  # Science: Gadgets
    "https://opentdb.com/api.php?amount=1&category=31&type=multiple",  # Entertainment: Japanese Anime & Manga
    "https://opentdb.com/api.php?amount=1&category=32&type=multiple",  # Entertainment: Cartoon & Animations
]

# Function to get a random interval between 5 to 20 minutes
def get_random_interval():
    interval = random.randint(60, 750)
    print(f"New interval: {interval} seconds")
    return interval

# Function to get a programming-related question from a random database
def get_random_code_question():
    try:
        # Select a random database URL
        selected_url = random.choice(question_databases)
        response = requests.get(selected_url)
        if response.status_code == 200:
            question_data = response.json()
            question = question_data['results'][0]['question']
            options = question_data['results'][0]['incorrect_answers'] + [question_data['results'][0]['correct_answer']]
            random.shuffle(options)
            return f"{question} Options: {', '.join(options)}"
        else:
            return "Could not retrieve a question at this time."
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Initial random interval
message_interval = get_random_interval()
last_message_time = time.time()

while True:
    # Get the current mouse position
    x, y = pyautogui.position()
    print(f"Mouse position: ({x}, {y})")
    
    # Click at the current mouse position
    pyautogui.click(x, y)
    print("Clicked at current mouse position")
    
    # Check if it's time to send the question
    current_time = time.time()
    if current_time - last_message_time >= message_interval:
        # Get a random code-related question from a random database
        question = get_random_code_question()
        print(f"Generated question: {question}")
        
        # Type the question
        pyautogui.typewrite(question)
        print(f"Typed question: {question}")
        
        # Press Enter to send the question
        pyautogui.press('enter')
        print("Pressed Enter")
        
        # Update the last message time and get a new random interval
        last_message_time = current_time
        message_interval = get_random_interval()
    
    # Wait for 30 seconds before the next click
    time.sleep(30)
    print("Sleeping for 30 seconds")


    