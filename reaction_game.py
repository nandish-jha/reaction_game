from gpiozero import Button
from time import sleep
import random
import lcd_driver

disp = lcd_driver.lcd()

right_b = Button(23)
left_b = Button(24)

time = random.uniform(5, 10)
sleep(time)
disp.display_line("GO GO GO", 1)

while True:
        if right_b.is_pressed:
            disp.display_line("           RIGHT", 1)
            disp.display_line("            WINS", 2)
            break
        if left_b.is_pressed:
            disp.clear()
            disp.display_line("LEFT", 1)
            disp.display_line("WINS", 2)
            break