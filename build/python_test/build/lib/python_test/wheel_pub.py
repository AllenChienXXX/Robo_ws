import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist


class WheelPublisher(Node):

    def __init__(self):
        super().__init__('wheel_publisher')
        self.publisher_ = self.create_publisher(String, 'cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.index = 0
        self.size = 4
        self.linear_list = [1.0,0,1.0,0]
        self.angular_list = [0,1.57,0,1.57]

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

    def publishMessage(self):
        twist_msg = Twist()
        log_msg = "Publishing: linear: "+self.linear_list[self.index]+",angular: " + self.angular_list[self.index]
        
        twist_msg.linear.x = self.linear_list[self.index]
        twist_msg.angular.z = self.angular_list[self.index]

        self.index+=1
        if self.index >= 4:
            self.index = 0

        self.get_logger().info(log_msg)

        self.publisher_.publish(twist_msg)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = WheelPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()