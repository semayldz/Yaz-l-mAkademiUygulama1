#  Turtlesim’in doğrusal hızını kontrol eden bir node yazınız 
import rospy
from geometry_msgs.msg import Twist

def turtle_vel():
    rospy.init_node('turtle_vel', anonymous=True)
    
    vel_msg = Twist()
    vel_msg.linear.x = float(input("Turtlesim için hız değeri giriniz: "))
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        turtle_vel()
    except rospy.ROSInterruptException:
        pass