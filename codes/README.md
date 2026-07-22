#  Autonomous PID Robot Controller (Raspberry Pi)

##  Project Overview
An autonomous navigation system for a Raspberry Pi robot that uses an **MPU6050 Gyroscope** paired with a **PID Controller** to maintain straight-line stability and execute precise 90-degree turns, while using **HC-SR04 Ultrasonic Sensors** for wall detection.

---

##  Core Modules & Logic

### 1. Orientation & PID Control
* **Gyroscope Angle Integration**: The system reads angular velocity from the MPU6050 along the Z-axis and integrates it over time to maintain continuous orientation tracking.
* **PID Heading Adjustment**: A PID controller constantly measures the error between target and actual heading to output steering correction values to the servo.

### 2. Autonomous Navigation & Turn Management
* **Obstacle Detection**: Monitors the front sensor for walls ($< 99\text{ cm}$).
* **Directional Logic**: Scans side sensors when an obstacle is detected to determine turn direction, shifting target heading by $\pm 90^\circ$.
* **State Machine**: Tracks total turns made, halting main operation after 12 successful turns.

### 3. Victory Lap & Safety
* **Timed Straight Drive**: Drives forward under PID lock for a final 5-second period after navigation finishes.
* **Emergency Halt**: Provides safe stopping routines to power down motors and reset steering position.

---

##  Hardware Pinout Summary

| Component | Function | GPIO / Interface |
| :--- | :--- | :--- |
| **Drive Motor** | Main Propulsion | Forward: GPIO 20 / Backward: GPIO 12 |
| **Steering Servo** | Wheel Direction | GPIO 17 |
| **Front Ultrasonic** | Distance Sensing | Trigger: GPIO 5 / Echo: GPIO 6 |
| **Left Ultrasonic** | Distance Sensing | Trigger: GPIO 23 / Echo: GPIO 24 |
| **Right Ultrasonic** | Distance Sensing | Trigger: GPIO 27 / Echo: GPIO 22 |
| **MPU6050 Gyro** | Heading Tracking | I2C Bus 1 (Address 0x68) |

---

## 🚀 Execution Sequence
