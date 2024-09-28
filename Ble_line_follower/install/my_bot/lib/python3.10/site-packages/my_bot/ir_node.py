# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String
# import asyncio
# from bleak import BleakScanner, BleakClient

# class BLEIRReceiverNode(Node):
#     def __init__(self):
#         super().__init__('ir_node')
#         self.publisher_ = self.create_publisher(String, 'ir_data', 10)
        
#         self.loop = asyncio.get_event_loop()
#         self.loop.run_until_complete(self.start_ble())

#     async def start_ble(self):
#         target_name = "ESP32BLE"
#         target_address = None
#         SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#         CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

#         # Scan for BLE devices
#         devices = await BleakScanner.discover()
#         for d in devices:
#             self.get_logger().info(f"Found device: {d.name} - {d.address}")
#             if target_name == d.name:
#                 target_address = d.address
#                 self.get_logger().info(f"Found target {target_name} with address {target_address}")
#                 break

#         if target_address is not None:
#             async with BleakClient(target_address) as client:
#                 self.get_logger().info(f"Connected to {target_name}: {client.is_connected}")

#                 while rclpy.ok():
#                     try:
#                         # Read data from the BLE characteristic
#                         ir_data = await client.read_gatt_char(CHARACTERISTIC_UUID)

#                         # Log the raw BLE data and its length
#                         self.get_logger().info(f"Raw BLE data: {ir_data}")
#                         self.get_logger().info(f"Received data length: {len(ir_data)}")
                        
#                         if len(ir_data) > 0:  # Check if data is not empty
#                             # Convert received bytes to string
#                             ir_data_str = ir_data.decode('utf-8', errors='ignore')
                            
#                             # Create a String message
#                             msg = String()
#                             msg.data = ir_data_str
                            
#                             # Publish the received data to the ROS 2 topic
#                             self.publisher_.publish(msg)
#                             self.get_logger().info(f"Received and published IR data: {ir_data_str}")

#                         await asyncio.sleep(0.1)  # Adjust the delay as needed

#                     except Exception as e:
#                         self.get_logger().error(f"Error in BLE communication: {str(e)}")
#                         break
#         else:
#             self.get_logger().info("Could not find the target Bluetooth device nearby.")

# def main(args=None):
#     rclpy.init(args=args)

#     ble_ir_receiver_node = BLEIRReceiverNode()

#     try:
#         rclpy.spin(ble_ir_receiver_node)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         ble_ir_receiver_node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#    main()






# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String
# import asyncio
# from bleak import BleakScanner, BleakClient

# class BLEIRReceiverNode(Node):
#     def __init__(self):
#         super().__init__('ir_node')
#         self.publisher_ = self.create_publisher(String, 'ir_data', 10)
        
#         self.loop = asyncio.get_event_loop()
#         self.loop.run_until_complete(self.start_ble())

#     async def start_ble(self):
#         target_name = "ESP32BLE"
#         target_address = None
#         SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#         CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

#         # Scan for BLE devices
#         devices = await BleakScanner.discover()
#         for d in devices:
#             self.get_logger().info(f"Found device: {d.name} - {d.address}")
#             if target_name == d.name:
#                 target_address = d.address
#                 self.get_logger().info(f"Found target {target_name} with address {target_address}")
#                 break

#         if target_address is not None:
#             async with BleakClient(target_address) as client:
#                 self.get_logger().info(f"Connected to {target_name}: {client.is_connected}")

#                 while rclpy.ok():
#                     try:
#                         # Read data from the BLE characteristic
#                         ir_data = await client.read_gatt_char(CHARACTERISTIC_UUID)

#                         # Log the raw BLE data and its length
#                         self.get_logger().info(f"Raw BLE data: {ir_data}")
#                         self.get_logger().info(f"Received data length: {len(ir_data)}")
                        
#                         if len(ir_data) > 0:  # Check if data is not empty
#                             # Convert raw bytes to a hex string
#                             ir_data_str = ir_data.hex()
                            
