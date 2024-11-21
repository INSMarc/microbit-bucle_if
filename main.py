def on_button_pressed_a():
    global Pluja, Sol
    Pluja = 1
    Sol = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Pluja, Sol
    Pluja = 0
    Sol = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Pluja, Sol
    Pluja = 0
    Sol = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

Sol = 0
Pluja = 0
Pluja = 0
Sol = 0

def on_forever():
    if Pluja == 1:
        basic.show_string("P")
    elif Sol == 1:
        basic.show_string("U")
    else:
        basic.show_string("A")
basic.forever(on_forever)
