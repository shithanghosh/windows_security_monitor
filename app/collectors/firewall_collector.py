from app.collectors.base import BaseCollector

class FirewallCollector(BaseCollector):
    def collect(self) -> dict:
        """
        Mocks the gathering of Windows Firewall profiles and status.
        Uses PowerShell/Registry adapters in production.
        """
        return {
            "module": "windows_firewall",
            "check_id": "WIN-FW-001",
            "observed_state": {
                "profile": "Public",
                "enabled": False,
                "inbound_rules": "BlockAll"
            }
        }
