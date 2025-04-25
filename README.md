Overall Requirements of the Micromouse Power Subsystem Project
The project focuses on designing a power subsystem for a micromouse robot, a small autonomous robot tasked with navigating a maze in competitions. The power subsystem must meet a variety of requirements to ensure the robot operates efficiently, reliably, and within the specified constraints. Below are the detailed requirements that define the scope and functionality of this subsystem.

1. Motor Control
The power subsystem must support bidirectional control of up to four motors:

Two Brushed DC Motors: Each motor can draw up to 200mA at the maximum voltage of a 1S1P battery (typically around 4.2V when fully charged).
Two Auxiliary Motors: Each requires 500mA, necessitating a higher current capacity. This requirement demands a motor driver capable of handling these current levels and providing precise control for navigation.
2. Battery Monitoring
To manage the battery effectively, the subsystem must include:

An INA219 Current Sensor connected to the I2C bus for monitoring battery voltage and current.
Proper configuration of the INA219, ensuring that address pins A0 and A1 are not both grounded to set a unique I2C address and avoid bus conflicts. This feature enables real-time tracking of battery health and power consumption.
3. Battery Charging
The subsystem must charge the battery from a 9V input pin with two distinct charging modes:

Low Current Mode: 200mA, suitable for slower, gentler charging.
High Current Mode: Approximately 600mA (±100mA), allowing faster charging when needed. These modes provide flexibility in balancing charging speed and battery longevity.
4. USB-C Integration
The design must incorporate a USB-C interface capable of delivering 9V from a USB host. This functionality serves as an alternative power source or charging option, enhancing the subsystem's versatility for different operational scenarios.

5. External Load Switches
Two high-side load switches must be included, each connected to the 5V rail and capable of handling 1A. These switches allow the subsystem to control power delivery to external components or peripherals, enabling efficient power management.

6. Regulated Voltage Outputs
The subsystem must provide stable power to the robot's electronics through two regulated outputs:

3.3V Output: With 5% accuracy and a maximum current of 300mA, suitable for powering microcontrollers and sensors.
5V Output: With 5% accuracy and a maximum current of 1.5A, supporting a broader range of components. These precise voltage levels are critical to ensure reliable operation of the micromouse's systems.
7. ON/OFF Switch
An ON/OFF switch is required to control the robot's power state:

OFF State: Battery draw must be less than 30μA to minimize energy loss during inactivity.
ON State: Must support a peak current of 2A to meet the robot's maximum power demand and shut down both the 5V and 3.3V outputs when switched off. This switch ensures energy conservation and safe power cycling.
Summary
The micromouse power subsystem must integrate motor control, battery monitoring and charging, USB-C functionality, load switching, regulated voltage outputs, and an efficient ON/OFF mechanism. These requirements collectively ensure the robot can navigate a maze autonomously while maintaining power efficiency, reliability, and adaptability to varying operational needs. The design must balance performance with constraints such as current limits, voltage accuracy, and minimal power draw in the OFF state, making it a critical component of the micromouse's success in competition environments.
