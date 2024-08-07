import os
import json
from genie.testbed import load
from pyats import aetest


class CheckFiles(aetest.Testcase):
    @aetest.setup
    def setup(self):
        # Load the testbed file
        self.testbed = load('TestLab/testbed.yaml')
        # set a specific device in the testbed
        self.device = self.testbed.devices['my_device']
        # connect to the device
        self.device.connect()

    @aetest.test
    def list_files(self):
        # execute a command to list all files in the current directory
        output = self.device.execute('ls -la')
        output_directory = 'TestLab/DataDump'
        file_path = os.path.join(output_directory, 'outputDateien.json')
        os.makedirs(output_directory, exist_ok=True)  # create an output directory if it does not exist
        data = {'output': output}
        # save the output in a JSON file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @aetest.test
    def list_arp_table(self):
        # execute a command to list the ARP table
        arp_output = self.device.execute('show arp')
        output_directory = 'TestLab/DataDump'
        arp_path = os.path.join(output_directory, 'arp_table.json')
        os.makedirs(output_directory, exist_ok=True)
        arp_data = {'arp_table': arp_output}
        # save the ARP table in a JSON file
        with open(arp_path, 'w') as file:
            json.dump(arp_data, file, indent=4)

    @aetest.cleanup
    def cleanup(self):
        # disconnect from the device
        self.device.disconnect()

if __name__ == '__main__':
    aetest.main()


