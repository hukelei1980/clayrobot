#行走稳定性控制节点
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class StabilityControlNode(Node):
    def __init__(self):
        super().__init__('stability_control_node')
        self.subscription_ = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription_  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Received velocity command')

def main(args=None):
    rclpy.init(args=args)
    stability_control_node = StabilityControlNode()
    rclpy.spin(stability_control_node)
    stability_control_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
