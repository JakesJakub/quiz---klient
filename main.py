odpovedi = [65, 66, 67, 68]

def on_button_pressed_a():
    radio.send_value("answer", odpovedi[0])
    radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_value("answer", odpovedi[1])
    radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
input.on_button_pressed(Button.A, on_button_pressed_b)

def on_pin_released_p0():
    radio.send_value("answer", odpovedi[2])
    radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
input.on_pin_released(TouchPin.P0, on_pin_released_p0)

def on_pin_released_p1():
    radio.send_value("answer", odpovedi[3])
    radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
input.on_pin_released(TouchPin.P0, on_pin_released_p1)
