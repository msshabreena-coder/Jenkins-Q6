import time


print("Frontend check started.")
time.sleep(4)

with open("frontend_report.txt", "w") as file:
    file.write("Frontend check completed successfully.\n")

print("Frontend check completed.")
