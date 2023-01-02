

from math import pi

from pick_and_place_module.pick_and_place import PickAndPlace

def main():

    
    pick_and_place = PickAndPlace(0.05, 0.5)             # Arguments: gripper z offset, intermediate vertical z stop
    
    pick_and_place.setPickPose(0.448, 0.2, 0.48, 0, pi, 0)  # Arguments: x, y, z, roll, pitch, yaw 
    pick_and_place.setDropPose(0.0, 0.4, 0.7, 0, pi, 0)  # Arguments: x, y, z, roll, pitch, yaw
    pick_and_place.setGripperPose(0.03, 0.03)         # Arguments: finger1 linear movement, finger2 linear movement  
        
    pick_and_place.execute_pick_and_place()              # For execution in joint space
    #pick_and_place.execute_cartesian_pick_and_place()    # For execution in cartesian space
    


if __name__ == "__main__":
    main()

