import os
import subprocess
import sys
from typing import AnyStr, List


def lsusb() -> List[AnyStr]:
    out = subprocess.run(['lsusb'], capture_output=True).stdout
    return out.decode(sys.stdout.encoding).split(os.linesep)
