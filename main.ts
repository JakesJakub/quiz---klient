let odpovedi = [65, 66, 67, 68]
radio.setGroup(69)
let stop = 1
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (stop == 1) {
        radio.sendValue("answer", odpovedi[0])
        radio.receivedPacket(RadioPacketProperty.SerialNumber)
        stop -= 1
        basic.showIcon(IconNames.Yes)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (stop == 1) {
        radio.sendValue("answer", odpovedi[1])
        radio.receivedPacket(RadioPacketProperty.SerialNumber)
        stop -= 1
        basic.showIcon(IconNames.Yes)
    }
    
})
input.onPinReleased(TouchPin.P0, function on_pin_released_p0() {
    
    if (stop == 1) {
        radio.sendValue("answer", odpovedi[2])
        radio.receivedPacket(RadioPacketProperty.SerialNumber)
        stop -= 1
        basic.showIcon(IconNames.Yes)
    }
    
})
input.onPinReleased(TouchPin.P1, function on_pin_released_p1() {
    
    if (stop == 1) {
        radio.sendValue("answer", odpovedi[3])
        radio.receivedPacket(RadioPacketProperty.SerialNumber)
        stop -= 1
        basic.showIcon(IconNames.Yes)
    }
    
})
