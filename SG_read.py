#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float64


def reader():
    rospy.init_node('e8257d_trigger')
    name_list = []
    for band in ["100ghz","200ghz"]:
        for stage in ["1st", "2nd_upper", "2nd_lower"]:
            name_ = "sg_{}_{}".format(band,stage)
            name_list.append(name_)

    rate = rospy.Rate(0.2)
    pub_freq_list = []
    pub_power_list = []
    pub_onoff_list = []

    for name in name_list:
        pub_freq = rospy.Publisher("{}_freq".format(name), Float64, queue_size=1)
        pub_power = rospy.Publisher("{}_power".format(name), Float64, queue_size=1)
        pub_onoff = rospy.Publisher("{}_onoff".format(name), Int32, queue_size=1)
        pub_freq_list.append(pub_freq)
        pub_power_list.append(pub_power)
        pub_onoff_list.append(pub_onoff)


    while not rospy.is_shutdown():
        
        msg_freq = Float64()
        msg_power = Float64()
        msg_onoff = Int32()

        [publisher.publish(msg_freq) for publisher in pub_freq_list]
        [publisher.publish(msg_power) for publisher in pub_power_list]
        [publisher.publish(msg_onoff) for publisher in pub_onoff_list]
            
        rate.sleep()

if __name__ == '__main__':
    reader()