#                             # Create a String message
#                             msg = String()
#                             msg.data = ir_data_str
                            
#                             # Publish the received data to the ROS 2 topic
#                             self.publisher_.publish(msg)
#                             self.get_logger().info(f"Received and published IR data: {ir_data_str}")

#                         await asyncio.sleep(0.1)  # Adjust the delay as needed

#                     except Exception as e:
#                         self.get_logger().error(f"Error in BLE communication: {str(e)}")
#                         break
#         else:
#             self.get_logger().info("Could not find the target Bluetooth device nearby.")

# def main(args=None):
#     rclpy.init(args=args)

#     ble_ir_receiver_node = BLEIRReceiverNode()

#     try:
#         rclpy.spin(ble_ir_receiver_node)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         ble_ir_receiver_node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#    main()



# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String
# import asyncio
# from bleak import BleakScanner, BleakClient

# class BLEIRReceiverNode(Node):
#     def __init__(self):
#         super().__init__('ir_node')
#         self.publisher_ = self.create_publisher(String, 'ir_data', 10)
        
#         # Subscriber for motor commands
#         self.motor_commands_subscription = self.create_subscription(
#             String,
#             'motor_commands',  # Topic to subscribe to
#             self.motor_commands_callback,
#             10
#         )
#         self.get_logger().info("Subscription to 'motor_commands' topic created.")

#         self.loop = asyncio.get_event_loop()
#         self.loop.run_until_complete(self.start_ble())

#     async def start_ble(self):
#         target_name = "ESP32BLE"
#         target_address = None
#         SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#         CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

#         # Scan for BLE devices
#         devices = await BleakScanner.discover()
#         for d in devices:
#             self.get_logger().info(f"Found device: {d.name} - {d.address}")
#             if target_name == d.name:
#                 target_address = d.address
#                 self.get_logger().info(f"Found target {target_name} with address {target_address}")
#                 break

#         if target_address is not None:
#             async with BleakClient(target_address) as client:
#                 self.get_logger().info(f"Connected to {target_name}: {client.is_connected}")

#                 while rclpy.ok():
#                     try:
#                         # Read data from the BLE characteristic
#                         ir_data = await client.read_gatt_char(CHARACTERISTIC_UUID)

#                         # Log the raw BLE data and its length
#                         self.get_logger().info(f"Raw BLE data: {ir_data}")
#                         self.get_logger().info(f"Received data length: {len(ir_data)}")
                        
#                         if len(ir_data) > 0:  # Check if data is not empty
#                             # Convert raw bytes to a hex string
#                             ir_data_str = ir_data.hex()
                            
#                             # Create a String message
#                             msg = String()
#                             msg.data = ir_data_str
                            
#                             # Publish the received data to the ROS 2 topic
#                             self.publisher_.publish(msg)
#                             self.get_logger().info(f"Received and published IR data: {ir_data_str}")

#                         await asyncio.sleep(0.1)  # Adjust the delay as needed

#                     except Exception as e:
#                         self.get_logger().error(f"Error in BLE communication: {str(e)}")
#                         break
#         else:
#             self.get_logger().info("Could not find the target Bluetooth device nearby.")

#     def motor_commands_callback(self, msg):
#         motor_commands = msg.data
#         self.get_logger().info(f"Received motor commands: {motor_commands}")

# def main(args=None):
#     rclpy.init(args=args)

#     ble_ir_receiver_node = BLEIRReceiverNode()

#     try:
#         rclpy.spin(ble_ir_receiver_node)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         ble_ir_receiver_node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()


# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String
# import asyncio
# from bleak import BleakScanner, BleakClient

# class BLEIRReceiverNode(Node):
#     def __init__(self):
#         super().__init__('ble_ir_receiver_node')
#         self.publisher_ = self.create_publisher(String, 'ir_data', 10)
        
#         # Subscriber for motor commands
#         self.motor_commands_subscription = self.create_subscription(
#             String,
#             'motor_commands',  # Topic to subscribe to
#             self.motor_commands_callback,
#             10
#         )
#         self.get_logger().info("Subscription to 'motor_commands' topic created.")

