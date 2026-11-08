# FactoryTwin AI — Day 02: Industrial Cell Simulation

## Objective
Build a reproducible industrial simulation with a conveyor,
a dynamic workpiece, gravity, and collision geometry.

## Environment
- ROS 2 Lyrical
- Gazebo Jetty
- SDF 1.10
- Python 3 unittest
- Local CPU simulation

## Reproduction
Run from the repository root:

    gz sim -r worlds/factory_cell.sdf

## Geometry
- Floor: 10 x 10 x 0.1 m
- Conveyor: 6 x 1.2 x 0.2 m
- Conveyor center height: 0.55 m
- Workpiece: 0.4 x 0.4 x 0.4 m
- Workpiece mass: 1 kg

## Observed Results
- Expected resting Z: 0.8500 m
- Observed resting Z: 0.8499 m
- X = 2.95 m: remained supported
- X = 3.00 m: fell
- X = 3.05 m: contacted the conveyor and fell

These are single-run observations, not statistical
estimates of a stability threshold.

## Automated Tests
Positive test:

    python3 -m unittest discover -s tests -v

Expected: 3 tests pass.

Negative test:

    FACTORY_SDF=worlds/factory_cell_invalid.sdf python3 -m unittest discover -s tests -v

Expected: one failure due to mismatched collision dimensions.

## Limitations
- Conveyor is static and cannot transport objects.
- Physical behavior was tested only in simulation.
- Stability was not evaluated across multiple runs.
- Geometry tests do not replace physics benchmarks.
- No real actuators are connected.
