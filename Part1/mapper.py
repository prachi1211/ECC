#!/usr/bin/env python3

import sys
import re
from datetime import datetime


pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) .* \[(?P<timestamp>[^\]]+)\]')

for line in sys.stdin:
    match = pattern.search(line.strip())
    if match:
        ip = match.group('ip')
        timestamp_str = match.group('timestamp').split()[0] 
        try:
            timestamp = datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S")
            hour = timestamp.strftime("%H")
            print(f"{hour}\t{ip}\t1") 
        except ValueError:
            pass
