# Big Score
# Demonstrates displaying text on a graphics screen

from livewires import games, color

# initialise pygame window
games.init (screen_width = 640, screen_height = 480, fps = 50)

# set background
wall_image = games.load_image ("wall.jpg")
games.screen.background = wall_image

# initialise a text Object to score

score = games.Text (value = 1756521,
                    size = 60,
                    color = color.black,
                    x = 550,
                    y = 30)

# add score to screen
games.screen.add (score)
games.screen.mainloop ()
