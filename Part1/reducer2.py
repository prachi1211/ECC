#!/usr/bin/env python3

import sys
from operator import itemgetter
from collections import defaultdict

ip_counts = defaultdict(int)


for line in sys.stdin:
    line = line.strip()
    hour, ip, count = line.split('\t', 2)
    count = int(count)
    ip_counts[ip] += count

sorted_ips = sorted(ip_counts.items(), key=itemgetter(1), reverse=True)
for ip, count in sorted_ips[:3]:
    print(f"IP: {ip}, Count: {count}")