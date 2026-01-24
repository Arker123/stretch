import rclpy
from rclpy.node import Node
import hello_helpers.hello_misc as hm


class JointStateSubscriber(Node):
    def __init__(self):
        super().__init__('joint_state_subscriber')

        self.get_logger().info('Creating HelloNode interface...')
        self.robot = hm.HelloNode.quick_create(self.get_name())

        # Run commands once after node starts
        self.execute_motion_sequence()

    def execute_motion_sequence(self):
        self.get_logger().info('Stowing robot...')
        self.robot.stow_the_robot()

        self.get_logger().info('Moving arm and lift...')
        self.robot.move_to_pose(
            {
                'joint_arm': (0.5, 40.0),
                'joint_lift': (1.55, 40.0)
            },
            blocking=True
        )

        self.robot.move_to_pose({'joint_wrist_yaw': (0.5, 20.0)}, blocking=True)
        self.robot.move_to_pose({'joint_wrist_pitch': (-1.0, 20.0)}, blocking=True)
        self.robot.move_to_pose({'joint_wrist_roll': (1.0, 20.0)}, blocking=True)

        # Open gripper
        self.robot.move_to_pose({'joint_gripper_finger_right': (50, 50)})
        self.robot.move_to_pose({'joint_gripper_finger_right': (50, 50)})

        # Close gripper
        self.robot.move_to_pose({'joint_gripper_finger_right': (0, 50)})
        self.robot.move_to_pose({'joint_gripper_finger_right': (0, 50)})

        self.robot.move_to_pose(
            {
                'joint_head_pan': (0.0, 20),
                'joint_head_tilt': (0.0, 20)
            }
        )

        self.get_logger().info('Motion sequence complete.')


def main(args=None):
    rclpy.init(args=args)

    node = JointStateSubscriber()

    try:
        rclpy.spin(node)  # keeps node alive if needed
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
