#!/usr/bin/env python

try:
    from sonic_psu.psu_base import PsuBase
except ImportError as e:
    raise ImportError (str(e) + "- required module not found")

class FanUtil(PsuBase):
    """Platform-specific FanUtil class"""

    def __init__(self):
        PsuBase.__init__(self)


    def get_num_sensors(self):     
        """   
            Get the number of sensors
            :return: int num_sensors
        """
        num_sensors = 4

        return num_sensors

    def get_sensor_input_num(self, index):     
        """   
            Get the number of the input items of the specified sensor
            :return: int input_num
        """
        input_num = 4

        return input_num

    def get_sensor_name(self, index):
        """   
            Get the device name of the specified sensor.
            for example "coretemp-isa-0000"
            :return: str sensor_name
        """
        sensor_name = "coretemp-isa-0000"

        return sensor_name

    def get_sensor_input_name(self, sensor_index, input_index):
        """
            Get the input item name of the specified input item of the 
            specified sensor index, for example "Physical id 0"
            :return: str sensor_input_name
        """
        sensor_input_name = "Physical id 0"

        return sensor_input_name

    def get_sensor_input_type(self, sensor_index, input_index):
        """
            Get the item type of the specified input item of the specified sensor index, 
            The return value should among  "valtage","temperature"
            :return: str sensor_input_type
        """
        sensor_input_type = "temperature"

        return sensor_input_type

    def get_sensor_input_value(self, sensor_index, input_index):
        """
            Get the current value of the input item, the unit is "V" or "C"
            :return: float sensor_input_value
        """
        sensor_input_value = 41.0

        return sensor_input_value

    def get_sensor_input_low_threshold(self, sensor_index, input_index):
        """
            Get the low threshold of the value, 
            the status of this item is not ok if the current value<low_threshold
            :return: float sensor_input_low_threshold
        """
        sensor_input_low_threshold = 0.0

        return sensor_input_low_threshold

    def get_sensor_input_high_threshold(self, sensor_index, input_index):
        """
            Get the high threshold of the value, 
            the status of this item is not ok if the current value > high_threshold
            :return: float sensor_input_high_threshold
        """
        sensor_input_low_threshold = 50.0

        return sensor_input_low_threshold