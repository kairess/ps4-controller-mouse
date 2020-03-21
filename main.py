import pyglet
from pynput.mouse import Button, Controller

mouse = Controller()

joysticks = pyglet.input.get_joysticks()

if joysticks:
    joystick = joysticks[0]

joystick.open()

is_moving_x, is_moving_y, is_scrolling = False, False, False
mouse_x, mouse_y, scroll_y = 0, 0, 0

def on_joybutton_press(joystick, button):
    if button == 2:
        mouse.click(Button.left, 1)

def on_joyhat_motion(joystick, hat_x, hat_y):
    print(hat_x, hat_y)

def on_joyaxis_motion(joystick, axis, value):
    global is_moving_x, is_moving_y, mouse_x, mouse_y, is_scrolling, scroll_y

    if axis == 'x':
        if abs(value) > 0.2:
            is_moving_x = True
            mouse_x = value * 4
        else:
            is_moving_x = False
            mouse_x = 0
    elif axis == 'y':
        if abs(value) > 0.2:
            is_moving_y = True
            mouse_y = value * 4
        else:
            is_moving_y = False
            mouse_y = 0
    elif axis == 'rz':
        if abs(value) > 0.2:
            is_scrolling = True
            scroll_y = -value * 2
        else:
            is_scrolling = False
            scroll_y = 0
    

joystick.push_handlers(
    on_joybutton_press,
    on_joyhat_motion,
    on_joyaxis_motion
)

def mouse_move(dt):
    global is_moving_x, is_moving_y, mouse_x, mouse_y, is_scrolling, scroll_y

    if is_moving_x or is_moving_y:
        mouse.move(mouse_x, mouse_y)

def mouse_scroll(dt):
    if is_scrolling:
        mouse.scroll(0, scroll_y)

pyglet.clock.schedule_interval(mouse_move, interval=0.005)
pyglet.clock.schedule_interval(mouse_scroll, interval=0.01)

pyglet.app.run()
