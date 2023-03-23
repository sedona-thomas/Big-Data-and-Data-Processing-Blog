
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

files = ["data_processing_kumu.json", "tools.json"]


class KumuBluePrintDebugger(object):

    def __init__(self, file):
        '''
        :param file: The file to be checked.
        '''
        self.filepath = "{}/{}".format(os.getcwd(), file)
        print(self.filepath)
        print(os.path.exists(self.filepath))
        self.data = None

    def run(self):
        '''
        Runs the debugger.
        '''
        self._load_file()
        self._check_JSON_syntax()
        self._ensure_unique_ids()
        self._write_file()

    def _load_file(self):
        '''
        Loads the file into memory.
        '''
        f = open(self.filepath)
        for line in f:
            print(line)
        print(f)
        self.data = json.load(f)

        # list all directories with the os module
        # )

    def _check_JSON_syntax(self):
        '''
        Checks the JSON syntax.
        '''
        try:
            json.dumps(self.data)
        except ValueError as e:
            print(f"Error: {e}")
            exit()

    def _ensure_unique_ids(self):
        '''
        Kumu requires unique ids for elements and connections.
        This function ensures that the ids are unique.
        '''
        elements = self.data['elements']
        connections = self.data['connections']
        n = 0
        for element in elements:
            element["id"] = "e{}".format(n)
            n += 1
        n = 0
        for connection in connections:
            connection["id"] = "e{}".format(n)
            n += 1

    def _write_file(self):
        '''
        Writes the file to disk.
        '''
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f)


def main():
    for file in files:
        debugger = KumuBluePrintDebugger(file)
        debugger.run()


if __name__ == '__main__':
    main()
