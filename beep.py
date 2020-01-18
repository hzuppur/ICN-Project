import winsound
import time
from datetime import datetime

def beep():
  x = 0
  while(True):
    frequency = 500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    print("Beep nr {}. 🤠".format(x))
    x += 1
    time.sleep(9)

while(True):
  if int(datetime.now().strftime("%S"))%10 == 0:
    beep()
    break
