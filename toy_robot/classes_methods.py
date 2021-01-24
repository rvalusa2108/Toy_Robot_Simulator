# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:55:15 2020

@author: Raghu
"""

import logging
import os
import sys
import yaml

# Reading the config yaml file
with open('./toy_robot/config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)


# Initializing the logger module - file and console handlers
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


class Robot_Direction_Position(object):
    """
    Robot Toy simulator class defined with grid size initialization
    movement and LEFT & RIGHT rotation
    """
    def __init__(self, grid_size=[4, 4], x=0, y=0, direction='NORTH'):
        # breakpoint()
        self.grid_size = grid_size
        self.x_max = self.grid_size[0]-1
        self.y_max = self.grid_size[1]-1
        self.direction = direction
        
        if int(x) <= self.x_max and int(y) <= self.y_max:
            self.x = int(x)
            self.y = int(y)
        else:
            logger.info(f"""Robot placement coordinates are outside of the grid defined.""")        
            sys.exit()            
            
        
        
        if not (self.grid_size[0] > 0 and self.grid_size[1] > 0):
            logger.info(f"""Enter the correct grid size with non-negative coordinates.\nEntered grid coordinate values: X = {self.grid_size[0]}, Y = {self.grid_size[1]}""")        
            sys.exit()
        
       
    def robo_move(self,):
        try:
            # breakpoint()
            if self.direction == 'NORTH':
                if self.y+1 <= self.y_max and self.y+1 >= 0:
                    self.y += 1
                    
    
            if self.direction == 'EAST':
                if self.x+1 <= self.x_max and self.x+1 >= 0:
                    self.x += 1
            
            if self.direction == 'SOUTH':
                if self.y-1 <= self.y_max and self.y-1 >= 0:
                    self.y -= 1
    
            if self.direction == 'WEST':
                if self.x-1 <= self.x_max and self.x-1 >= 0:
                    self.x -= 1
    
            return self
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(f"""\nException Message : \n{e}\nException Type: {exc_type}\nFilename: {fname}\nLine_No: {exc_tb.tb_lineno}""")
            
    
    
    def robo_position(self, pos):
        try:
            # breakpoint()
            if pos == 'LEFT':
                if self.direction == 'NORTH':
                    # self.direction = 'WEST'
                    curr_direction = 'WEST'
        
                if self.direction == 'EAST':
                    # self.direction = 'NORTH'
                    curr_direction = 'NORTH'
                
                if self.direction == 'SOUTH':
                    # self.direction = 'EAST'
                    curr_direction = 'EAST'
        
                if self.direction == 'WEST':
                    # self.direction = 'SOUTH'
                    curr_direction = 'SOUTH'
            
            if pos == 'RIGHT':
                if self.direction == 'NORTH':
                    # self.direction = 'EAST'
                    curr_direction = 'EAST'
        
                if self.direction == 'EAST':
                    # self.direction = 'SOUTH'
                    curr_direction = 'SOUTH'
                
                if self.direction == 'SOUTH':
                    # self.direction = 'WEST'
                    curr_direction = 'WEST'
        
                if self.direction == 'WEST':
                    # self.direction = 'NORTH'
                    curr_direction = 'NORTH'
            
            self.direction = curr_direction
            
            return self
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(f"""\nException Message : \n{e}\nException Type: {exc_type}\nFilename: {fname}\nLine_No: {exc_tb.tb_lineno}""")
                
    
    def report(self,):
        try:
            # breakpoint()
            logger.info(f"X: {self.x} Y: {self.y} Direction: {self.direction}")
            print(f"X: {self.x} Y: {self.y} Direction: {self.direction}")
            return self.x, self.y, self.direction
    
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(f"""\nException Message : \n{e}\nException Type: {exc_type}\nFilename: {fname}\nLine_No: {exc_tb.tb_lineno}""")
            
       
    
    
    
    
