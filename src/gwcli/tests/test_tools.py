from gwcli.parsers import parse_lsbusb, parse_mount_paths


def test_parse_lsusb(fixture_loader):
    with fixture_loader.file('lsusb_stdout.txt') as fd:
        (vendor_id, device_id, vendor_name), = list(parse_lsbusb(fd))
        assert vendor_id == '091e'
        assert device_id == '4c9a'
        assert vendor_name == 'Garmin International'


def test_device_mount_path_finder(fixture_loader):
    with fixture_loader.file('lsusb_stdout.txt') as fd1:
        (vendor_id, device_id, vendor_name), = list(parse_lsbusb(fd1))
        with fixture_loader.file('ls_stdout.txt') as fd2:
            paths = list(parse_mount_paths(fd2, vendor_id, device_id))
            expect = '/var/run/user/1000/gvfs/mtp:host=091e_4c9a_0000c6b00a09'
            assert expect == paths[0]
            assert 'mtp:host=091e_4c9a_0000c6b00a09' == paths[1]



