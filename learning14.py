import time
import random

def print_delay(text, delay=1.5):
    print(text)
    time.sleep(delay)

def pipeline_game():
    print_delay("ALERT: The CI/CD pipeline is down!")
    print_delay("You have 3 options to investigate:")
    print_delay("1. Check Docker daemon")
    print_delay("2. Restart Jenkins")
    print_delay("3. Look at Kubernetes pods")

    choice = input("What do you want to do? (1/2/3): ").strip()

    if choice == "1":
        print_delay("Docker daemon seems fine.")
        print_delay("Try another option.")
        pipeline_game()

    elif choice == "2":
        print_delay("Restarting Jenkins...")
        time.sleep(2)
        if random.random() > 0.5:
            print_delay("Jenkins is back up. You fixed the pipeline.")
        else:
            print_delay("Still broken. Maybe it's something else.")
            pipeline_game()

    elif choice == "3":
        print_delay("Looking at Kubernetes pods...")
        print_delay("Found a crashloop on 'deploy-service'.")
        print_delay("You have 2 choices:")
        print_delay("1. Delete pod to let it restart")
        print_delay("2. Tail logs")

        sub_choice = input("Choose an action (1/2): ").strip()

        if sub_choice == "1":
            print_delay("Pod restarted successfully.")
            print_delay("Pipeline is green again. Good job.")
        else:
            print_delay("Logs show an environment variable is missing.")
            print_delay("Fixing config and re-deploying...")
            time.sleep(2)
            print_delay("Success. You debugged the issue and fixed the pipeline.")

    else:
        print_delay("Invalid choice. Try again.")
        pipeline_game()

if __name__ == "__main__":
    pipeline_game()
