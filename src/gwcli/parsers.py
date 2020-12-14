import re
from typing import Tuple, AnyStr, Generator, Iterator

lsusb_lint_rxp = re.compile(r'.+ ID (\w{4}):(\w{4}) (Garmin ?.+)')


def parse_lsbusb(fd: Iterator) -> Generator[Tuple[AnyStr, AnyStr, AnyStr], None, None]:
    """Parse lsbusb output and yield any Garmin device info."""
    for line in fd:
        match = lsusb_lint_rxp.match(line)
        if match:
            yield match.groups()


def parse_mount_paths(lines: Generator[AnyStr, None, None],
                     vendor_id: AnyStr,
                     device_id: AnyStr) -> Generator[AnyStr, None, None]:
    """Parse the correct MTP home paths for the device."""
    mtp_mount_rxp = re.compile(
        r'((.*/)?mtp:host={}_{}.+)'.format(vendor_id, device_id)
    )
    for line in lines:
        match = mtp_mount_rxp.match(line)
        if match:
            yield match.groups()[0]


