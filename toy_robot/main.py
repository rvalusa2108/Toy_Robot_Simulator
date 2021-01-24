
import yaml
import os
from toy_robot import classes_methods as cm


if __name__ == "__main__":
    try:
        #Initialize the Grid size
        grid_size = [5, 9]
        
        # Reading the file containing the commands
        filename = './toy_robot/input_commands.txt'
        with open(filename) as f:
            commands = f.readlines() 
    
        for cmd in commands:
            # breakpoint()
            cmd = cmd.rstrip('\n')
            if cmd.split(' ')[0] == "PLACE":
                pos_dir = cmd.split(' ')
                robo_obj = cm.Robot_Direction_Position(grid_size=grid_size, x=pos_dir[1], y=pos_dir[2], direction=pos_dir[3])
    
            if cmd == 'MOVE':
                robo_obj.robo_move()
                
            if cmd in ['LEFT', 'RIGHT']:
                robo_obj.robo_position(pos=cmd)
            
            if cmd == 'REPORT':
               X, Y, Direction = robo_obj.report()
    
    except:
        pass





