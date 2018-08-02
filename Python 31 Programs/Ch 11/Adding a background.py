# New Graphics Window
# Demonstrates creating a graphics window

from livewires import games

# initialise graphics screen
games.init (screen_width = 640, screen_height = 480, fps = 50)

#create variable for background image
wall_image = games.load_image ("wall.jpg", transparent = False)

# adjust the game screen to reflect new background
games.screen.background = wall_image
#run

games.screen.mainloop ()
