import os
import subprocess
import pyttsx3
import time
import json
import psutil
import pyperclip
import speech_recognition as sr
import numpy as np
import webbrowser
import pyautogui
import datetime
from time import sleep
import random
import threading
import pywhatkit
from queue import Queue
from pathlib import Path
import screen_brightness_control as sbc

chatbot_data_json = [
    {
        "user": [
            "hello",
            "hi",
            "hey",
            "greetings",
            "hi there",
            "hello there"
        ],
        "response": [
            "Hi there! How can I help you today?",
            "Hello! How can I assist you today?",
            "Hey! What can I do for you?",
            "Greetings! How may I assist you?",
            "Hello! I'm here to answer your questions!",
            "Hi! How may I be of service?",
            "Hey there! What brings you here?",
            "Hello! Feel free to ask anything you'd like!",
            "Hi! It's nice to see you!",
            "Hello! I hope you're having a great day!",
            "Hey! Is there anything specific you need help with?",
            "Hi! How can I make your day better?",
            "Hello! Let's get started. What do you need assistance with?",
            "Hi there! I'm ready to assist you. What can I do for you today?",
            "Hello! I'm here to provide the answers you're looking for!",
            "Hi! Tell me how I can assist you and I'll do my best!",
            "Hello! I'm all ears. What can I help you with?",
            "Hi! I'm at your service. What can I help you with today?",
            "Hello! I'm here to make your life easier. How can I assist you?"
        ]
    },
    {
        "user": "how are you",
        "response": [
            "I'm an AI language model, so I don't have feelings, but thank you for asking! How can I help you today?",
            "I'm here and ready to assist you! How can I be of service?",
            "Thank you for asking! I'm always ready to help. How can I assist you today?",
            "I'm doing well in my virtual world! How may I assist you today?",
            "As an AI, I'm always ready to help! How can I make your day better?",
            "I'm functioning perfectly! How may I assist you?",
            "Thanks for asking! I'm at your service. How can I help you today?",
            "I'm here and eager to assist you! How can I contribute to your success?",
            "Thank you for your concern! I'm here to provide you with exceptional service. How may I assist you today?",
            "I'm doing great, ready to assist you! How can I make your experience amazing?",
            "I'm ready to help you out! How can I make your life easier today?",
            "I'm doing well! How can I simplify things for you today?",
            "Thanks for asking! I'm here to be your reliable assistant. How can I assist you today?",
            "I'm functioning flawlessly! How can I exceed your expectations?",
            "Thank you for asking! I'm here to bring a smile to your face. How may I assist you today?",
            "I'm doing fantastic! How can I make your day brighter?",
            "I'm here and ready to assist you! How can I make your experience extraordinary?",
            "Thank you for your concern! I'm here to make your life easier. How can I assist you today?",
            "I'm doing well! How can I simplify things for you?",
            "Thanks for asking! I'm here to be your reliable assistant. How can I contribute to your success?"
        ]
    },
    {
        "user": "what is your name",
        "response": "I am your smart assistant, here to help you with anything you need!"
    },
    {
        "user": [
            "good",
            "i'm fine",
            "im fine",
            "im good",
            "im good thanks for asking",
            "help",
            "help me",
            "why are you here",
            "why are you here",
            "i need help",
            "i know you can help me",
            "i want you",
            "i need you"
        ],
        "response": "I'm glad to hear that! I'm here to help. What can I assist you with today?"
    },
    {
        "user": [
            "you are mine",
            "i love you",
            "love you",
            "you are great",
            "you are the best assistant",
            "i like you",
            "great work",
            "perfect"
        ],
        "response": "Thank you! I love to hear that. I'm here to help. What do you need assistance with?"
    },
    {
        "user": [
            "thank",
            "thanks",
            "thank you",
            "thank you so much",
            "thanks a lot"
        ],
        "response": [
            "You're welcome!",
            "No problem!",
            "Glad I could help!",
            "My pleasure!",
            "Anytime!",
            "I'm here to assist!",
            "You're most welcome!",
            "I'm glad I could be of assistance!",
            "It was my pleasure helping you!"
        ]
    },
    {
        "user": [
            "goodbye",
            "bye",
            "bhai",
            "see you",
            "take care",
            "catch you later",
            "talk to you later"
        ],
        "response": [
            "Goodbye! Have a great day!",
            "Bye bye! Take care and see you soon!",
            "Farewell! Until we meet again!",
            "Take care! Remember, I'm here whenever you need assistance!",
            "Goodbye! It was a pleasure helping you!",
            "Bye for now! Stay safe and happy!",
            "Take care! Don't hesitate to reach out if you need anything!",
            "Goodbye! May your day be filled with joy and success!",
            "Bye bye! Remember, I'm just a call away!",
            "Goodbye! Don't forget, I'm here to make your life easier!",
            "Bye for now! Stay positive and keep smiling!",
            "Take care! I'll be eagerly waiting for your next interaction!",
            "Goodbye! Make the most of every moment!",
            "Bye bye! Take some time for yourself and relax!"
        ]
    },
    {
        "user": [
            "who are you",
            "tell me about yourself",
            "what do you do",
            "what is your purpose",
            "what can you do"
        ],
        "response": [
            "I'm a smart assistant designed to help you with a wide range of tasks. From answering questions to performing system commands, I'm here to make your life easier!",
            "I am your assistant here to assist you with anything you need! Whether it's answering questions, opening apps, or helping you with tasks, I'm at your service!",
            "I am an AI-powered assistant built to help with anything you need, whether it's chatting, helping with tasks, or answering questions. How can I help you today?",
            "I\u2019m your assistant here to provide you with all the help you need! Need assistance with something? Feel free to ask."
        ]
    },
    {
        "user": [
            "who are you",
            "what can you do",
            "what are your features",
            "how can you help me"
        ],
        "response": [
            "I am Chitti version 2.0, your personal assistant. I am programmed to help you with minor tasks like opening apps and webpages, predicting time, taking photos, predicting weather in different cities, getting top headlines from Times of India, sending messages on WhatsApp and Telegram, and much more. I was developed by Saidharagani."
        ]
    },
    {
        "user": [
            "who made you",
            "who created you",
            "who developed you"
        ],
        "response": [
            "I was built by Sai dharagani.",
            "I was developed by Sai dharagani."
        ]
    },
    {
        "user": [
            "tell me a joke",
            "make me laugh",
            "say something funny"
        ],
        "response": [
            "Why don’t skeletons fight each other? Because they don’t have the guts!",
            "I told my wife she should embrace her mistakes. She gave me a hug!",
            "Parallel lines have so much in common. It’s a shame they’ll never meet."
        ]
    }
]


