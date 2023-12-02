import obspython as obs
import tkinter as tk
from tkinter import ttk
import time
import threading

# User Variables - Will need to edit to your liking
audio_source = "Mic/Aux" # Edit this if need, this is the audio source name of microphone

x_position = "0" # X Position of the Message - Need to keep this as a string format

y_position = "0" # Y Position of the message - Need to keep this as a string format

mute_message = "YOU'RE MUTED IDIOT" # Message if person is muted

mute_time = 30 # If muted, how long should the script wait to notify? (Integar, no need for quotes)

recording_or_streaming = "Both" # Will you be recording or streaming? (values: Both, Recording, Streaming) Recording - Mute will notify ONLY when recording, same for Streaming, both for oth!

# Boolean Variables, no touchy!!
alerted = False
mute_detect_time = None

def make_alert_thread():
    """ This function is the message the user will receive if they're muted. """
    global alerted, mute_detect_time
    popup = tk.Tk() #Tkinter initialization

    popup.wm_title("MUTED") #Title of Message

    popup.geometry(f"300x300+{x_position}+{y_position}") #Geometry of window. The only thing you'll need to change is the x and y coordinates (which is the last two numbers)

    label = ttk.Label(popup, text=f"{mute_message}") #Message string - Can change to alphabetical character

    label.pack(side="left", fill="x", pady=100) #Where the message is located in the application

    b1 = ttk.Button(popup, text="Okay", command = popup.destroy) #Message + Command of Okay button.
    b1.pack() #Same as label1 Pack, just has nothing in it

    popup.focus() #Focusing everything so hopefully it will work xD
    label.focus() #Focusing everything so hopefully it will work xD
    b1.focus() #Focusing everything so hopefully it will work xD

    popup.mainloop() #This part finishes the tkinter GUI (Which is a message inside of the GUI) 

    alerted = False
    mute_detect_time = None

def get_muted():
    """ This function detects if the user is muted or not. """
    global alerted, mute_detect_time, mute_time, recording_or_streaming
    source = obs.obs_get_source_by_name(audio_source)
    muted = obs.obs_source_muted(source)
    obs.obs_source_release(source)
    
    # If statements for recording or streaming
    if recording_or_streaming.lower() == "recording":
        choice = obs.obs_frontend_recording_active()
    elif recording_or_streaming.lower() == "streaming":
        choice = obs.obs_frontend_streaming_active()
    elif recording_or_streaming.lower() == "both":
        choice = obs.obs_frontend_streaming_active() or obs.obs_frontend_recording_active()

    if choice:
        if muted:
            if alerted:  # we've already alerted, nothing to do
                return
            
            #otherwise, we're muted, what do we do?
            if not mute_detect_time:
                mute_detect_time = time.time()
                alerted = False
            if not alerted and (mute_detect_time + mute_time) < time.time():  #< time.time():
                # we've been muted too long, and havent alerted
                muted2 = obs.obs_source_muted(source)
                print("Muted 2 ran")
                if muted2:
                    threading.Thread(target=make_alert_thread, daemon=True).start()
                    alerted = True  # so we don't notify twice on the same mute
                    print("Muted 2 ran again")
        else:
            mute_detect_time = None

obs.timer_add(get_muted, 5000)
print(f"Mute Checker initialized, {mute_time} second delay")
