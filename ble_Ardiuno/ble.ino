#i
nclude <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>

const char *SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b";
const char *CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8";

BLECharacteristic myCharacteristic(CHARACTERISTIC_UUID, BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE | BLECharacteristic::PROPERTY_NOTIFY);

const int ledPin = 2;  // Pin connected to the blue LED
bool deviceConnected = false;
bool valueWritten = false;
uint8_t receivedData[9] = {0};  // Array to hold received values (size 9)

// Callback class for characteristic write event
class MyCallbacks : public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *pCharacteristic) {
        std::string value = pCharacteristic->getValue();

        // Ensure the value length is exactly 9 bytes
        if (value.length() == 9) {
            for (int i = 0; i < 9; i++) {
                receivedData[i] = (uint8_t)value[i];  // Read each byte into the array
            }
            valueWritten = true;  // Mark that new values were written
        } else {
            Serial.println("Received data length is incorrect.");
        }
    }
};

// Callback class for connection events
class ServerCallbacks : public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) {
        deviceConnected = true;
    }

    void onDisconnect(BLEServer* pServer) {
        deviceConnected = false;
    }
};

void setup() {
    Serial.begin(115200);

    // Initialize BLE
    BLEDevice::init("ESP32BLE");

    // Create BLE Server
    BLEServer *pServer = BLEDevice::createServer();
    pServer->setCallbacks(new ServerCallbacks());  // Set connection callbacks

    // Create BLE Service
    BLEService *myService = pServer->createService(SERVICE_UUID);

    // Add characteristic to the service
    myCharacteristic.setCallbacks(new MyCallbacks());  // Set characteristic write callbacks
    myService->addCharacteristic(&myCharacteristic);

    // Start the service
    myService->start();

    // Start advertising
    BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
    pAdvertising->start();
    Serial.println("BLE advertising started.");

    // Set up the LED pin
    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, LOW);  // Ensure LED is off initially
}

void loop() {
    // Send data (two values: 10 and 11) to the Python client if connected
    if (deviceConnected) {
        uint8_t valuesToSend[2] = {10, 11};  // Array with values 10 and 11
        myCharacteristic.setValue(valuesToSend, sizeof(valuesToSend));
        myCharacteristic.notify();  // Notify the Python client of the new values
        Serial.println("Sent values 10 and 11 to Python client.");

        // Delay for demonstration purposes (adjust as necessary)
        delay(1000);
    }

    // Check if new data has been received
    if (valueWritten) {
        Serial.print("Received data: ");
        for (int i = 0; i < 9; i++) {
            Serial.print(receivedData[i]);
            Serial.print(" ");
        }
        Serial.println();

        // Check if the received data matches specific criteria
        if (receivedData[0] == 1 && receivedData[1] == 0 && receivedData[2] == 150 &&
            receivedData[3] == 1 && receivedData[4] == 0 && receivedData[5] == 150 &&
            receivedData[6] == 1 && receivedData[7] == 0 && receivedData[8] == 150) {
            Serial.println("Received specific values.");
            digitalWrite(ledPin, HIGH);  // Turn on the blue LED
        } else {
            digitalWrite(ledPin, LOW);  // Turn off the blue LED for other values
        }

        valueWritten = false;  // Reset the flag
    }

    // Ensure LED is off when disconnected
    if (!deviceConnected) {
        digitalWrite(ledPin, LOW);
    }
}
