import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float64

name_list = []
for band in ["100ghz","200ghz"]:
    for stage in ["1st", "2nd_upper", "2nd_lower"]:
        name_ = "sg_{}_{}".format(band,stage)
        name_list.append(name_)

rospy.init_node('e8257d_trigger')
rate = rospy.Rate(0.2)

def reader():
    while not rospy.is_shutdown():
        for name in name_list:
            pub_freq = rospy.Publisher("{}_freq".format(name), Float64, queue_size=1)
            pub_power = rospy.Publisher("{}_power".format(name), Float64, queue_size=1)
            pub_onoff = rospy.Publisher("{}_onoff".format(name), Int32, queue_size=1)

            msg_freq = Float64()
            msg_power = Float64()
            msg_onoff = Int32()

            pub_freq.publish(msg_freq)
            pub_power.publish(msg_power)
            pub_onoff.publish(msg_onoff)

        rate.sleep()

if __name__ == '__main__':
    reader()