import time
import math

def square_root_after_delay(number, delay_ms):
    time.sleep(delay_ms / 1000)
    result = math.sqrt(number)
    return result

number = 25100
delay_ms = 2123

print(f"Square root of {number} after {delay_ms} milliseconds is {square_root_after_delay(number, delay_ms)}")
