#Turtlesim’in hareket halindeki doğrusal hızını ve baktığı yönü (derece cinsinden) içeren bir
# mesaj tipi oluşturun ve bunu bir topic üzerinden yayınlayın. 

import rospy
from ros_essentials_cpp.msg import MyTwistMessage

def turtle_vel():

    pub = rospy.Publisher('my_twist_topic', MyTwistMessage, queue_size=10)
    rospy.init_node('my_twist_publisher_node', anonymous=True)
    
    linear_speed = 10
    angular_speed_degree = 30
    angular_speed = math.radians(abs(angular_speed_degree))

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        vel_msg = MyTwistMessage()
        vel_msg.linear.x = linear_speed
        vel_msg.angular.z = angular_speed
        rospy.loginfo("Linear velocity: %f, Angular velocity: %f", linear_speed, angular_speed)
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        turtle_vel()
    except rospy.ROSInterruptException:
        pass