#         # BLE variables
#         self.client = None
#         self.target_address = None
#         self.SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#         self.CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

#         self.loop = asyncio.get_event_loop()
#         self.loop.run_until_complete(self.start_ble())

#     async def start_ble(self):
#         target_name = "ESP32BLE"

#         # Scan for BLE devices
#         devices = await BleakScanner.discover()
#         for d in devices:
#             self.get_logger().info(f"Found device: {d.name} - {d.address}")
#             if target_name == d.name:
#                 self.target_address = d.address
#                 self.get_logger().info(f"Found target {target_name} with address {self.target_address}")
#                 break

#         if self.target_address is not None:
#             self.client = BleakClient(self.target_address)
#             await self.client.connect()
#             self.get_logger().info(f"Connected to {target_name}: {self.client.is_connected}")

#             while rclpy.ok():
#                 try:
#                     # Read data from the BLE characteristic
#                     ir_data = await self.client.read_gatt_char(self.CHARACTERISTIC_UUID)

#                     # Log the raw BLE data and its length
#                     self.get_logger().info(f"Raw BLE data: {ir_data}")
#                     self.get_logger().info(f"Received data length: {len(ir_data)}")
                    
#                     if len(ir_data) > 0:  # Check if data is not empty
#                         # Convert raw bytes to a hex string
#                         ir_data_str = ir_data.hex()
                        
#                         # Create a String message
#                         msg = String()
#                         msg.data = ir_data_str
                        
#                         # Publish the received data to the ROS 2 topic
#                         self.publisher_.publish(msg)
#                         self.get_logger().info(f"Received and published IR data: {ir_data_str}")

#                     await asyncio.sleep(0.1)  # Adjust the delay as needed

#                 except Exception as e:
#                     self.get_logger().error(f"Error in BLE communication: {str(e)}")
#                     break
#         else:
#             self.get_logger().info("Could not find the target Bluetooth device nearby.")

#     async def send_data_via_ble(self, data):
#         if self.client and self.client.is_connected:
#             await self.client.write_gatt_char(self.CHARACTERISTIC_UUID, data)
#             self.get_logger().info(f"Sent data via BLE: {data.hex()}")

#     def motor_commands_callback(self, msg):
#         motor_commands = msg.data
#         self.get_logger().info(f"Received motor commands: {motor_commands}")

#         # Convert the received commands into bytes and send via BLE
#         data_to_send = motor_commands.encode()  # Or use another encoding/format
#         self.loop.create_task(self.send_data_via_ble(data_to_send))

# def main(args=None):
#     rclpy.init(args=args)

#     ble_ir_receiver_node = BLEIRReceiverNode()

#     try:
#         rclpy.spin(ble_ir_receiver_node)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         ble_ir_receiver_node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()






# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String
# import asyncio
# from bleak import BleakScanner, BleakClient

# class BLEIRReceiverNode(Node):
#     def __init__(self):
#         super().__init__('ble_ir_receiver_node')
#         self.publisher_ = self.create_publisher(String, 'ir_data', 10)
        
#         # Subscriber for motor commands
#         self.motor_commands_subscription = self.create_subscription(
#             String,
#             'motor_commands',  # Topic to subscribe to
#             self.motor_commands_callback,
#             10
#         )
#         self.get_logger().info("Subscription to 'motor_commands' topic created.")

#         # BLE variables
#         self.client = None
#         self.target_address = None
#         self.SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#         self.CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

#         self.loop = asyncio.get_event_loop()
#         self.loop.run_until_complete(self.start_ble())

#     async def start_ble(self):
#         target_name = "ESP32BLE"

#         # Scan for BLE devices
#         devices = await BleakScanner.discover()
#         for d in devices:
#             self.get_logger().info(f"Found device: {d.name} - {d.address}")
#             if target_name == d.name:
#                 self.target_address = d.address
#                 self.get_logger().info(f"Found target {target_name} with address {self.target_address}")
#                 break

