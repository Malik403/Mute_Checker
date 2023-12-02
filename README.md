# Mute_Checker
This is an obspython script to help a user remember to unmute their microphone by notiftying them (with a Tkinter GUI Message) if their microphone remains muted for longer than a configured length of time.

## User Options to Edit
For the moment, configuration is done by editing the script itself. All of the configurable variables are at the top of the script.

**audio_source:** This variable sets the name of the audio source to monitor. The default is "Mic/Aux" which is the first default microphone source.

**x_position:** The "x" position (in pixels) where the mute notification should be displayed -- I have made an axis locator and it's on my GitHub. [Link](https://github.com/Malik403/axis_locator).

**y_position:** The "y" position (in pixels) where the mute notification should be displayed.

**mute_message:** Message to display when muted. The default message is "YOU'RE MUTED IDIOT".

**mute_time:** How long (in seconds) the microphone can be muted before the notification will be displayed. The default time is 30 seconds.

**recording_or_streaming:** Whether notifications should be displayed when the user is recording, when the user is streaming, or both. Legal values are "recording", "streaming", or "both". The default value is "both".


## Installation
Copy the script to a location of your choice, and edit the variables at the top with your desired settings. The script requires no additional python modules and is compatable with any version of python supported by OBS.

Once the script is installed, you need to add the script to OBS:
1. Go to "Tools > Scripts".
2. If needed, go to the "Python Settings" tab and configure the location where you have Python itself installed (it should show "Loaded Python Version:     
   3.xx" beneath the Python path).
3. In the "Scripts" tab, click the "+" icon and find/select the script.
4. Use the "Script Log" button to look at the log for the script, you should see "Mute Checker Initialized, xx second delat" in the log


## Demo
![](https://github.com/Malik403/Mute_Checker/blob/main/Animation.gif)


## Credits
I originally made this script for my streamer friend, Kobe_Skrobe. You can see him in action [here](https://twitch.tv/Kobe_Skrobe).
