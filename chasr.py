import pyautogui as pag ##imported for mouse movement
import screeninfo as si ##imported for screen sizes

pag.FAILSAFE = False #Stops the program from stopping when the mouse hits a corner

allscreen = si.get_monitors() #all active screens are defined

try:
    screen1 = allscreen[0] #screen1 is defined including width, height, name, etc.
    screen2 = allscreen[1] #screen2 is defined including width, height, etc.
    fullwidth = screen1.width + screen2.width #full length of both screens are defined
    dual = True

except: # if calling a second screen when there isn't one, don't panic
    screen1 = allscreen[0] #instead, only call the first screen size
    fullwidth = screen1.width #fullwidth is just the one screen's width
    dual = False

xoff = 7 #how many pixels the mouse moves in one tick on x-axis
yoff = 7 #how many pixels the mouse moves in one tick on y-axis

while True: #Do this forever

    pag.moveRel(xoff,yoff,.1) #move the mouse that far for 1/10 of a second
    p = pag.position() #call the mouse position
    px = p.x #single out the x-axis of the mouse's position
    py = p.y #single out the y-axis of the mouse's position

    if px == fullwidth-1 or px == 0: #if the mouse is at the farthest right or left point
        xoff = -xoff #reverse it's movement on the x-axis

    if dual == True: # if there are two screens
        if py == screen1.height-1 or py == 0 or py == screen2.height-1: #check if the mouse is touching any top or bottom edges
            yoff = -yoff #and flip it's movement on the y-axis if it is
    
    elif dual == False: #If there's only one screen,
        if py == screen1.height-1 or py == 0: #check if the mouse is touching the top or bottom
            yoff = -yoff #and send it back from whence it came.