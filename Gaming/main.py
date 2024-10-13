import PySimpleGUI as sg
import random

# Theme and font setup
sg.theme('DarkBlue4')
sg.set_options(font='Arial 16')

# Choices for the game
choices = ['rock', 'paper', 'scissors']

# Define the layout
layout = [
    [sg.Push(), sg.Text('Choose An Option'), sg.Push()],
    [
        sg.Button(image_source='Gaming/rock.png', key='rockUser', tooltip='Rock'),
        sg.Button(image_source='Gaming/paper.png', key='paperUser', tooltip='Paper'),
        sg.Button(image_source='Gaming/scicessior.png', key='scissorsUser', tooltip='Scissors')
    ],
    [
        sg.Push(), sg.Image('Gaming/women.png'), sg.Text('VS'), sg.Image('Gaming/computer.png'), sg.Push()
    ],
    [
        sg.Push(), sg.Image(key='firstOutput', size=(100, 100)), 
        sg.Image(key='computerOutput', size=(100, 100)), sg.Push()
    ],
    [sg.Button('Reset', key='reset')]
]

# Create the window
window = sg.Window('Rock-Paper-Scissors', layout, icon='Gaming/game.png')

# Game loop
while True:
    event, values = window.read()

    # Break the loop if the window is closed
    if event == sg.WIN_CLOSED:
        break

    # Reset button logic
    if event == 'reset':
        window['firstOutput'].update(source=None)
        window['computerOutput'].update(source=None)

    # User selection logic
    if event in ['rockUser', 'paperUser', 'scissorsUser']:
        user_choice = event[:-4]  # Extract choice from key (e.g., 'rockUser' -> 'rock')
        computer_choice = random.choice(choices)

        # Update the images for user and computer choices
        window['firstOutput'].update(source=f'Gaming/{user_choice}.png')
        window['computerOutput'].update(source=f'Gaming/{computer_choice}.png')

# Close the window when the loop ends
window.close()
