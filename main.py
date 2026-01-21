import stretch_body.robot
import time

robot = stretch_body.robot.Robot()
robot.startup()

robot.stow()

robot.arm.move_to(0.5)
robot.lift.move_to(1.55)
robot.push_command()

time.sleep(5)

robot.end_of_arm.move_to('wrist_yaw',0.5)
robot.end_of_arm.move_to('wrist_pitch', -0.5)
robot.end_of_arm.move_to('wrist_roll', 1)

robot.end_of_arm.move_to('stretch_gripper',50)
robot.end_of_arm.move_to('stretch_gripper',-50)

robot.head.pose('wheels')

robot.stow()

robot.stop()
