distance_mi = 7
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = True

if isinstance(distance_mi, (int, float)) != True or distance_mi == 0:
    print('False')
elif distance_mi <= 1:
    if not is_raining:
        print('True')
    else:
        print('False')
elif distance_mi > 1 and distance_mi <= 6:
    if has_bike  == True and not is_raining:
        print('True')
    else:
        print('False')
else:
    if has_car == True or has_ride_share_app == True:
        print('True')
    else:
        print('False')

