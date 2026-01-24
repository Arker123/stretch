import stretch_body.robot
import time

robot = stretch_body.robot.Robot()
robot.startup()

robot.stow()

# robot.arm.move_to(0.5)
# robot.lift.move_to(1.55)
# robot.push_command()

# print("Waiting for arm and lift to reach position...")
# time.sleep(5)

# print("Moving end effector...")
# robot.end_of_arm.move_to('wrist_yaw',0.5)
# robot.end_of_arm.wait_until_at_setpoint()
# robot.end_of_arm.move_to('wrist_pitch', -0.5)
# robot.end_of_arm.wait_until_at_setpoint()
# robot.end_of_arm.move_to('wrist_roll', 1)
# robot.end_of_arm.wait_until_at_setpoint()

# # time.sleep(5)

# print("Operating gripper...")
# robot.end_of_arm.move_to('stretch_gripper',100)
# robot.end_of_arm.wait_until_at_setpoint()
# robot.end_of_arm.move_to('stretch_gripper',0)
# robot.end_of_arm.wait_until_at_setpoint()


# print("Moving head to neutral position...")
# robot.head.move_to('head_pan',1.0)
# robot.head.move_to('head_tilt',1.0)
# robot.head.wait_until_at_setpoint()

# robot.stow()

robot.base.translate_by(0.1)
robot.push_command()
robot.base.wait_until_at_setpoint()
robot.base.rotate_by(1.57)
robot.push_command()

robot.stop()
