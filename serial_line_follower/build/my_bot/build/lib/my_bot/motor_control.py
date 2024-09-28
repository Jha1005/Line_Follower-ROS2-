import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class MotorControlNode(Node):
    def __init__(self):
        super().__init__('motor_control')

        # Serial port setup with error handling
        try:
            self.serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)  # Adjust port and baud rate
            self.get_logger().info("Serial port opened successfully.")
        except serial.SerialException as e:
            self.get_logger().error(f"Failed to open serial port: {e}")
            self.serial_port = None

        # Subscription to the 'ir_data' topic
        self.subscription = self.create_subscription(
            String,
            'ir_data',
            self.listener_callback,
            10
        )
        self.subscription  # Prevent unused variable warning

    def listener_callback(self, msg):
        ir_data = msg.data
        self.get_logger().info(f'Received IR data: "{ir_data}"')

        # Determine motor commands based on IR data
        if ir_data == '00':
            # Command when IR data is '00' - all motors stop
            commands = [0, 1, 100,   # Motor 1: in1_A, in2_A, pwm_A
                        0, 1, 100,   # Motor 2: in1_B, in2_B, pwm_B
                        0, 1, 100]   # Motor 3: in1_C, in2_C, pwm_C
        elif ir_data == '11':
            # Example command: all motors full forward
            commands = [1, 0, 255,   # Motor 1: in1_A, in2_A, pwm_A
                        1, 0, 255,   # Motor 2: in1_B, in2_B, pwm_B
                        1, 0, 255]   # Motor 3: in1_C, in2_C, pwm_C
        elif ir_data == '10':
            # Example command: mixed controls
            commands = [1, 0, 150,   # Motor 1: in1_A, in2_A, pwm_A
                        0, 1, 180,   # Motor 2: in1_B, in2_B, pwm_B
                        1, 0, 200]   # Motor 3: in1_C, in2_C, pwm_C
        else:
            # Default command if IR data doesn't match known patterns
            commands = [0, 0, 0,     # Motor 1: in1_A, in2_A, pwm_A
                        0, 0, 0,     # Motor 2: in1_B, in2_B, pwm_B
                        0, 0, 0]     # Motor 3: in1_C, in2_C, pwm_C

        self.send_motor_command(commands)

    def send_motor_command(self, commands):
        if self.serial_port:
            try:
                # Send initial sync byte before data
                initial_byte = 0xAA  # Specific byte for synchronization
                
                # Append trailing byte 0x55 at the end of the command sequence
                trailing_byte = 0x55
                data = bytes([initial_byte] + commands + [trailing_byte])
                self.serial_port.write(data)

                # Log the data sent
                self.get_logger().info(f'Sent motor commands: {commands}, Trailing byte: {trailing_byte}')
                
            except serial.SerialTimeoutException:
                self.get_logger().error("Serial write timeout occurred.")
            except serial.SerialException as e:
                self.get_logger().error(f"Serial communication error: {e}")
        else:
            self.get_logger().warn("Serial port not available. Command not sent.")

def main(args=None):
    rclpy.init(args=args)
    motor_control_node = MotorControlNode()
    rclpy.spin(motor_control_node)
    motor_control_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
