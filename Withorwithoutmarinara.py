# Welcome Branch

# Libraries Imported Here
import sys
import time

# ANSI color codes
RESET = "\033[0m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"

print(CYAN + "Welcome Branch - Developer: CorDae Clark" + RESET)
print("\n" + GREEN + "Welcome to InfoTechCenter V.1.0" + RESET)

x = 0
ellipsis = 0

while x != 20:
    x += 1

    ellipsisMessage = (
        GREEN + "InfoTechCenter OS Booting " +
        YELLOW + "." * ellipsis +
        RESET
    )

    ellipsis += 1

    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()

    time.sleep(0.5)

    if ellipsis == 4:
        ellipsis = 0

    if x == 20:
        print(
            "\n" + GREEN +
            "Operating System Booted - Retina Scanned - Access Granted" +
            RESET
        )
