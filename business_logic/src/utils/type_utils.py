

def get_type_devices(device_records_list):
    devices_list = []
    for device in device_records_list:
        devices_list.append(
            {
                'device_id': device['id'],
                'devicename': device['name']
            }
        )
    return devices_list
