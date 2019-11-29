#!/usr/bin/env python
# The keyboard of our robot control though
# This code is supported online
# Changed by Butian Du
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Float32
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
import numpy as np
import kinematic_model as ka

def ros_pub_cb(action_command_msg):
    j = 0
    cycle_gait_data = Float32MultiArray()
    if (action_command_msg.data == 'w'):
        rate, cycle_gait_np_data = ka.forward_gait()
    elif (action_command_msg.data == 's'):
        rate, cycle_gait_np_data = ka.backward_gait()
    elif (action_command_msg.data == 'a'):
        rate, cycle_gait_np_data = ka.turnleft_gait()
    elif (action_command_msg.data == 'd'):
        rate, cycle_gait_np_data = ka.turnright_gait()
    elif (action_command_msg.data == 'j'):
        rate, cycle_gait_np_data = ka.jump_gait()
        j = 1
    elif (action_command_msg.data == 'k'):
        rate, cycle_gait_np_data = ka.keep_gait()
        j = 1
    rospy.loginfo(cycle_gait_np_data)
    data_length = cycle_gait_np_data.shape[0]
    pause = rospy.Rate(data_length * rate)
    cycle_gait_data.data = cycle_gait_np_data
    while (j<2):
        for i in range(data_length):
            joint1_ros_pub.publish(cycle_gait_data.data[i, 0])
            joint2_ros_pub.publish(cycle_gait_data.data[i, 1])
            joint3_ros_pub.publish(cycle_gait_data.data[i, 2])
            joint4_ros_pub.publish(cycle_gait_data.data[i, 3])
            joint5_ros_pub.publish(cycle_gait_data.data[i, 4])
            joint6_ros_pub.publish(cycle_gait_data.data[i, 5])
            joint7_ros_pub.publish(cycle_gait_data.data[i, 6])
            joint8_ros_pub.publish(cycle_gait_data.data[i, 7])
            pause.sleep()
        j = j + 1

def stay_in_place()
    zeros = Float64()
    zeros.data = 0.2
    joint1_ros_pub.publish(0)
    joint2_ros_pub.publish(0)
    joint3_ros_pub.publish(0)
    joint4_ros_pub.publish(0)
    joint5_ros_pub.publish(zeros.data * 2)
    joint6_ros_pub.publish(zeros.data * 2)
    joint7_ros_pub.publish(zeros.data)
    joint8_ros_pub.publish(zeros.data)


if __name__ == '__main__':
    try:
        rospy.init_node('ros_pub_node', anonymous=True)
        joint1_ros_pub = rospy.Publisher('/ligongjoint1_position_controller/command', Float64, queue_size=10)
        joint2_ros_pub = rospy.Publisher('/ligong/joint2_position_controller/command', Float64, queue_size=10)
        joint3_ros_pub = rospy.Publisher('/ligong/joint3_position_controller/command', Float64, queue_size=10)
        joint4_ros_pub = rospy.Publisher('/ligong/joint4_position_controller/command', Float64, queue_size=10)
        joint5_ros_pub = rospy.Publisher('/ligong/joint5_position_controller/command', Float64, queue_size=10)
        joint6_ros_pub = rospy.Publisher('/ligong/joint6_position_controller/command', Float64, queue_size=10)
        joint7_ros_pub = rospy.Publisher('/ligong/joint7_position_controller/command', Float64, queue_size=10)
        joint8_ros_pub = rospy.Publisher('/ligong/joint8_position_controller/command', Float64, queue_size=10)
        rospy.Subscriber("action_command", String, ros_pub_cb)
        while not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException:
        pass