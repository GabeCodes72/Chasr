# Chasr
A python project that drags your mouse around and bounces like the old DVD screensaver.
It took way more time than it should have to figure some stuff out for this thing, but it was worth the annoyance and lost hair.

#What happens?
Pyautogui is imported to move the mouse and screeninfo is imported for the... well, screen info. Size and how many there are. 
The "failsafe" is disabled because I didn't want it crashing on the rare chance that it hits the corner.
Afterwards, the size and quantity of the monitors is defined, allowing them to be defined and called as needed. The code then defines the first and second screen. If there isn't a second screen, it resorts to just defining one and sets the value `dual` to `False`.
The distance the mouse travels on each axis per tick is set. (I set it at 7 because it just has to be big enough to not move like Internet Explorer and small enough so that the mouse isn't senselessly jumping around the screen.
With everything defined, the fun begins with the mouse moving just a ***teeny*** bit down and right. The following all happens in a split second:
The mouse's position is called and split into x and y coordinates separately. The code then checks if the mouse is near the left or right edges of the screen. If it is, then the mouse will turn around, but still going whichever direction it was going on the y-axis. The `dual` value is then checked to see if it is true or false. If it's true, there are two screens and the mouse can be checked to see if it is touching the bottom of either the 1st OR 2nd screen. If it's false, there's only one screen and the mouse will only be checked to see if it's touching the bottom of the one screen. After both, it's also checked if it's touching the top. Both paths have this check because the top will always be 0.
If either is true, then the mouse will move opposite of where it was going on the Y-Axis.
This whole process is then repeated every 1/10 of a second.

There's a lot here, but it's just what is happening. If you don't like the nerd stuff, then know this: This only works with two screens. It also only works correctly if the screens are side-by-side.

Well, have fun! Just open the file and let that mouse do it's thing. Also, you can still move the mouse very easily, so you can close the window and stop it the regular way, or you can focus the window and hit Ctrl+C to stop the program.
