from nicegui import ui
import datetime
import random

# Function to show the current date and time
def show_datetime():
    now = datetime.datetime.now()
    ui.notify(f'Current Date and Time: {now.strftime("%Y-%m-%d %H:%M:%S")}')

# Function to share a joke
def tell_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts!",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    joke = random.choice(jokes)
    ui.notify(f'Joke: {joke}')

# Function to show a motivational quote
def show_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Believe you can and you're halfway there. - Theodore Roosevelt"
    ]
    quote = random.choice(quotes)
    ui.notify(f'Motivational Quote: {quote}')

# Function to show a random number between 1 and 100
def random_number():
    number = random.randint(1, 100)
    ui.notify(f'Random Number: {number}')

# Function to greet the user with a personalized message
def greet_user():
    with ui.dialog() as dialog, ui.card():
        ui.label('What is your name?')
        name_input = ui.input()
        ui.button('Greet', on_click=lambda: (ui.notify(f'Hello, {name_input.value}!'), dialog.close()))
        ui.button('Cancel', on_click=dialog.close)
    dialog.open()

# Function to calculate the square of a user-defined number
def square_number():
    with ui.dialog() as dialog, ui.card():
        ui.label('Enter a number:')
        number_input = ui.input().props('type=number')
        ui.button('Calculate', on_click=lambda: (ui.notify(f'The square of {number_input.value} is {int(number_input.value) ** 2}'), dialog.close()))
        ui.button('Cancel', on_click=dialog.close)
    dialog.open()

# UI setup with tabs
@ui.page('/')
def main_page():
    ui.label('Welcome to your personalized NiceGUI app!')
    with ui.tabs():
        with ui.tab('Datetime'):
            ui.button('Show Current Date and Time', on_click=show_datetime)

        with ui.tab('Joke'):
            ui.button('Tell Me a Joke', on_click=tell_joke)

        with ui.tab('Quote'):
            ui.button('Show Motivational Quote', on_click=show_quote)

        with ui.tab('Random Number'):
            ui.button('Generate Random Number', on_click=random_number)

        with ui.tab('Greeting'):
            ui.button('Greet Me', on_click=greet_user)

        with ui.tab('Square'):
            ui.button('Calculate Square of a Number', on_click=square_number)

# Run the app on host and port 8080
ui.run(host="0.0.0.0", port=8080)