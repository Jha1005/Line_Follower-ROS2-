import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class IRReceiverNode(Node):
    def __init__(self):
        super().__init__('ir_node')
        # Create a publisher for the 'ir_data' topic with a queue size of 10
        self.publisher_ = self.create_publisher(String, 'ir_data', 10)
        # Open the serial port with the specified parameters
        self.serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)  # Adjust port and baud rate
        # Create a timer to call the callback function at a regular interval (0.1 seconds)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        # Check if there's data available in the serial buffer
        if self.serial_port.in_waiting > 0:
            # Read a line from the serial port, decode it to a string, and remove trailing whitespace
            line = self.serial_port.readline().decode('utf-8').rstrip()
            # Publish the cleaned data to the 'ir_data' topic
            self.publisher_.publish(String(data=line))
            # Log the data being published
            self.get_logger().info(f'Publishing IR data: "{line}"')

def main(args=None):
    # Initialize the ROS 2 Python client library
    rclpy.init(args=args)
    # Create an instance of the IRReceiverNode class
    ir_receiver_node = IRReceiverNode()
    # Spin the node to keep it active and processing callbacks
    rclpy.spin(ir_receiver_node)
    # Clean up and shut down the node when done
    ir_receiver_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()