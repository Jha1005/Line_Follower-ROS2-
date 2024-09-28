import rclpy
from rclpy.node import Node
import asyncio
from bleak import BleakScanner, BleakClient

class BLEIRNode(Node):
    def __init__(self):
        super().__init__('blue')
        self.get_logger().info("BLE IR Node initialized. Scanning for BLE devices...")
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.start_ble())

    async def start_ble(self):
        target_name = "ESP32BLE"
        target_address = None

        SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
        CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

        # Scan for BLE devices
        devices = await BleakScanner.discover()
        for d in devices:
            self.get_logger().info(f"Found device: {d.name} - {d.address}")
            if target_name == d.name:
                target_address = d.address
                self.get_logger().info(f"Found target {target_name} with address {target_address}")
                break

        if target_address is not None:
            async with BleakClient(target_address) as client:
                self.get_logger().info(f"Connected to {target_name}: {client.is_connected}")

                while rclpy.ok():
                    try:
                        # Read data from the BLE characteristic
                        data = await client.read_gatt_char(CHARACTERISTIC_UUID)
                        if len(data) == 2:
                            self.get_logger().info(f"Received data: {data}")

                            # Process received data if needed
                            # For example, we assume the received data is correct and we prepare an array of size 3
                            response_data = bytes([128, 128, 128])  # Example response data

                            # Send data back to the Arduino
                            await client.write_gatt_char(CHARACTERISTIC_UUID, response_data, response=True)
                            self.get_logger().info(f"Sent data: {response_data}")

                        await asyncio.sleep(1)  # Adjust the delay as needed

                    except Exception as e:
                        self.get_logger().error(f"Error in communication: {str(e)}")
                        break
        else:
            self.get_logger().info("Could not find the target Bluetooth device nearby.")

def main(args=None):
    rclpy.init(args=args)

    blue = BLEIRNode()

    try:
        rclpy.spin(blue)
    except KeyboardInterrupt:
        pass
    finally:
        blue.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
