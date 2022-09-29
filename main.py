import arcade

my_window = arcade.open_window(1000, 900, "Graph Paper")
arcade.set_background_color(arcade.color.AMBER)
arcade.start_render()
for x_location in range(50, 1000, 50):
    arcade.draw_line(x_location, 50, x_location, 900, arcade.color.BLACK, 2)
for y_location in range(50, 900, 50):
    arcade.draw_line(50, y_location, 1000, y_location, arcade.color.BLACK, 2)
arcade.finish_render()

arcade.run()