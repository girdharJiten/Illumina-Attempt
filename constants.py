# Manually define common protocol mappings
PROTOCOL_MAP = { 
    1: "icmp",
    2: "igmp",
    6: "tcp",
    17: "udp",
    47: "gre",
    50: "esp",
    51: "ah",
    132: "sctp"
}

LOG_FIELD_NAMES = ['version', 'account-Id', 'interface-id', 'srcaddr', 'dstaddr', 'srcport', 'dstport', 'protocol', 'packets', 'bytes', 'start', 'end', 'action', 'log-status']
