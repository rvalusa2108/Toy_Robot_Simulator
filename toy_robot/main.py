
import os
import sys
import logging
import yaml
import arrow

from toy_robot import classes_methods as cm

if __name__ == "__main__":
    try:
        # yaml config reading
        with open('./toy_robot/config.yaml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
        
        logger = logging.getLogger()
        if logger.handlers:
            for handler in logger.handlers:
                logger.removeHandler(handler)
        
        logger = logging.getLogger(__name__)
        logger.handlers.clear()
        if not logger.hasHandlers():
            logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
            file_handler = logging.FileHandler('./toy_robot/'+config['log_file_name'])
            file_handler.setLevel(logging._nameToLevel[config['file_log_level']])
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            consoleHandler = logging.StreamHandler(sys.stdout)
            consoleHandler.setLevel(logging._nameToLevel[config['console_log_level']])
            consoleHandler.setFormatter(formatter)
            logger.addHandler(consoleHandler)
            
        logger.info(f"####################### {arrow.now().format('MM/DD/YYYY HH:mm:ss - dddd, MMMM,YYYY')} ################################")        
        
        #Initialize the Grid size
        grid_size = config['grid_size']
        
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
    
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        logger.error(f"""\nException Message : \n{e}\nException Type: {exc_type}\nFilename: {fname}\nLine_No: {exc_tb.tb_lineno}""")
        





