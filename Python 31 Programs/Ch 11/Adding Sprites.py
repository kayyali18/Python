# Pizza Sprite
# Demonstrating creating a sprite

from livewires import games

games.init (screen_width = 640, screen_height = 480, fps = 50)

# intitialise background image
wall_image = games.load_image ("wall.jpg", transparent = False)
games.screen.background = wall_image

## add a sprite

pizza_image = games.load_image ("pizza.bmp")
pizza = games.Sprite (image = pizza_image, x = 320, y = 240)
games.screen.add (pizza)
# to remove sprite
# games.screen.destroy (pizza)

# run game
games.screen.mainloop ()
