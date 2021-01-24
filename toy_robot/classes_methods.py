# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:55:15 2020

@author: Raghu
"""

import logging
import os
import sys
import yaml


class Robot_Direction_Position(object):
    def __init__(self, grid_size=[4, 4], x=0, y=0, direction='NORTH'):
        # breakpoint()
        self.x = int(x)
        self.y = int(y)
        self.direction = direction
        self.grid_size = grid_size
        self.x_max = self.grid_size[0]
        self.y_max = self.grid_size[1]
        
        if not (self.grid_size[0] > 0 and self.grid_size[1] > 0):
            print(f"""Enter the correct grid size with non-negative coordinates.\nEntered grid coordinate values: X = {self.grid_size[0]}, Y = {self.grid_size[1]}""")        
            sys.exit()
        
    # def check_grid_size(self,):
    #     if not (self.grid_size[0] > 0 and self.grid_size[1] > 0):
    #         print(f"""Enter the correct grid size with non-negative coordinates.
    #               Grid coordinate values: X={self.grid_size[0]}, Y={self.grid_size[1]}""")
            
            
        
    def robo_move(self,):
        # breakpoint()
        if self.direction == 'NORTH':
            if self.y+1 <= self.y_max:
                self.y += 1
                

        if self.direction == 'EAST':
            if self.x+1 <= self.x_max:
                self.x += 1
        
        if self.direction == 'SOUTH':
            if self.y-1 <= self.y_max:
                self.y -= 1

        if self.direction == 'WEST':
            if self.x-1 <= self.x_max:
                self.x -= 1

        return self


    def robo_position(self, pos):
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
    
    def report(self,):
        # breakpoint()
        print(f"X: {self.x} Y: {self.y} Direction: {self.direction}")
        return self.x, self.y, self.direction
    
    
    
    
    
    
