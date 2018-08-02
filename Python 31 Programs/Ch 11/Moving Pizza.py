# Moving Pizza
# Demonstrates sprite velocities

from livewires import games

# initialise screen
games.init(screen_width = 640, screen_height = 480, fps = 50)

# set background image
wall_image = games.load_image("wall.jpg", transparent = False)
games.screen.background = wall_image

pizza_image = games.load_image("pizza.bmp")

#use pizza as a sprite to allow movement
the_pizza = games.Sprite (image = pizza_image,
                          x = games.screen.width/2,
                          y = games.screen.height/2,
                          dx = 1,
                          dy = 1)

#add the pizza sprite to the game screen
games.screen.add (the_pizza)

games.screen.mainloop ()
