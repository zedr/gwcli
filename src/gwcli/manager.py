import os
from typing import Generator, AnyStr
from pathlib import Path

from gwcli import parsers, tools


class Manager:
    """The Device Manager."""

    @classmethod
    def get_mount_paths(cls) -> Generator[AnyStr, None, None]:
        """Get the local mount paths of any compatible devices."""
        for (vendor_id, device_id, _) in parsers.parse_lsbusb(tools.lsusb()):
            base_path = Path('/var/run/user/') / str(os.getuid()) / 'gvfs'
            dirs = (str(pth) for pth in base_path.glob('*'))
            for path in parsers.parse_mount_paths(dirs, vendor_id, device_id):
                yield path

