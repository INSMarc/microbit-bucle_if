input.onButtonPressed(Button.A, function () {
    Pluja = 1
    Sol = 0
})
input.onButtonPressed(Button.AB, function () {
    Pluja = 0
    Sol = 0
})
input.onButtonPressed(Button.B, function () {
    Pluja = 0
    Sol = 1
})
let Sol = 0
let Pluja = 0
Pluja = 0
Sol = 0
basic.forever(function () {
    if (Pluja == 1) {
        basic.showString("P")
    } else if (Sol == 1) {
        basic.showString("U")
    } else {
        basic.showString("A")
    }
})
