#use conditional statements to determine whether commuting is possible based on the weather,
# the distance to travel, and the availability of a vehicle
distance_mi = int(input("Distance you want to travel"))
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print("False")
#if the distance is less than 1 and not raining
elif distance_mi <= 1 and not is_raining: # writing is_raining == False may have the chance to miss "==" to "=" use not
    print("True")
#if the distance is between 1 and 6 miles with bike go on
elif 1 < distance_mi <= 6 and has_bike: #its like 1<3 fi 1 less than distance
    print("True")
#if distance is 6 miles and if he got car or app he can go
elif distance_mi > 6 and(has_car or has_ride_share_app):
    print("True")
else:
    print("False")
