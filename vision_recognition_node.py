#AI视觉识别节点
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class VisionRecognitionNode(Node):
    def __init__(self):
        super().__init__('vision_recognition_node')
        self.subscription_ = self.create_subscription(
            Image,
            'camera/image_raw',
            self.listener_callback,
            10)
        self.subscription_  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Received image')

def main(args=None):
    rclpy.init(args=args)
    vision_recognition_node = VisionRecognitionNode()
    rclpy.spin(vision_recognition_node)
    vision_recognition_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
