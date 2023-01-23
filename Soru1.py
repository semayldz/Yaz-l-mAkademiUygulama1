#Turtlesim’in hareket halindeki doğrusal hızını ve baktığı yönü (derece cinsinden) içeren bir
# mesaj tipi oluşturun ve bunu bir topic üzerinden yayınlayın. 

import rospy
from geometry_msgs.msg import Twist

def turtle_vel():

    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
    rospy.init_node('turtle_vel', anonymous=True)
    linear_vel = 10
    angular_vel = 30

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        vel_msg = Twist()
        vel_msg.linear.x = linear_vel
        vel_msg.angular.z = angular_vel
        rospy.loginfo("Linear velocity: %f, Angular velocity: %f", linear_vel, angular_vel)
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        turtle_vel()
    except rospy.ROSInterruptException:
        pass