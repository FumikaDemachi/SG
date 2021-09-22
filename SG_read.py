import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float64

name_list = []
for n in ["100ghz","200ghz"]:
    for m in ["1st", "2nd_upper", "2nd_lower"]:
        name_ = "sg_{}_{}".format(n,m)
        name_list.append(name_)

def reader_freq():
    for name in name_list:
        rospy.init_node('e8257d')
        pub_freq = rospy.Publisher(name, Float64, que_size=1)
        pub_power = rospy.Publisher(name, Float64, que_size=1)
        pub_onoff = rospy.Publisher(name, Int32, que_size=1)
        rate = rospy.Rate(0.2)

        msg_freq = Float64
        msg_power = Float64
        msg_onoff = Int32

        pub_freq.publish(msg_freq)
        pub_power.publish(msg_power)
        pub_onoff.publish(msg_onoff)