#         if self.target_address is not None:
#             self.client = BleakClient(self.target_address)
#             await self.client.connect()
#             self.get_logger().info(f"Connected to {target_name}: {self.client.is_connected}")

#             while rclpy.ok():
#                 try:
#                     # Read data from the BLE characteristic
#                     ir_data = await self.client.read_gatt_char(self.CHARACTERISTIC_UUID)

#                     # Log the raw BLE data and its length
#                     self.get_logger().info(f"Raw BLE data: {ir_data}")
#                     self.get_logger().info(f"Received data length: {len(ir_data)}")
                    
#                     if len(ir_data) > 0:  # Check if data is not empty
#                         # Convert raw bytes to a hex string
#                         ir_data_str = ir_data.hex()
                        
#                         # Create a String message
#                         msg = String()
#                         msg.data = ir_data_str
                        
#                         # Publish the received data to the ROS 2 topic
#                         self.publisher_.publish(msg)
#                         self.get_logger().info(f"Received and published IR data: {ir_data_str}")

#                     await asyncio.sleep(0.1)  # Adjust the delay as needed

#                 except Exception as e:
#                     self.get_logger().error(f"Error in BLE communication: {str(e)}")
#                     break
#         else:
#             self.get_logger().info("Could not find the target Bluetooth device nearby.")

#     async def send_data_via_ble(self, data):
#         if self.client and self.client.is_connected:
#             await self.client.write_gatt_char(self.CHARACTERISTIC_UUID, data)
#             self.get_logger().info(f"Sent data via BLE: {data.hex()}")

#     def motor_commands_callback(self, msg):
#         motor_commands = msg.data
#         self.get_logger().info(f"Received motor commands: {motor_commands}")

#         # Convert the received commands into bytes for BLE
#         data_to_send = motor_commands.encode()  # Convert to bytes
#         self.loop.create_task(self.send_data_via_ble(data_to_send))

#         # Create a String message for publishing
#         publish_msg = String()
#         publish_msg.data = motor_commands  # The data as a string
        
#         # Publish the received motor commands to the ROS 2 topic
#         self.publisher_.publish(publish_msg)
#         self.get_logger().info(f"Published motor commands: {motor_commands}")

# def main(args=None):
#     rclpy.init(args=args)

#     ble_ir_receiver_node = BLEIRReceiverNode()

#     try:
#         rclpy.spin(ble_ir_receiver_node)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         ble_ir_receiver_node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()



# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String
# import asyncio
# from bleak import BleakScanner, BleakClient

# class BLEIRReceiverNode(Node):
#     def __init__(self):
#         super().__init__('ble_ir_receiver_node')
#         self.publisher_ = self.create_publisher(String, 'ir_data', 10)
        
#         # Subscriber for motor commands
#         self.motor_commands_subscription = self.create_subscription(
#             String,
#             'motor_commands',  # Topic to subscribe to
#             self.motor_commands_callback,
#             10
#         )
#         self.get_logger().info("Subscription to 'motor_commands' topic created.")

#         # BLE variables
#         self.client = None
#         self.target_address = None
#         self.SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#         self.CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

#         self.loop = asyncio.get_event_loop()
#         self.loop.run_until_complete(self.start_ble())

#     async def start_ble(self):
#         target_name = "ESP32BLE"

#         # Scan for BLE devices
#         devices = await BleakScanner.discover()
#         for d in devices:
#             self.get_logger().info(f"Found device: {d.name} - {d.address}")
#             if target_name == d.name:
#                 self.target_address = d.address
#                 self.get_logger().info(f"Found target {target_name} with address {self.target_address}")
#                 break

#         if self.target_address is not None:
#             self.client = BleakClient(self.target_address)
#             await self.client.connect()
#             self.get_logger().info(f"Connected to {target_name}: {self.client.is_connected}")

