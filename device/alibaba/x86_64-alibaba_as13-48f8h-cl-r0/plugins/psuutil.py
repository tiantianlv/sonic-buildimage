#!/usr/bin/env python

import os.path
import subprocess
import sys
import re
import requests

try:
    from sonic_psu.psu_base import PsuBase
except ImportError as e:
    raise ImportError (str(e) + "- required module not found")

class PsuUtil(PsuBase):
    """Platform-specific PSUutil class"""

    def __init__(self):
        self.psu_restful_url = "http://192.168.1.10:8080/api/sys/fruid/status"
        PsuBase.__init__(self)

    def get_num_psus(self):
        """
        Retrieves the number of PSUs available on the device
        :return: An integer, the number of PSUs available on the device
        """
        return 2

    def get_psu_status(self, index):
        """
        Retrieves the oprational status of power supply unit (PSU) defined
                by 1-based index <index>
        :param index: An integer, 1-based index of the PSU of which to query status
        :return: Boolean, True if PSU is operating properly, False if PSU is faulty
        """

        psu_key = "PSU" + str(index)
        psu_status_key = "Power Status"
        psu_power_status = False

        try:
            r = requests.get(self.psu_restful_url)
            json_response = r.json()
            fru_status_list = json_response.get('Information')

            for fru_status in fru_status_list:            
                is_psu = fru_status.get(psu_key)
                psu_status  = str(fru_status.get(psu_status_key)).strip()

                if is_psu is not None and psu_status == "OK":
                    psu_power_status = True

        except:
            print "Error: Unable to access PSU status"
            return False

        return psu_power_status

    def get_psu_presence(self, index):
        """
        Retrieves the presence status of power supply unit (PSU) defined
                by 1-based index <index>
        :param index: An integer, 1-based index of the PSU of which to query status
        :return: Boolean, True if PSU is plugged, False if not
        """

        psu_key = "PSU" + str(index)
        psu_presence_key = "Present"
        psu_presence_status = False

        try:
            r = requests.get(self.psu_restful_url)
            json_response = r.json()
            fru_status_list = json_response.get('Information')

            for fru_status in fru_status_list:            
                is_psu = fru_status.get(psu_key)
                psu_status  = str(fru_status.get(psu_presence_key)).strip()

                if is_psu is not None and psu_status == "Present":
                    psu_presence_status = True

        except:
            print "Error: Unable to access PSU status"
            return False

        return psu_presence_status