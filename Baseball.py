'''
Korbin Griffin
3/13/19
The Hitting Metrics of Baseball
Final Project
All work is done with association with Logan Pennock
This code is to determine if the team up to bat will get a hit or not.
It also determines if the hit will either be a single, double, triple, or home run.
It is able to determine this by using the speed of the pitch, launch angle, speed of bat, and speed of outfielder.
'''
# This is used to give me a sense of who the person is
def introduction(x, y, z, a, b, c):
    print (x)
    print (y)
    print (z)
    print (a)
    print (b)
    print (c)
introduction ("Hello, if you are a baseball player please follow the commands below")
introduction (int(input("What is your name?")))
introduction (int(input("Do you prefer wood or metal bats?")))
introduction (int(input("How old are you?")))
introduction (int(input("How tall are you?")))
introduction (int(input("Good luck and have fun!")))
# This part of code is used to find all of the variables for the full code below
for i in range(3):
    speed_of_pitch = int(input("What is the speed of the pitch?: "))
    launch_angle = int(input("What is the angle you hit the ball at?: "))
    speed_of_bat = int(input("What is the speed of the bat?: "))
    speed_of_outfielder = 8.8
    overall_speed_of_ball = speed_of_bat - speed_of_pitch
# This For Loop shows all of the different metrics i'm using in my code.
    while launch_angle >= 0:
        print("Hit in play")
        if launch_angle <= 5:
            print("You're Out!")
            break
        elif launch_angle <= 30 and launch_angle >= 6:
            x = print("You Got a Single!")
            break
        else:
            print("You hit high enough to get more than a single.")
            x = True
            break
# Uses overall_speed_of_ball and launch_angle to determine if the ball is hit to the outfield or not
    while x == True:
        if overall_speed_of_ball  >= 20 and launch_angle <= 50:
            print("You got a single!")
            break
        elif overall_speed_of_ball >= 21 and overall_speed_of_ball <= 60 and launch_angle >= 91:
            print("You got to the outfield.")
            ball_catch = overall_speed_of_ball / speed_of_outfielder
# Uses ball_catch to determine if the outfielder can reach the ball in time and determine how many bases you get
            if ball_catch <= 7:
                print ("Ball caught.")
                break
            elif ball_catch >= 8 and ball_catch <= 10:
                print("You got a single.")
            elif ball_catch >= 11 and ball_catch <= 17:
                print("You got a double.")
                break
            elif ball_catch >= 18 and ball_catch <= 30:
                print("You got a triple.")
                break
            else:
                print("Home Run!")
                break
# This code shows how many bases you will get depending on the launch angle of the bat


