print("Welcome to Pilot Navigation System...")
landing_altitude = float(input("Enter altitude = "))
if landing_altitude <= 3000 and landing_altitude > 0 :
    print("Altitude is safe for landing")
elif landing_altitude <= 0:
    print("It's already landed")
elif landing_altitude > 3000 and landing_altitude < 6000:
    print("Come down to 3000 ft and Open landing Gear for landing")
elif landing_altitude > 6000:
    print("Not allowed to land the plane")
else:
    print("Please enter Correct altitude...")