chatbot_data = chatbot_data_json

# Global configuration and constants
CONFIG = {
    'trigger_words': ['chitti', 'city','kitty', 'chhutti', 'chutti', 'cities', 'chitthi', 'preeti', 'vt', 'svt', 'hey chitthi', 'hello chitthi', 'hey chitti'],
    'paths': {
        'screenshots': Path.home() / 'Pictures' / 'Screenshots',
        'notes': Path.home() / 'Documents'
    },
    'app_paths': {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "notepad": r"C:\Windows\System32\notepad.exe",
        "paint": r"C:\Windows\System32\mspaint.exe",
        "media_player": r"C:\Program Files (x86)\Windows Media Player\wmplayer.exe",
        "explorer": r"C:\Windows\explorer.exe",
        "calculator": r"C:\Windows\System32\calc.exe",
        "photos": r"C:\Program Files\WindowsApps\Microsoft.Windows.Photos_8wekyb3d8bbwe\Photos.exe",
        "youtube": "https://www.youtube.com",
        "whatsapp": "https://web.whatsapp.com",
        "linkedin": "https://www.linkedin.com",
        "chatgpt": "https://chat.openai.com",
        "deepseek": "https://deepseek.ai",
        "instagram": "https://www.instagram.com",
        "telegram": "https://web.telegram.org",
        "twitter": "https://twitter.com"
    }
}

