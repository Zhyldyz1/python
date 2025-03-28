import time

with open("/var/log/syslog", "r") as f:
    f.seek(0, 2)  # move to end
    while True:
        line = f.readline()
        if not line:
            time.sleep(1)
            continue
        print(line.strip())