#             while rclpy.ok():
#                 try:
#                     # Read data from the BLE characteristic
#                     ir_data = await self.client.read_gatt_char(self.CHARACTERISTIC_UUID)

#                     # Log the raw BLE data and its length
#                     self.get_logger().info(f"Raw BLE data: {ir_data}")
#                     self.get_logger().info(f"Received data length: {len(ir_data)}")
                    
#                     if len(ir_data) > 0:  # Check if data is not empty
#                         # Convert raw bytes to a string of decimal values
#                         decimal_values = ' '.join(str(byte) for byte in ir_data)
                        
#                         # Create a String message
#                         msg = String()
#                         msg.data = decimal_values
                        
#                         # Publish the received data to the ROS 2 topic
#                         self.publisher_.publish(msg)
#                         self.get_logger().info(f"Received and published IR data: {decimal_values}")

#                     await asyncio.sleep(0.1)  # Adjust the delay as needed

#                 except Exception as e:
#                     self.get_logger().error(f"Error in BLE communication: {str(e)}")
#                     break
#         else:
#             self.get_logger().info("Could not find the target Bluetooth device nearby.")

#     async def send_data_via_ble(self, data):
#         if self.client and self.client.is_connected:
#             await self.client.write_gatt_char(self.CHARACTERISTIC_UUID, data)
#             self.get_logger().info(f"Sent data via BLE: {data.hex()}")

#     def motor_commands_callback(self, msg):
#         motor_commands = msg.data
#         self.get_logger().info(f"Received motor commands: {motor_commands}")

#         # Convert the received commands into bytes for BLE
#         data_to_send = motor_commands.encode()  # Convert to bytes
#         self.loop.create_task(self.send_data_via_ble(data_to_send))

#         # Create a String message for publishing
#         publish_msg = String()
#         publish_msg.data = motor_commands  # The data as a string
        
#         # Publish the received motor commands to the ROS 2 topic
#         self.publisher_.publish(publish_msg)
#         self.get_logger().info(f"Published motor commands: {motor_commands}")

# def main(args=None):
#     rclpy.init(args=args)

#     ble_ir_receiver_node = BLEIRReceiverNode()

#     try:
#         rclpy.spin(ble_ir_receiver_node)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         ble_ir_receiver_node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()



# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String
# import asyncio
# from bleak import BleakScanner, BleakClient

# class BLEIRReceiverNode(Node):
#     def __init__(self):
#         super().__init__('ble_ir_receiver_node')
#         self.publisher_ = self.create_publisher(String, 'ir_data', 10)
        
#         # Subscriber for motor commands
#         self.motor_commands_subscription = self.create_subscription(
#             String,
#             'motor_commands',  # Topic to subscribe to
#             self.motor_commands_callback,
#             10
#         )
#         self.get_logger().info("Subscription to 'motor_commands' topic created.")

#         # BLE variables
#         self.client = None
#         self.target_address = None
#         self.SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#         self.CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

#         self.loop = asyncio.get_event_loop()
#         self.loop.run_until_complete(self.start_ble())

#     async def start_ble(self):
#         target_name = "ESP32BLE"

#         # Scan for BLE devices
#         devices = await BleakScanner.discover()
#         for d in devices:
#             self.get_logger().info(f"Found device: {d.name} - {d.address}")
#             if target_name == d.name:
#                 self.target_address = d.address
#                 self.get_logger().info(f"Found target {target_name} with address {self.target_address}")
#                 break

#         if self.target_address is not None:
#             self.client = BleakClient(self.target_address)
#             await self.client.connect()
#             self.get_logger().info(f"Connected to {target_name}: {self.client.is_connected}")

#             while rclpy.ok():
#                 try:
#                     # Read data from the BLE characteristic
#                     ir_data = await self.client.read_gatt_char(self.CHARACTERISTIC_UUID)

#                     # Log the raw BLE data and its length
#                     self.get_logger().info(f"Raw BLE data: {ir_data}")
#                     self.get_logger().info(f"Received data length: {len(ir_data)}")
                    
