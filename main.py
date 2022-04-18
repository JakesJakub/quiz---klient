odpovedi = [65, 66, 67, 68]
radio.set_group(69)
stop = 1


def on_button_pressed_a():
    global stop
    if stop == 1:
        radio.send_value("answer", odpovedi[0])
        radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
        stop -= 1
        basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global stop
    if stop == 1:
        radio.send_value("answer", odpovedi[1])
        radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
        stop -= 1
        basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_released_p0():
    global stop
    if stop == 1:
        radio.send_value("answer", odpovedi[2])
        radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
        stop -= 1
        basic.show_icon(IconNames.YES)
input.on_pin_released(TouchPin.P0, on_pin_released_p0)

def on_pin_released_p1():
    global stop
    if stop == 1:
        radio.send_value("answer", odpovedi[3])
        radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
        stop -= 1
        basic.show_icon(IconNames.YES)
input.on_pin_released(TouchPin.P1, on_pin_released_p1)