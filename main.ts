radio.setGroup(150)
let stop = 1
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (stop == 1) {
        radio.sendValue("answer", 0)
        radio.receivedPacket(RadioPacketProperty.SerialNumber)
        stop -= 1
        basic.showString("A")
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (stop == 1) {
        radio.sendValue("answer", 1)
        radio.receivedPacket(RadioPacketProperty.SerialNumber)
        stop -= 1
        basic.showString("B")
    }
    
})
input.onPinReleased(TouchPin.P0, function on_pin_released_p0() {
    
    if (stop == 1) {
        radio.sendValue("answer", 2)
        radio.receivedPacket(RadioPacketProperty.SerialNumber)
        stop -= 1
        basic.showString("C")
    }
    
})
input.onPinReleased(TouchPin.P1, function on_pin_released_p1() {
    
    if (stop == 1) {
        radio.sendValue("answer", 3)
        radio.receivedPacket(RadioPacketProperty.SerialNumber)
        stop -= 1
        basic.showString("D")
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    
    if (stop == 0) {
        basic.clearScreen()
        stop += 1
    }
    
})
