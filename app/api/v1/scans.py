from fastapi import APIRouter
from app.collectors.system_collector import SystemCollector
from app.collectors.firewall_collector import FirewallCollector

router = APIRouter()

@router.post('/scans/start')
def start_scan():
    """
    Initiates the data collection from the active modules.
    """
    sys_collector = SystemCollector()
    fw_collector = FirewallCollector()
    
    sys_evidence = sys_collector.collect()
    fw_evidence = fw_collector.collect()
    
    return {
        'message': 'Baseline scan initiated',
        'evidence_collected': [sys_evidence, fw_evidence]
    }
