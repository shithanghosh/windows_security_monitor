import platform
from app.collectors.base import BaseCollector

class SystemCollector(BaseCollector):
    def collect(self) -> dict:
        """
        Gathers OS version, build, architecture, and device details.
        """
        return {
            "module": "system_inventory",
            "check_id": "WIN-SYS-001",
            "observed_state": {
                "os": platform.system(),
                "release": platform.release(),
                "version": platform.version(),
                "architecture": platform.machine(),
                "node": platform.node()
            }
        }
