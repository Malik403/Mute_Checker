# Mute_Checker
This script will notify the user if they're muted or not.

/ User Options for Running \
audio_source - This variable will need an Audio source to monitor. The default value is "Mic/Aux" which is the first default microphone source. No need to change if it's called that!

x_position - This variable would be the x position of the mute notification
                                                                                - I have made a axis locator and it's on my GitHub. Link: [Not uploaded yet]
y_position - This variable would be the y position of the mute notification

mute_message - Message to display when muted. The default message is "YOU'RE MUTED IDIOT"

mute_time - Time AFTER muting when the notification will show. The default time is 30 seconds

recording_or_streaming - This variable will be used if the user wants to notify ONLY when recording or ONLY when streaming. There's an option if you want it as both - it will notify if you're recording OR streaming. values: ("recording", "streaming", "both").