#                     if len(ir_data) > 0:  # Check if data is not empty
#                         # Convert raw bytes to a string of decimal values without extra spaces
#                         decimal_values = ''.join(f"{byte:02d}" for byte in ir_data)
                        
#                         # Create a String message
#                         msg = String()
#                         msg.data = decimal_values
                        
#                         # Publish the received data to the ROS 2 topic
#                         self.publisher_.publish(msg)
#                         self.get_logger().info(f"Received and published IR data: {decimal_values}")

#                     await asyncio.sleep(0.1)  # Adjust the delay as needed

#                 except Exception as e:
#                     self.get_logger().error(f"Error in BLE communication: {str(e)}")
#                     break
#         else:
#             self.get_logger().info("Could not find the target Bluetooth device nearby.")

#     async def send_data_via_ble(self, data):
#         if self.client and self.client.is_connected:
#             await self.client.write_gatt_char(self.CHARACTERISTIC_UUID, data)
#             self.get_logger().info(f"Sent data via BLE: {data.hex()}")

#     def motor_commands_callback(self, msg):
#         motor_commands = msg.data
#         self.get_logger().info(f"Received motor commands: {motor_commands}")

#         # Convert the received commands into bytes for BLE
#         data_to_send = motor_commands.encode()  # Convert to bytes
#         self.loop.create_task(self.send_data_via_ble(data_to_send))

#         # Create a String message for publishing
#         publish_msg = String()
#         publish_msg.data = motor_commands  # The data as a string
        
#         # Publish the received motor commands to the ROS 2 topic
#         self.publisher_.publish(publish_msg)
#         self.get_logger().info(f"Published motor commands: {motor_commands}")

# def main(args=None):
#     rclpy.init(args=args)

#     ble_ir_receiver_node = BLEIRReceiverNode()

#     try:
#         rclpy.spin(ble_ir_receiver_node)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         ble_ir_receiver_node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()




# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String
# import asyncio
# from bleak import BleakScanner, BleakClient

# class BLEIRReceiverNode(Node):
#     def __init__(self):
#         super().__init__('ble_ir_receiver_node')
#         self.publisher_ = self.create_publisher(String, 'ir_data', 10)
        
#         # Subscriber for motor commands
#         self.motor_commands_subscription = self.create_subscription(
#             String,
#             'motor_commands',  # Topic to subscribe to
#             self.motor_commands_callback,
#             10
#         )
#         self.get_logger().info("Subscription to 'motor_commands' topic created.")

#         # BLE variables
#         self.client = None
#         self.target_address = None
#         self.SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#         self.CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

#         self.loop = asyncio.get_event_loop()
#         self.loop.run_until_complete(self.start_ble())

#     async def start_ble(self):
#         target_name = "ESP32BLE"

#         # Scan for BLE devices
#         devices = await BleakScanner.discover()
#         for d in devices:
#             self.get_logger().info(f"Found device: {d.name} - {d.address}")
#             if target_name == d.name:
#                 self.target_address = d.address
#                 self.get_logger().info(f"Found target {target_name} with address {self.target_address}")
#                 break

#         if self.target_address is not None:
#             self.client = BleakClient(self.target_address)
#             await self.client.connect()
#             self.get_logger().info(f"Connected to {target_name}: {self.client.is_connected}")

#             # Read data from BLE characteristic and publish to ROS 2 topic
#             while rclpy.ok():
#                 try:
#                     ir_data = await self.client.read_gatt_char(self.CHARACTERISTIC_UUID)
#                     self.get_logger().info(f"Raw BLE data: {ir_data}")
#                     self.get_logger().info(f"Received data length: {len(ir_data)}")
                    
#                     if len(ir_data) > 0:  # Check if data is not empty
#                         # Convert raw bytes to a string of decimal values
#                         decimal_values = ' '.join(str(byte) for byte in ir_data)
                        
#                         # Create a String message
#                         msg = String()
#                         msg.data = decimal_values
                        
