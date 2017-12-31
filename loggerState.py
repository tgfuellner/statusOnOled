import re
import urequests
import utime
from SSD1306 import util

def getStatus():
  resp = urequests.get('http://logger/cgi-bin/state.py')
  m = re.search('__(.*)__.*(\d+)', resp.text)
  return (m.group(1), m.group(2))

def putOnOled():
  line1, line2 = getStatus()
  util.printLines(line1, line2)
  
def checkForEver():
  while True:
      putOnOled()
      utime.sleep(10)
  


if __name__ == "__main__":
  print(getStatus())
