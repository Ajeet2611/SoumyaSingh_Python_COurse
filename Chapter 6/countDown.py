#Print a Countdown before something "exciting" happens (like "Launching..." "Happy New Year !").

import time
count = int(input("Please enter countdown number set: "))
print("Countdown Strarts Now: ")
for i in range(count,0,-1):
    print(i)

    time.sleep(1)

print("\n WOHOO! Happy New Year")

