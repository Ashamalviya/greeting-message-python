hour = int(input("Enter the hour (0-23): "))

if hour >= 0 and hour < 12:
    print("Good Morning Sir!")

elif hour >= 12 and hour < 17:
    print("Good Afternoon Sir!")

else:
    print("Good Night Sir!")
