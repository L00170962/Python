"""
:description: A unit function to test the important functions
"""

# Importing the functions to check
from readlog import log_dhcpd
from dhcpack import dhcpack
from macvendor import macvendor

# Importing the unittest inbuilt module
import unittest
class TestFactorial(unittest.TestCase):
   
    def test_open_file(self):
        """Test method to check if file can be opened and read"""
        open_file_result = log_dhcpd("./dhcpd.log")
        assert open_file_result != None

    def test_get_mac_vendor(self):
        """Test method to check the vendor is returned correctly for a give OUI number"""
        get_mac_vendor_result = macvendor("a4:4c:c8")
        self.assertEqual(get_mac_vendor_result, "Dell")

if __name__ == '__main__':
    unittest.main()