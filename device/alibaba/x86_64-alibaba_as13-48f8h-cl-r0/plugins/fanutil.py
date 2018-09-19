#!/usr/bin/env python

try:
    from sonic_psu.psu_base import PsuBase
except ImportError as e:
    raise ImportError (str(e) + "- required module not found")

class FanUtil(PsuBase):
    """Platform-specific FanUtil class"""

    def __init__(self):
        PsuBase.__init__(self)


    def get_num_fans(self):     
        """   
            Get the number of fans
            :return: int num_fans
        """
        num_fans = 4

        return num_fans

    def get_fan_speed(self, index):
        """
            Get the current speed of the fan, the unit is "RPM"  
            :return: int fan_speed
        """
        fan_speed = 105600

        return fan_speed


    def  get_fan_low_threshold(self, index):
        """
            Get the low speed threshold of the fan.
            if the current speed < low speed threshold, 
            the status of the fan is not ok.
            :return: int fan_low_threshold
        """
        fan_low_threshold = 300

        return fan_low_threshold

    def get_fan_high_threshold(self, index):
        """
            Get the hight speed threshold of the fan, 
            if the current speed > high speed threshold, 
            the status of the fan is not ok
            :return: int fan_high_threshold
        """
        fan_high_threshold = 16000

        return fan_high_threshold

    def get_fan_pn(self, index):
        """
            Get the product name of the fan
            :return: str fan_pn
        """
        fan_pn = "M6510-FAN-F"

        return fan_pn

    def get_fan_sn(self, index):
        """
            Get the serial number of the fan
            :return: str fan_sn
        """
        fan_sn = "1000000000014"

        return fan_sn