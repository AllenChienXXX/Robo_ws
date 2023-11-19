import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class LidarSubscriber(Node):

    def __init__(self):
        super().__init__('lidar_subscriber')
        self.sub_name = "lidar"
        self.pub_name = "sen_vel"

        self.sen_pub = self.create_publisher(Twist, self.pub_name, 10)
        self.sen_sub = self.create_subscription(LaserScan, self.sub_name, self.callback,10)


    def callback(self, msg):
        self.process(msg)

    def process(self, _msg):
        twist_msg = Twist()
        allMore = True
        # self.get_logger().info("I heard: '%f'" % _msg.ranges[0])
        # self.get_logger().info('I heard: "%s"' % msg.data)

        for i in _msg.ranges:
            if i<1.0:
                allMore = False
                break
        
        if allMore:
            twist_msg.linear.x = 0.5
            twist_msg.angular.z = 0.0
        else:
            twist_msg.linear.x = 0.0
            twist_msg.angular.z = 0.5
        
        self.sen_pub.publish(twist_msg)



def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = LidarSubscriber()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()