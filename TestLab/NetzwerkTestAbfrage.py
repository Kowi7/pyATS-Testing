import os
import json
from genie.testbed import load
from pyats import aetest


class CheckFiles(aetest.Testcase):
    @aetest.setup
    def setup(self):
        # Laden des Testbeds aus einer Datei
        self.testbed = load('TestLab/testbed.yaml')
        # Zugriff auf ein spezifisches Gerät
        self.device = self.testbed.devices['my_device']
        # Verbinden mit dem Gerät
        self.device.connect()

    @aetest.test
    def list_files(self):
        # Ausführen des 'ls -la' Befehl aus, um die Dateiliste zu erhalten
        output = self.device.execute('ls -la')
        output_directory = 'TestLab/DataDump'
        file_path = os.path.join(output_directory, 'outputDateien.json')
        os.makedirs(output_directory, exist_ok=True)  # Erstellt den Ordner, falls er nicht existieren sollte
        data = {'output': output}
        # Speichern der Daten in einer JSON-Datei
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @aetest.test
    def list_arp_table(self):
        # Ausführen des ARP-Befehls, um die ARP-Tabelle zu erhalten
        arp_output = self.device.execute('show arp')
        output_directory = 'TestLab/DataDump'
        arp_path = os.path.join(output_directory, 'arp_table.json')
        os.makedirs(output_directory, exist_ok=True)
        arp_data = {'arp_table': arp_output}
        # Speichern der ARP-Tabelle in einer JSON-Datei
        with open(arp_path, 'w') as file:
            json.dump(arp_data, file, indent=4)

    @aetest.cleanup
    def cleanup(self):
        # Trennen der Verbindung
        self.device.disconnect()

if __name__ == '__main__':
    aetest.main()


