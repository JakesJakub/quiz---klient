radio.set_group(150)
stop = 1

def on_button_pressed_a():
    global stop
    if stop == 1:
        radio.send_value("answer", 0)
        radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
        stop -= 1
        basic.show_string("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global stop
    if stop == 1:
        radio.send_value("answer", 1)
        radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
        stop -= 1
        basic.show_string("B")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_released_p0():
    global stop
    if stop == 1:
        radio.send_value("answer", 2)
        radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
        stop -= 1
        basic.show_string("C")
input.on_pin_released(TouchPin.P0, on_pin_released_p0)

def on_pin_released_p1():
    global stop
    if stop == 1:
        radio.send_value("answer", 3)
        radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
        stop -= 1
        basic.show_string("D")
input.on_pin_released(TouchPin.P1, on_pin_released_p1)

def on_logo_event_pressed():
    global stop
    if stop == 0:
        basic.clear_screen()
        stop += 1
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)