#                         # Publish the received data to the ROS 2 topic
#                         self.publisher_.publish(msg)
#                         self.get_logger().info(f"Received and published IR data: {decimal_values}")

#                     await asyncio.sleep(0.1)  # Adjust the delay as needed

#                 except Exception as e:
#                     self.get_logger().error(f"Error in BLE communication: {str(e)}")
#                     break
#         else:
#             self.get_logger().info("Could not find the target Bluetooth device nearby.")

#     async def send_data_via_ble(self, data):
#         if self.client and self.client.is_connected:
#             await self.client.write_gatt_char(self.CHARACTERISTIC_UUID, data)
#             self.get_logger().info(f"Sent data via BLE: {data.hex()}")

#     def motor_commands_callback(self, msg):
#         motor_commands = msg.data
#         self.get_logger().info(f"Received motor commands: {motor_commands}")

#         # Convert the received commands into bytes for BLE
#         data_to_send = motor_commands.encode()  # Convert to bytes
#         self.loop.create_task(self.send_data_via_ble(data_to_send))

# def main(args=None):
#     rclpy.init(args=args)

#     ble_ir_receiver_node = BLEIRReceiverNode()

#     try:
#         rclpy.spin(ble_ir_receiver_node)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         ble_ir_receiver_node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()




# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String
# import asyncio
# from bleak import BleakScanner, BleakClient

# class BLEIRReceiverNode(Node):
#     def __init__(self):
#         super().__init__('ble_ir_receiver_node')
#         self.publisher_ = self.create_publisher(String, 'ir_data', 10)
        
#         # Subscriber for motor commands
#         self.motor_commands_subscription = self.create_subscription(
#             String,
#             'motor_commands',  # Topic to subscribe to
#             self.motor_commands_callback,
#             10
#         )
#         self.get_logger().info("Subscription to 'motor_commands' topic created.")

#         # BLE variables
#         self.client = None
#         self.target_address = None
#         self.SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#         self.CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

#         self.loop = asyncio.get_event_loop()
#         self.loop.run_until_complete(self.start_ble())

#     async def start_ble(self):
#         target_name = "ESP32BLE"

#         # Scan for BLE devices
#         devices = await BleakScanner.discover()
#         for d in devices:
#             self.get_logger().info(f"Found device: {d.name} - {d.address}")
#             if target_name == d.name:
#                 self.target_address = d.address
#                 self.get_logger().info(f"Found target {target_name} with address {self.target_address}")
#                 break

#         if self.target_address is not None:
#             self.client = BleakClient(self.target_address)
#             await self.client.connect()
#             self.get_logger().info(f"Connected to {target_name}: {self.client.is_connected}")

#             while rclpy.ok():
#                 try:
#                     # Read data from the BLE characteristic
#                     ir_data = await self.client.read_gatt_char(self.CHARACTERISTIC_UUID)

#                     # Log the raw BLE data and its length
#                     self.get_logger().info(f"Raw BLE data: {ir_data}")
#                     self.get_logger().info(f"Received data length: {len(ir_data)}")
                    
#                     if len(ir_data) > 0:  # Check if data is not empty
#                         # Convert raw bytes to a string of decimal values
#                         decimal_values = ''.join(f'{byte:02x}' for byte in ir_data)  # Hexadecimal format without spaces
#                         decimal_values = ' '.join(str(byte) for byte in ir_data)
#                         # Create a String message
#                         msg = String()
#                         msg.data = decimal_values
                        
#                         # Publish the received data to the ROS 2 topic
#                         self.publisher_.publish(msg)
#                         self.get_logger().info(f"Received and published IR data: {decimal_values}")

#                     await asyncio.sleep(0.1)  # Adjust the delay as needed

#                 except Exception as e:
#                     self.get_logger().error(f"Error in BLE communication: {str(e)}")
#                     break
#         else:
#             self.get_logger().info("Could not find the target Bluetooth device nearby.")

