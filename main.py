import pyautogui
import time
import keyboard


def bot():
    if pyautogui.pixel(1129, 224)[0] == 170:
        pyautogui.click(1009, 270)
        pyautogui.click(1009, 397)
        pyautogui.click(1009, 465)
    elif pyautogui.pixel(1285, 212)[0] == 59:
        print("No energy")
        shop()
        energy_full = False
        while not energy_full:
            if keyboard.is_pressed("q"):
                street()
                return "q"

            if pyautogui.pixel(1416, 212)[0] == 251:
                print("Energy full")
                energy_full = True
            else:
                print("Eating")
                pyautogui.click(957, 878)
        street()
    else:
        if pyautogui.pixel(959, 686)[0] == 89:
            print("Enemy attacked")
            keyboard.press_and_release("d")
        elif pyautogui.pixel(959, 686)[0] == 219:
            print("Money collected")
            keyboard.press_and_release("a")
        else:
            print("Street crossed")
            keyboard.press_and_release("w")


def shop():
    print("Go to shop")
    pyautogui.click(640, 147)


def street():
    print("Go to street")
    pyautogui.click(640, 104)

running = False
pressedKey = ""
while True:
    pressedKey = keyboard.read_key()
    if keyboard.is_pressed("s"):
        while pressedKey != "q":
            pressedKey = bot()
            if keyboard.is_pressed("q"):
                pressedKey = "q"
                break

#   1054 150 enemy
#   959 686  money

# energy empty - 1278 212   R:59
# energy full - 1416 212    R:251
# kebab X:  957 , Y:  878
# lvl btn X:1015 Y:273  RGB: 229
