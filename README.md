# FactoryTwin AI

**ROS 2 Industrial Sensor Monitoring & Fault Detection**

A hands-on robotics engineering project focused on industrial automation, distributed communication, fault detection, and reproducible testing.

## Overview

FactoryTwin AI is an educational robotics project developed using Python and ROS 2.

Version 0.1 demonstrates a simulated industrial sensor communicating with a controller through ROS 2 topics, including a software watchdog that detects interrupted message delivery.

## Technology Stack

- Ubuntu 26.04 LTS
- ROS 2 Lyrical
- Python 3.14
- Gazebo Sim 10.5 (installed; integration pending)
- Git

## Architecture

```text
sensor_peca.py
   |
   | Publishes std_msgs/Bool
   v
/sensor/peca
   |
   | Subscribes
   v
controlador_esteira.py
   |
   +-- Process sensor readings
   +-- Monitor communication timeout
   +-- Report communication recovery
```

## Features — v0.1

- Simulated Boolean sensor publishing every second
- ROS 2 publisher/subscriber communication
- Conditional controller logic
- Communication watchdog with a three-second timeout
- Fault detection and recovery logging

## Running Locally

Prerequisite: ROS 2 Lyrical with Python bindings and standard message packages installed.

Terminal 1:

```bash
source /opt/ros/lyrical/setup.bash
python3 sensor_peca.py
```

Terminal 2:

```bash
source /opt/ros/lyrical/setup.bash
python3 controlador_esteira.py
```

## Fault Injection Test

1. Start the controller without the sensor.
2. Confirm a communication timeout is reported.
3. Start the sensor.
4. Confirm communication recovery is logged.
5. Observe normal message processing.

**Observed results:** Timeout detection, recovery logging, and resumed message processing were demonstrated in local terminal tests.

## Limitations

- Sensor values are artificially generated.
- No physical robot or actuator is controlled.
- The watchdog detects message absence, not message correctness.
- Communication recovery does not constitute industrial safety authorization.
- Gazebo physics integration and automated testing are future milestones.

## Roadmap

- [x] ROS 2 publisher/subscriber communication
- [x] Simulated industrial sensor
- [x] Controller with fault detection
- [x] Communication recovery testing
- [ ] Automated local unit tests
- [ ] Structured performance measurements
- [ ] Gazebo simulation integration
- [ ] Virtual industrial workcell
- [ ] Robot manipulation and evaluation

## Development Policy

Local development using free tools. No GitHub Actions, paid CI services, or paid cloud infrastructure.

## Project Status

**v0.1 — Initial working prototype**

The project is under active development as part of a practical robotics and embodied AI learning journey.
