total_jumping_jacks = 100
completed = 0

while completed < total_jumping_jacks:
    # Do 10 jumping jacks
    completed += 10
    print(f"You have completed {completed} jumping jacks.")

    if completed == total_jumping_jacks:
        print("Congratulations! You completed the workout!")
        break

    # Ask if tired
    tired = input("Are you tired? (yes/y or no/n): ").lower()

    if tired in ['yes', 'y']:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        
        if skip in ['yes', 'y']:
            print(f"You completed a total of {completed} jumping jacks.")
            break
        else:
            remaining = total_jumping_jacks - completed
            print(f"{remaining} jumping jacks remaining.")
    else:
        remaining = total_jumping_jacks - completed
        print(f"{remaining} jumping jacks remaining.")