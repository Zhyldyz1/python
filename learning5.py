import shutil

total, used, free = shutil.disk_usage("/")
if used / total > 0.9:
    print("Disk usage is above 90%! Take action.")