from django.test import TestCase
from .models import DeviceType, User, Device, DeviceStatus
from django.utils import dateparse
import pytz


class DeviceTestCase(TestCase):
    def setUp(self):
        notebook = DeviceType.objects.create(name='Notebook')
        johnny = User.objects.create(first_name='John', last_name='Doe', username='Johnny')
        Device.objects.create(mac_address='5F:B4:9F:07:D1:E5', device_name='Hermes', device_type=notebook, user=johnny)

    def test_device_has_been_created(self):
        """One device type, a user and one of his devices correctly identified"""
        # Exactly one device should exist
        found_devices = Device.objects.all()
        self.assertEqual(len(found_devices), 1)

        # The device should be equal to Hermes
        hermes = found_devices[0]
        self.assertEqual(hermes.mac_address, '5F:B4:9F:07:D1:E5')
        self.assertEqual(hermes.device_name, 'Hermes')

        # The device user should be equal to Johnny
        johnny = hermes.user
        self.assertEqual(johnny.first_name, 'John')
        self.assertEqual(johnny.last_name, 'Doe')
        self.assertEqual(johnny.username, 'Johnny')

        # The device type should be equal to the notebook type
        notebook = hermes.device_type
        self.assertEqual(notebook.name, 'Notebook')

    def test_find_latest_device_status(self):
        """The device status with the most recent timestamp is the latest one"""
        device = Device.objects.filter(mac_address='5F:B4:9F:07:D1:E5')[0]

        # Add first status for the device
        first_timestamp_from_somewhere = '2015-10-13 19:44:51.008230+01:00'
        first_timestamp = dateparse.parse_datetime(first_timestamp_from_somewhere).astimezone(pytz.utc)
        DeviceStatus.objects.create(device=device, timestamp=first_timestamp)

        # Add second status for the device
        second_timestamp_from_somewhere = '2015-10-13 19:44:52.008230+01:00'
        second_timestamp = dateparse.parse_datetime(second_timestamp_from_somewhere).astimezone(pytz.utc)
        DeviceStatus.objects.create(device=device, timestamp=second_timestamp)

        # Get latest status for this device
        latest_status = DeviceStatus.objects.latest(field_name='timestamp')
        self.assertEqual(latest_status.timestamp, second_timestamp)
