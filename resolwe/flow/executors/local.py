"""Local workflow executor."""
from __future__ import absolute_import, division, print_function, unicode_literals

import logging
import os
import shlex
import subprocess
import time

from resolwe.flow.executors import BaseFlowExecutor

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class FlowExecutor(BaseFlowExecutor):
    """Local dataflow executor proxy."""

    name = 'local'

    def __init__(self, *args, **kwargs):
        """Initialize attributes."""
        super(FlowExecutor, self).__init__(*args, **kwargs)

        self.processes = {}
        self.kill_delay = 5
        self.proc = None
        self.stdout = None
        self.command = '/bin/bash'

    def start(self):
        """Start process execution."""
        self.proc = subprocess.Popen(shlex.split(self.command),
                                     stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT, universal_newlines=True)

        self.processes[self.data_id] = self.proc
        self.stdout = self.proc.stdout

        return self.proc.pid

    def run_script(self, script):
        """Execute the script and save results."""
        self.proc.stdin.write(os.linesep.join(['set -x', 'set +B', script, 'exit']) + os.linesep)
        self.proc.stdin.close()

    def end(self):
        """End process execution."""
        self.proc.wait()

        return self.proc.returncode

    def terminate(self, data_id):
        """Terminate a running script."""
        proc = self.processes[data_id]
        proc.terminate()

        time.sleep(self.kill_delay)
        if proc.poll() is None:
            proc.kill()
