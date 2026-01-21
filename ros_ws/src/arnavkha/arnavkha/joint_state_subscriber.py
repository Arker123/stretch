import hello_helpers.hello_misc as hm

def main():
    temp = hm.HelloNode.quick_create('temp')
    temp.stow_the_robot()
    temp.move_to_pose({'joint_arm': (0.5, 40.0)}, custom_contact_thresholds=True)
    temp.move_to_pose({'joint_lift': (1.55, 40.0)}, custom_contact_thresholds=True)
    
    temp.move_to_pose({'joint_wrist_yaw': (0.5, 20)})
    temp.move_to_pose({'joint_wrist_pitch': (-0.5, 20)})
    temp.move_to_pose({'joint_wrist_roll': (1.0, 20)})
    
    # open gripper
    temp.move_to_pose({'joint_gripper_finger_right': (50, 50)})
    temp.move_to_pose({'joint_gripper_finger_right': (50, 50)})
    
    # close gripper
    temp.move_to_pose({'joint_gripper_finger_right': (0, 50)})
    temp.move_to_pose({'joint_gripper_finger_right': (0, 50)})
    
    temp.move_to_pose({'joint_head_pan': (0.0, 20), 'joint_head_tilt': (0.0, 20)})
    
    # temp.move_to_pose({'translate_mobile_base': 1.0})
    
    # temp.move_to_pose({'
    