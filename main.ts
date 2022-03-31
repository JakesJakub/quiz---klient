let odpovedi = [65, 66, 67, 68]
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendValue("answer", odpovedi[0])
    radio.receivedPacket(RadioPacketProperty.SerialNumber)
})
input.onButtonPressed(Button.A, function on_button_pressed_b() {
    radio.sendValue("answer", odpovedi[1])
    radio.receivedPacket(RadioPacketProperty.SerialNumber)
})
input.onPinReleased(TouchPin.P0, function on_pin_released_p0() {
    radio.sendValue("answer", odpovedi[2])
    radio.receivedPacket(RadioPacketProperty.SerialNumber)
})
input.onPinReleased(TouchPin.P0, function on_pin_released_p1() {
    radio.sendValue("answer", odpovedi[3])
    radio.receivedPacket(RadioPacketProperty.SerialNumber)
})
