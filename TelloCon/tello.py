"""
A simple python library to control DJI Tello Drones
"""

import socket
from threading import Thread

class Controller:

    """
    
    """

    def __init__(self, isSwarm = False):
        self.isSwarm = isSwarm

        #Store all tello instances in an array
        self.tellos = {}

    def add(host):
        tello = Tello()

        self.tellos.update({id:tello})


class Tello:
    """

    """
    def __init__(self):
        pass

    def connect():
        pass

    def disconnect():
        pass

    def end():
        pass