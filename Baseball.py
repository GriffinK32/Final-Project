# The Hitting Metrics of Baseball
# Korbin Griffin

bat = x

for i in range(3):
    speed_of_pitch = int(input("What is the speed of the pitch?: "))
    launch_angle = int(input("What is the angle you hit the ball at?: "))
    speed_of_bat = int(input("What is the speed of the bat?: "))
    speed_of_outfielder = 8.8
    overall_speed_of_ball = speed_of_bat - speed_of_pitch
    while launch_angle >= 0:
        print("hit in play")
        if launch_angle >= 5:
            print ("You're Out!")
            break
        elif launch_angle == (6,15):
            x = print ("You Got a Single!")
            break
        else:
            print("you hit high enough to get more than a single")
    