#     async def send_data_via_ble(self, data):
#         if self.client and self.client.is_connected:
#             await self.client.write_gatt_char(self.CHARACTERISTIC_UUID, data)
#             self.get_logger().info(f"Sent data via BLE: {data.hex()}")

#     def motor_commands_callback(self, msg):
#         motor_commands = msg.data
#         self.get_logger().info(f"Received motor commands: {motor_commands}")

#         # Convert the received commands into bytes for BLE
#         data_to_send = motor_commands.encode()  # Convert to bytes
#         self.loop.create_task(self.send_data_via_ble(data_to_send))

# def main(args=None):
#     rclpy.init(args=args)

#     ble_ir_receiver_node = BLEIRReceiverNode()

#     try:
#         rclpy.spin(ble_ir_receiver_node)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         ble_ir_receiver_node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()


import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import asyncio
from bleak import BleakScanner, BleakClient

class BLEIRReceiverNode(Node):
    def __init__(self):
        super().__init__('ble_ir_receiver_node')
        self.publisher_ = self.create_publisher(String, 'ir_data', 10)
        
        # Subscriber for motor commands
        self.motor_commands_subscription = self.create_subscription(
            String,
            'motor_commands',  # Topic to subscribe to
            self.motor_commands_callback,
            10
        )
        self.get_logger().info("Subscription to 'motor_commands' topic created.")

        # BLE variables
        self.client = None
        self.target_address = None
        self.SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
        self.CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.start_ble())

    async def start_ble(self):
        target_name = "ESP32BLE"

        # Scan for BLE devices
        devices = await BleakScanner.discover()
        for d in devices:
            self.get_logger().info(f"Found device: {d.name} - {d.address}")
            if target_name == d.name:
                self.target_address = d.address
                self.get_logger().info(f"Found target {target_name} with address {self.target_address}")
                break

        if self.target_address is not None:
            self.client = BleakClient(self.target_address)
            await self.client.connect()
            self.get_logger().info(f"Connected to {target_name}: {self.client.is_connected}")

            while rclpy.ok():
                try:
                    # Read data from the BLE characteristic
                    ir_data = await self.client.read_gatt_char(self.CHARACTERISTIC_UUID)

                    # Log the raw BLE data and its length
                    self.get_logger().info(f"Raw BLE data: {ir_data}")
                    self.get_logger().info(f"Received data length: {len(ir_data)}")
                    
                    if len(ir_data) > 0:  # Check if data is not empty
                        # Convert raw bytes to a string of hexadecimal values without gaps
                        hexadecimal_values = ''.join(f'{byte:02d}' for byte in ir_data)
                        
                        # Create a String message
                        msg = String()
                        msg.data = hexadecimal_values
                        
                        # Publish the received data to the ROS 2 topic
                        self.publisher_.publish(msg)
                        self.get_logger().info(f"Received and published IR data: {hexadecimal_values}")

                    await asyncio.sleep(1)  # Adjust the delay as needed

                except Exception as e:
                    self.get_logger().error(f"Error in BLE communication: {str(e)}")
                    break
        else:
            self.get_logger().info("Could not find the target Bluetooth device nearby.")

    async def send_data_via_ble(self, data):
        if self.client and self.client.is_connected:
            await self.client.write_gatt_char(self.CHARACTERISTIC_UUID, data)
            self.get_logger().info(f"Sent data via BLE: {data.hex()}")

    def motor_commands_callback(self, msg):
        motor_commands = msg.data
        self.get_logger().info(f"Received motor commands: {motor_commands}")

        # Convert the received commands into bytes for BLE
        data_to_send = bytes(motor_commands, 'utf-8')  # Ensure data is in byte format
        self.loop.create_task(self.send_data_via_ble(data_to_send))

def main(args=None):
    rclpy.init(args=args)

    ble_ir_receiver_node = BLEIRReceiverNode()

    try:
        rclpy.spin(ble_ir_receiver_node)
    except KeyboardInterrupt:
        pass
    finally:
        ble_ir_receiver_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
