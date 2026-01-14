#Welcome Branch

#Libraries Imported Here
import sys
import time

print("Welcome Branch - Develapor: CorDae Clark")
print("\n Welcome to infotechcenter V.1.0")


x = 0
ellipsis = 0

while x != 20:
    x += 1
    ellipsisMessage = ("InfoTechCenter OS Booting" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r/033[K" + ellipsisMessage + "   ")
    sys.stdout.flush()
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\nOperating system Booted Up - Retina Scanned - Access Granted")