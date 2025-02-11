from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://github.com/rasoolmahmoodzadeh/sniper/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "BLETest.mpy")

ota_updater.download_and_install_update_if_available()
