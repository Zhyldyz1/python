import time

LOG_FILE = 'sample.log'
ERROR_THRESHOLD = 3  # Alert if this many errors happen
TIME_WINDOW = 60     # ...within this many seconds

def monitor_log():
    error_times = []

    with open(LOG_FILE, 'r') as f:
        f.seek(0, 2)  # Move to the end of file

        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue

            if "ERROR" in line:
                now = time.time()
                error_times.append(now)

                # Keep only recent errors
                error_times = [t for t in error_times if now - t <= TIME_WINDOW]

                if len(error_times) >= ERROR_THRESHOLD:
                    print("ALERT: Too many errors in short time!")
                    error_times.clear()

if __name__ == '__main__':
    print("Watching log for errors...")
    monitor_log()
