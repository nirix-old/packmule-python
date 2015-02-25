"""
Copyright 2015 Jack Polgar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import shutil
import subprocess
import tempfile
from packmule.util import cd


class Archiver():
    def __init__(self, options):
        self.options = options
        self.cwd = os.getcwd()

    def pack(self):
        self.create_tmpdir()
        self.run_commands()
        self.remove_files()
        self.create_archives()
        self.cleanup()

    def create_tmpdir(self):
        self.tmpdir = self.cwd + "/packmule_tmp"
        shutil.copytree(self.cwd, self.tmpdir)

    def run_commands(self):
        with cd(self.tmpdir):
            for command in self.options['commands']:
                subprocess.call(command, shell=True)

    def remove_files(self):
        print("remove_files: not yet implemented")

    def create_archives(self):
        for format in self.options['formats']:
            if format == "zip":
                shutil.make_archive(self.cwd + self.options['package-as'],
                                    'zip', self.tmpdir)
            elif format == "tar":
                shutil.make_archive(self.cwd + self.options['package-as'],
                                    'tar', self.tmpdir)
            elif format == "tar.gz":
                shutil.make_archive(self.cwd + self.options['package-as'],
                                    'gztar', self.tmpdir)
            elif format == "tar.bz2":
                shutil.make_archive(self.cwd + self.options['package-as'],
                                    'bztar', self.tmpdir)

    def cleanup(self):
        shutil.rmtree(self.tmpdir)