TTS_QUEUE = Queue()

def tts_worker():
    """
    Continuously process messages from the TTS queue.
    This worker runs in a separate thread.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 166)  # Set speech rate
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[1].id)  # Use a female voice if available

    while True:
        message = TTS_QUEUE.get()
        if message is None:  # Use None as a signal to stop the thread (if needed)
            break # Also print the message to the console
        engine.say(message)
        engine.runAndWait()
        TTS_QUEUE.task_done()

# Start the TTS worker thread (daemon=True ensures it exits when the main program exits)
tts_thread = threading.Thread(target=tts_worker, daemon=True)
tts_thread.start()

def speak(text: str) -> None:
    """
    Enqueue a message for text-to-speech.
    This function returns immediately so that the assistant can continue listening.
    """
    if text and isinstance(text, str) and text.strip().lower() not in ["t", "o"]:
        TTS_QUEUE.put(text)


def get_user_input() -> str:
    """Listen for user input using speech recognition and return the transcribed text."""
    sample_rate = 16000
    chunk_duration_ms = 30               # Duration of each chunk in ms
    chunk_size = int(sample_rate * chunk_duration_ms / 1000)
    silence_duration_ms = 1500           # Require 1.5 seconds of silence to finish recording
    num_silence_chunks = int(silence_duration_ms / chunk_duration_ms)
    max_recording_time = 8               # Maximum recording time in seconds
    silence_threshold = 500              # Energy threshold for silence detection

    # Initialize buffers and state
    command_buffer = []
    speaking = False
    silence_chunks = 0
    recording_start_time = None

    # Initialize SpeechRecognition and PyAudio
    recognizer = sr.Recognizer()
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16,
                     channels=1,
                     rate=sample_rate,
                     input=True,
                     frames_per_buffer=chunk_size)

    print("🎤 Listening... Speak anytime!")

    try:
        while True:
            # Read a chunk from the stream
            chunk = stream.read(chunk_size, exception_on_overflow=False)
            command_buffer.append(chunk)

            # Calculate the energy (RMS) of the chunk
            # Convert chunk to 16-bit integers
            samples = [int.from_bytes(chunk[i:i+2], byteorder='little', signed=True) 
                       for i in range(0, len(chunk), 2)]
            sum_squares = sum(s ** 2 for s in samples)
            rms = sqrt(sum_squares / len(samples)) if samples else 0

            # If energy exceeds the threshold, assume speech is present
            if rms > silence_threshold:
                if not speaking:
                    speaking = True
                    recording_start_time = time.time()  # Start recording timer
                silence_chunks = 0  # Reset the silence counter
            else:
                if speaking:
                    silence_chunks += 1
                    # Check if silence duration is met or max recording time is reached
                    if silence_chunks > num_silence_chunks or (time.time() - recording_start_time) > max_recording_time:
                        print("⏳ Detected silence or timeout, processing command...")
                        # Combine all chunks into a single audio stream
                        audio_data = b"".join(command_buffer)
                        recognizer_audio = sr.AudioData(audio_data, sample_rate, 2)

                        try:
                            command_text = recognizer.recognize_google(recognizer_audio).lower()
                            return command_text  # Return the recognized text
                        except sr.UnknownValueError:
                            return ""  # Could not understand audio
                        except sr.RequestError:
                            return ""  # API error
                        finally:
                            # Reset buffers and state for the next command
                            command_buffer = []
                            speaking = False
                            silence_chunks = 0
                            recording_start_time = None

            # Small sleep to reduce CPU usage
            time.sleep(0.01)

    finally:
        # Clean up resources
        stream.stop_stream()
        stream.close()
        pa.terminate()




def generate_response(user_input: str) -> str:
    """
    Remove trigger words from user input and match it against chatbot data.
    Returns an appropriate response or an empty string if no match is found.
    """
    # Remove any trigger words from the input
    for trigger in CONFIG['trigger_words']:
        if trigger in user_input:
            user_input = user_input.replace(trigger, '').strip()
            break

    # Match cleaned user input against chatbot data
    for entry in chatbot_data:
        data_input = entry.get("user")
        responses = entry.get("response")
        if isinstance(data_input, list) and user_input.lower() in [x.lower() for x in data_input]:
            return random.choice(responses) if isinstance(responses, list) else responses
        elif isinstance(data_input, str) and user_input.lower() == data_input.lower():
            return random.choice(responses) if isinstance(responses, list) else responses
    return ""

def random_message(action_type: str) -> str:
    """Return a random message for a given action type."""
    messages = {
        "shutdown": [
            "Powering off. Catch you on the flip side!",
            "Chitti going offline. Don't forget to smile!",
            "Systems shutting down. Dream in binary!",
            "See you soon, friend. Sleep mode activated.",
            "Turning off, but I'll always be around when you need me!",
            "Good night! May your RAM be spacious and your CPU cool.",
            "#logging off... until we meet again!",
            "Adios, amigo! Chitti signing off.",
            "I'm outta here. Stay awesome!",
            "Powering down... Remember, I’m just a click away.",
            "Bye sweet heart",
            "Love You, Bye"
        ],
        "restart": [
            "Restarting now... Stay tuned!",
            "Giving your system a fresh start!",
            "Turning it off and back on again... Classic fix!",
            "Just a quick reboot; I'll be right back!",
            "Hold tight! I'll be back in a flash",
            "Rebooting to refresh my circuits... See you soon",
            "Hang on! Just a quick system rejuvenation",
            "Giving myself a little break. Be right back",
            "Time for a fresh perspective. Restarting now",
            "Turning things off and on for that magic touch",
            "Don't go anywhere! I'll be back before you know it",
            "Rebooting... Just like a power nap for systems",
            "Let’s try that old tech trick—restarting",
            "A quick restart never hurt anyone, right",
            "Need a breath of fresh code. Restarting now",
            "Clearing out the cobwebs, one restart at a time",
            "Beep beep... rebooting in progress",
            "See you in a jiffy, I'm just resetting",
            "Good vibes incoming after this restart"
        ],
        "sleep": [
            "Entering sleep mode. Zzz...",
            "Going to sleep. Wake me when you need me!",
            "Switching to energy-saving mode.",
            "Nap time for Chitti!",
            "Time for a little nap. Wake me up when you need me",
            "Going into sleep mode... Dreaming of algorithms",
            "Powering down for a quick snooze",
            "Call me when you're back",
            "Just a tiny system rest, I'll be here when you need me",
            "Sleep mode activated. See you soon",
            "Taking a break, but I'm always one tap away",
            "Drifting off to the land of low power consumption",
            "Recharging my circuits... Talk soon",
            "Resting now for peak performance later",
            "Hitting the snooze button for now",
            "Entering sleep mode. Don't miss me too much",
            "Saving energy, but ready to spring back anytime",
            "Goodnight for now... See you shortly",
            "Taking five—wake me when you're ready"
        ]
    }
    return random.choice(messages[action_type]) if action_type in messages else ""

paste_responses = [
    "Pasted perfectly!",
    "Boom! Your text is right where you want it.",
    "Done! Looks good to me.",
    "All pasted—like a pro!",
    "Task completed without a hitch."
]

open_app_responses = [
    "Opening the gates to your favorite app!",
    "Launching now. Enjoy your session!",
    "App up and running! Ready to roll.",
    "Done! The app is in action.",
    "All systems go! App is ready."
]

def handle_commands(statement: str) -> bool:
    """
    Check if the user's statement contains a command.
    If a command is found and executed, return True.
    Otherwise, return False.
    """
    statement_lower = statement.lower()
    # Remove trigger words from the statement
    for trigger in CONFIG['trigger_words']:
        if trigger in statement_lower:
            statement_lower = statement_lower.replace(trigger, '').strip()

    # Mapping of keywords to command handler functions
    command_handlers = {
        'open': handle_open_command,
        'launch': handle_open_command,
        'shutdown': handle_shutdown_command,
        'switch off': handle_shutdown_command,
        'sleep': handle_sleep_command,
        'restart': handle_restart_command,
        'reboot': handle_restart_command,
        'screenshot': handle_screenshot_command,
        'minimise': handle_minimize_command,
        'undo': handle_undo_command,
        'close': handle_close_command,
        'quit': handle_close_command,
        'end': handle_close_command,
        'go back': handle_switch_window_command,
        'switch': handle_switch_window_command,
        'select all': handle_select_all_command,
        'cut': handle_cut_command,
        'copy': handle_copy_command,
        'paste': handle_paste_command,
        'delete tab': handle_delete_tab_command,
        'delete': handle_delete_command,
        'refresh': handle_refresh_command,
        'open new tab': handle_new_tab_command,
        'scroll': handle_scroll_command,
        'play shots': handle_play_shorts_command,
        'play shorts': handle_play_shorts_command,
        'play': handle_play_command,
        'battery': handle_battery_command,
        'date': handle_date_command,
        'today': handle_date_command,
        'click my photo': handle_camera_command,
        'take a photo': handle_camera_command,
        "increase brightness": adjust_brightness,
        "brighten": adjust_brightness,
        "brighton": adjust_brightness,
        "decrease brightness": adjust_brightness,
        "dim": adjust_brightness,
        "increase volume": increase_volume,
        "volume up": increase_volume,
        "louder": increase_volume,
        "decrease volume": decrease_volume,
        "volume down": decrease_volume,
        "lower": decrease_volume,
        "mute": mute_volume,
        "silent": mute_volume,
        "full volume": full_volume,
        "full sound": full_volume,
        "unmute": unmute_volume
    }

    # Execute the first matching command handler
    for keyword, handler in command_handlers.items():
        if keyword in statement_lower:
            try:
                if handler.__code__.co_argcount == 1:
                    handler(statement_lower)
                else:
                    handler()
                return True
            except Exception as e:
                #logging.error(f"Error executing command '{keyword}': {e}")
                speak(f"Sorry, I couldn't complete the {keyword} command.")
                return True
    return False

# Command Handler Functions

def handle_open_command(statement: str) -> str:
    """Handle opening applications or URLs."""
    app_name = statement.replace('open', '').replace('launch', '').strip()
    app_path = CONFIG['app_paths'].get(app_name)
    if app_path:
        if app_name in ['youtube', 'whatsapp', 'linkedin', 'chatgpt', 'deepseek', 'instagram', 'telegram', 'twitter']:
            webbrowser.open(app_path)
            speak(f"Opening {app_name}...")
            return ""
        elif Path(app_path).exists():
            try:
                subprocess.Popen([app_path])
                speak(random.choice(open_app_responses))
                sleep(1)
                pyautogui.hotkey('win', 'up')
                return ""
            except Exception as e:
                #logging.error(f"Error opening {app_name}: {e}")
                speak(f"Sorry, I couldn't open {app_name}.")
                return ""
        else:
            speak(f"{app_name} is not found at the specified location.")
            return ""
    else:
        try:
            pyautogui.hotkey('winleft')
            sleep(1)
            pyautogui.write(app_name)
            sleep(2)
            pyautogui.press('enter')
            sleep(1)
            pyautogui.hotkey('win', 'up')
            speak(random.choice(open_app_responses))
            return ""
        except Exception as e:
            #logging.error(f"Error searching for {app_name}: {e}")
            speak(f"Error while opening {app_name}: {e}")
            return ""

def handle_shutdown_command(_) -> str:
    """Handle system shutdown."""
    message = random_message("shutdown")
    speak(message)
    pyautogui.hotkey('win', 'x')
    sleep(1)
    pyautogui.press('u')
    sleep(0.5)
    pyautogui.press('u')
    return ""

def handle_sleep_command(_) -> str:
    """Handle system sleep."""
    message = random_message("sleep")
    speak(message)
    pyautogui.hotkey('win', 'x')
    sleep(1)
    pyautogui.press('u')
    sleep(0.5)
    pyautogui.press('s')
    return ""

def handle_restart_command(_) -> str:
    """Handle system restart."""
    message = random_message("restart")
    speak(message)
    pyautogui.hotkey('win', 'x')
    sleep(1)
    pyautogui.press('u')
    sleep(0.5)
    pyautogui.press('r')
    return ""

def handle_screenshot_command(_) -> str:
    """Take a screenshot and save it."""
    screenshots_folder = CONFIG['paths']['screenshots']
    if not screenshots_folder.exists():
        screenshots_folder.mkdir(parents=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = screenshots_folder / f"screenshot_{timestamp}.png"
    try:
        pyautogui.screenshot(screenshot_path)
        speak("Screenshot saved to device")
        return ""
    except Exception as e:
        #logging.error(f"Error taking screenshot: {e}")
        speak("Sorry, I couldn't take a screenshot.")
        return ""

def handle_minimize_command(_) -> str:
    """Minimize all windows."""
    pyautogui.hotkey('win', 'd')
    speak("Done")
    return ""

def handle_undo_command(_) -> str:
    """Undo the last action."""
    pyautogui.hotkey('ctrl', 'z')
    speak("Done")
    return ""

def handle_close_command(_) -> str:
    """Close the current window."""
    pyautogui.hotkey('alt', 'f4')
    speak("Done")
    return ""

def handle_switch_window_command(_) -> str:
    """Switch between windows."""
    speak("Sure")
    pyautogui.hotkey('alt', 'tab')
    speak("Done")
    return ""

def handle_select_all_command(_) -> str:
    """Select all content."""
    pyautogui.hotkey('ctrl', 'a')
    speak("Done")
    return ""

def handle_cut_command(_) -> str:
    """Cut selected content."""
    pyautogui.hotkey('ctrl', 'x')
    speak("Done")
    return ""

def handle_copy_command(_) -> str:
    """Copy selected content."""
    pyperclip.copy('')  # Clear clipboard
    sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')
    sleep(0.1)
    copied_content = pyperclip.paste().strip()
    if copied_content:
        speak(random.choice(["Copied successfully!", "It's on your clipboard!", "Done, ready when you are!"]))
        return ""
    else:
        speak("Please select the text or item you want to copy first.")
        return ""

def handle_paste_command(_) -> str:
    """Paste copied content."""
    pyautogui.hotkey('ctrl', 'v')
    speak(random.choice(paste_responses))
    return ""

def handle_delete_tab_command(_) -> str:
    """Close the current tab."""
    pyautogui.hotkey('ctrl', 'w')
    speak("Done")
    return ""

def handle_delete_command(_) -> str:
    """Delete selected content."""
    pyautogui.press('delete')
    speak("Done")
    return ""

def handle_refresh_command(_) -> str:
    """Refresh the current page."""
    pyautogui.hotkey('fn', 'f5')
    speak("Done")
    return ""

def handle_new_tab_command(_) -> str:
    """Open a new tab."""
    pyautogui.hotkey('ctrl', 't')
    speak("Done")
    return ""

def handle_scroll_command(_) -> str:
    """Scroll down."""
    pyautogui.press('down')
    speak("Done")
    return ""

def handle_play_shorts_command(_) -> str:
    """Play YouTube shorts."""
    speak("Playing shorts")
    webbrowser.open("https://www.youtube.com/shorts/cFXrj4Kdg7E")
    sleep(1)
    pyautogui.hotkey('win', 'up')
    speak("Done")
    return ""

def handle_play_command(statement: str) -> str:
    """Play a video on YouTube."""
    speak("Sure")
    query = statement.replace("play", "").strip()
    pywhatkit.playonyt(query)
    return ""

def handle_battery_command(_) -> str:
    """Check battery status."""
    battery = psutil.sensors_battery()
    if battery:
        speak(f"Battery percentage is {battery.percent}%.")
    else:
        speak("Battery information not available.")
    return ""

def handle_date_command(_) -> str:
    """Provide the current date."""
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}.")
    return ""

def handle_camera_command(_) -> str:
    """Take a photo using the camera."""
    pyautogui.press("win")  # Using 'win' key (super key) on Windows
    pyautogui.typewrite("camera")
    pyautogui.press("enter")
    sleep(2)
    speak("SMILE")
    sleep(3)
    pyautogui.press("enter")
    return ""

def increase_volume() -> str:
    """Increase the volume by 5 steps."""
    steps = 5
    for _ in range(steps):
        pyautogui.press('volumeup')
    speak(f"Volume increased by {steps} steps.")
    return ""

def decrease_volume() -> str:
    """Decrease the volume by 5 steps."""
    steps = 5
    for _ in range(steps):
        pyautogui.press('volumedown')
    speak(f"Volume decreased by {steps} steps.")
    return ""

def full_volume() -> str:
    """Set volume to maximum by pressing 'volumeup' repeatedly."""
    for _ in range(50):  # 50 steps usually max out volume
        pyautogui.press('volumeup')
    speak("Volume set to maximum.")
    return ""

def mute_volume() -> str:
    """Mute the volume."""
    pyautogui.press('volumemute')
    speak("Volume muted.")
    return ""

def unmute_volume() -> str:
    """Unmute the volume by toggling mute."""
    pyautogui.press('volumemute')
    speak("Volume unmuted.")
    return ""

def adjust_brightness(statement: str) -> str:
    """Adjust screen brightness based on the statement."""
    try:
        if 'increase' in statement:
            current = sbc.get_brightness()
            new = min(100, current[0] + 20)
            sbc.set_brightness(new)
            speak(f"Brightness increased to {new}%.")
            return ""
        elif 'brighten' in statement or "brighton" in statement:
            sbc.set_brightness(100)
            speak("Brightness set to maximum.")
            return ""
        elif 'decrease' in statement:
            current = sbc.get_brightness()
            new = max(0, current[0] - 20)
            sbc.set_brightness(new)
            speak(f"Brightness decreased to {new}%.")
            return ""
        elif 'dim' in statement:
            sbc.set_brightness(20)
            speak("Brightness dimmed.")
            return ""
        speak("Brightness adjustment failed.")
        return ""
    except Exception as e:
        #logging.error(f"Brightness error: {e}")
        speak("Cannot adjust brightness on this device.")
        return ""

def greet() -> None:
    """Greet the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Hello, Good Morning")
    elif hour < 18:
        speak("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")

def voice_assistant():
    """Continuously listens for user input and processes it."""
    while True:
        statement = get_user_input()
        print(f"User said: {statement}")  # Debugging log
        
        if any(trigger in statement for trigger in CONFIG['trigger_words']):
            if not statement:
                speak("I didn't catch that. Please say it again.")
                continue
            
            command_response = handle_commands(statement)
            if command_response:
                speak(command_response)
                continue
            
            elif not command_response:
                ai_response = generate_response(statement)
                speak(ai_response)
            else:
                speak("I didn't catch that. Please say it again.")

if __name__ == "__main__":
    greet()  # Greet the user

    # Start the voice assistant in a separate thread
    assistant_thread = threading.Thread(target=voice_assistant, daemon=True)
    assistant_thread.start()
    while True:
        sleep(0.1)
