import time
from datetime import datetime
import winsound

# Set alarm time (24-hour format)
alarm_time = input("Enter alarm time (HH:MM:SS): ")

print(f"Alarm set for {alarm_time}")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time == alarm_time:
        print("⏰ Alarm! Wake up!")

        # Beep sound for Windows
        for i in range(5):
            winsound.Beep(1000, 1000)  # Frequency, Duration

        break

    time.sleep(1)
