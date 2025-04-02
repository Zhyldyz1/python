import time
import os
import signal
import threading
from collections import deque, Counter

# CONFIGURABLE VARIABLES
LOG_FILE = '/var/log/nginx/error.log'  # Change to your actual log file
ERROR_PATTERNS = ['ERROR', '500', 'Timeout']
THRESHOLD = 5      # Number of error matches to trigger alert
WINDOW = 60        # Seconds - sliding window for error frequency

# Internal state
error_counts = deque()
shutdown_flag = threading.Event()

def tail_f(file_path):
    with open(file_path, 'r') as f:
        f.seek(0, os.SEEK_END)
        while not shutdown_flag.is_set():
            line = f.readline()
            if not line:
                time.sleep(0.2)
                continue
            yield line.strip()

def match_error(line):
    return any(pattern in line for pattern in ERROR_PATTERNS)

def monitor_log():
    print(f"Monitoring {LOG_FILE} for patterns {ERROR_PATTERNS}...\n")
    for line in tail_f(LOG_FILE):
        if match_error(line):
            error_counts.append(time.time())
            print(f"[MATCH] {line}")
        purge_old_errors()
        if len(error_counts) >= THRESHOLD:
            send_alert()

def purge_old_errors():
    cutoff = time.time() - WINDOW
    while error_counts and error_counts[0] < cutoff:
        error_counts.popleft()

def send_alert():
    print(f"\n🔥 ALERT: More than {THRESHOLD} errors in last {WINDOW} seconds! 🔥\n")
    error_counts.clear()  # Reset after alert

def graceful_exit(signum, frame):
    print("\n[INFO] Shutdown signal received. Cleaning up...")
    shutdown_flag.set()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, graceful_exit)
    signal.signal(signal.SIGTERM, graceful_exit)
    try:
        monitor_log()
    except Exception as e:
        print(f"[ERROR] Unexpected failure: {e}")
