# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String

# class MotorControlNode(Node):
#     def __init__(self):
#         super().__init__('motor_control_node')

#         # Subscription to the 'ir_data' topic
#         self.subscription = self.create_subscription(
#             String,
#             'ir_data',  # Make sure this topic name is correct
#             self.listener_callback,
#             10
#         )
#         self.get_logger().info("Subscription to 'ir_data' topic created.")

#         # Publisher for motor commands
#         self.motor_command_publisher = self.create_publisher(String, 'motor_commands', 10)
#         self.get_logger().info("Publisher for 'motor_commands' topic created.")

#     def listener_callback(self, msg):
#         ir_data = msg.data
#         self.get_logger().info(f'Received IR data: "{ir_data}"')

#         # Determine motor commands based on IR data
#         if ir_data == '00':
#             # Command when IR data is '00' - all motors stop
#             commands = '0,1,100;0,1,100;0,1,100'  # Example: Motor 1, Motor 2, Motor 3
#         elif ir_data == '11':
#             # Example command: all motors full forward
#             commands = '1,0,255;1,0,255;1,0,255'
#         elif ir_data == '10':
#             # Example command: mixed controls
#             commands = '1,0,150;0,1,180;1,0,200'
#         else:
#             # Default command if IR data doesn't match known patterns
#             self.get_logger().info(f"Received unknown IR data pattern: {ir_data}")
#             commands = '0,0,0;0,0,0;0,0,0'

#         # Create a message and publish it
#         motor_command_msg = String()
#         motor_command_msg.data = commands
#         self.motor_command_publisher.publish(motor_command_msg)

#         self.get_logger().info(f'Published motor commands: {commands}')

# def main(args=None):
#     rclpy.init(args=args)
    
#     motor_control_node = MotorControlNode()
    
#     try:
#         rclpy.spin(motor_control_node)
#     except Exception as e:
#         motor_control_node.get_logger().error(f"An error occurred: {str(e)}")
#     finally:
#         motor_control_node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()


import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MotorControlNode(Node):
    def __init__(self):
        super().__init__('motor_control_node')

        # Subscription to the 'ir_data' topic
        self.subscription = self.create_subscription(
            String,
            'ir_data',  # Ensure this topic name is correct
            self.listener_callback,
            10
        )
        self.get_logger().info("Subscription to 'ir_data' topic created.")

        # Publisher for motor commands
        self.motor_command_publisher = self.create_publisher(String, 'motor_commands', 10)
        self.get_logger().info("Publisher for 'motor_commands' topic created.")

    def listener_callback(self, msg):
        ir_data = msg.data.strip()  # Remove any leading/trailing whitespace
        self.get_logger().info(f'Received IR data: "{ir_data}"')

        if ir_data == '1011':
            # Handle case where IR data is empty
            self.get_logger().info("IR data is empty, stopping all motors.")
            commands = '1,0,150;1,0,150;1,0,150'
        elif ir_data == '1011':  # Example based on your BLE hex data '16 17'
            # Add specific motor commands based on the IR data pattern
            commands = '1,0,150;1,0,150;1,0,150'
        else:
            # Handle any other cases with unknown patterns
            self.get_logger().info(f"Received unknown IR data pattern: {ir_data}")
            commands = '0,0,0;0,0,0;0,0,0'

        # Create a message and publish it
        motor_command_msg = String()
        motor_command_msg.data = commands
        self.motor_command_publisher.publish(motor_command_msg)

        self.get_logger().info(f'Published motor commands: {commands}')

def main(args=None):
    rclpy.init(args=args)
    
    motor_control_node = MotorControlNode()
    
    try:
        rclpy.spin(motor_control_node)
    except Exception as e:
        motor_control_node.get_logger().error(f"An error occurred: {str(e)}")
    finally:
        motor_control_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
