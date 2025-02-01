# AI语音识别节点
import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

class VoiceRecognitionNode(Node):
    def __init__(self):
        super().__init__('voice_recognition_node')
        self.publisher_ = self.create_publisher(String, 'voice_command', 10)
        self.timer_ = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = "Hello, ROS 2!"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    voice_recognition_node = VoiceRecognitionNode()
    rclpy.spin(voice_recognition_node)
    voice_recognition_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
