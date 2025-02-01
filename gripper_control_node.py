#智能抓取物品
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class GripperControlNode(Node):
    def __init__(self):
        super().__init__('gripper_control_node')
        self.subscription_ = self.create_subscription(
            Bool,
            'gripper_command',
            self.listener_callback,
            10)
        self.subscription_  # prevent unused variable warning

    def listener_callback(self, msg):
        if msg.data:
            self.get_logger().info('Gripper closed')
        else:
            self.get_logger().info('Gripper opened')

def main(args=None):
    rclpy.init(args=args)
    gripper_control_node = GripperControlNode()
    rclpy.spin(gripper_control_node)
    gripper_control_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
