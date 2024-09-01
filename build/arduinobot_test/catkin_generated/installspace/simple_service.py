#!/usr/bin/env python3
import rospy
from arduinobot_test.srv import AddTwoInts, AddTwoIntsResponse

def service_function(req):
    a = req.a
    b = req.b
    sum = a + b
    return AddTwoIntsResponse(sum)


if __name__ == "__main__":
    rospy.init_node('simple_service')
    service = rospy.Service('add_two_ints', AddTwoInts, service_function)
    rospy.loginfo("Service Started")
    rospy.spin()