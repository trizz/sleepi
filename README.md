# Sleepi
Raspberry Pi scripts for controlling an interactive RGB LED bar in the bedroom. By using a PIR sensor it detects movement
and it lights up a RGB ledstrip with the brightness adjusted depending on the time of day (or night) (not ready yet...).

### Other (possible) future features:
- A webinterface controlling the state of the RGB ledstrip
    - Different types of "programs" to create lighting effects
    - Set the ledstrip to a specific colour
- Use the ledstrip as a kind of wake-up light
    - Allow multiple "alarms" (for example only on workdays at 07.00 and in the weekend at 09.00)
    - Including sound (? I don't know this one yet...)
    
#### Known bugs
- At this moment, there are several threads to detect movement, fade the ledstrip etc. These can't be killed by
the script itself (for example with a <kbd>ctrl</kbd>+<kbd>c</kbd>). For now, while debugging you can enable the last 
two lines in `scripts/run.py` or you can kill the script yourself with a process manager.