import os
import time
import random

def check_for_changes():
    print("Checking for changes in the repo...")
    time.sleep(1)
    # Simulate change detection
    changed = random.choice([True, False])
    if changed:
        print("Changes detected.")
    else:
        print("No changes found.")
    return changed

def run_tests():
    print("Running unit tests...")
    time.sleep(2)
    passed = random.choice([True, True, False])  # Higher chance to pass
    if passed:
        print("All tests passed.")
    else:
        print("Tests failed.")
    return passed

def build_application():
    print("Building the application...")
    time.sleep(2)
    print("Build complete.")

def deploy_application():
    print("Deploying to staging environment...")
    time.sleep(2)
    print("Deployment successful.")

def main():
    print("=== DevOps Pipeline Simulation ===")
    if check_for_changes():
        if run_tests():
            build_application()
            deploy_application()
        else:
            print("Pipeline stopped: Fix the tests and try again.")
    else:
        print("Nothing to do. Pipeline exited.")

if __name__ == "__main__":
    main()
