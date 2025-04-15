count = 1

while True:
    print(f"Count is: {count}")
    answer = input("Do you want to continue? (yes/no): ").strip().lower()
    
    if answer != 'yes':
        print("Stopping the counter.")
        break

    count += 1
