# Turtlesim in pozisyonunu kontrol eden bir node yazınız

import rospy
from turtlesim.msg import Pose

def turtle_pose():

    rospy.init_node('turtle_pose', anonymous=True)
    
    pose_msg = Pose()
    pose_msg.x = float(input("x değerini giriniz: "))
    pose_msg.y = float(input("y değerini giriniz: "))
    pose_msg.theta = float(input("açı değerini giriniz: "))
    
    pose_publisher = rospy.Publisher('/turtle1/pose', Pose, queue_size=10)
    pose_publisher.publish(pose_msg)

    if __name__ == '__main__':
        try:
            turtle_pose()
        except rospy.ROSInterruptException:
            pass