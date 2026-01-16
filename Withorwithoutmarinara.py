# Welcome Branch
# This program simulates a simple boot-up animation
# using dots that appear and disappear.

# Libraries Imported Here
import sys      # Used to write output on the same line in the terminal
import time     # Used to add delays for animation timing

# ANSI color codes (used to color text in the terminal)
RESET = "\033[0m"    # Resets text color to default
GREEN = "\033[32m"   # Green text
CYAN = "\033[36m"    # Cyan text
YELLOW = "\033[33m"  # Yellow text

# Display startup messages
print(CYAN + "Welcome Branch - Developer: CorDae Clark" + RESET)
print("\n" + GREEN + "Welcome to InfoTechCenter V.1.0" + RESET)

# Counter to control how long the boot animation runs
x = 0

# Controls how many dots appear in the animation
ellipsis = 0

# Loop runs until x reaches 20
while x != 20:
    x += 1  # Increase loop counter

    # Create the boot message with animated dots
    ellipsisMessage = (
        GREEN + "InfoTechCenter OS Booting " +
        YELLOW + "." * ellipsis +
        RESET
    )

    ellipsis += 1  # Add another dot each loop

    # Overwrite the current terminal line with the new message
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()  # Force the update to appear immediately

    # Pause to control animation speed
    time.sleep(0.5)

    # Reset dots after reaching 3
    if ellipsis == 4:
        ellipsis = 0

    # When the loop finishes, print the success message
    if x == 20:
        print(
            "\n" + GREEN +
            "Operating System Booted - Retina Scanned - Access Granted" +
            RESET
        )