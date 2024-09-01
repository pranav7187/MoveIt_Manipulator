#!/usr/bin/env python3
import rospy
from arduinobot_test.srv import AddTwoInts
import sys

if __name__=="__main__":
    if len(sys.argv) == 3 : #first arg is file name then a then b
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    else:
        print("Error")
        sys.exit(-1)
    
    print("Requesting sum from service")
    rospy.wait_for_service('add_two_ints')
    add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
    response = add_two_ints(a, b)
    print(response)

