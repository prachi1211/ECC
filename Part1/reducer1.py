#!/usr/bin/env python3

import sys
from operator import itemgetter
from collections import defaultdict
from datetime import datetime, timedelta

hourly_ip_count = defaultdict(lambda: defaultdict(int))

for line in sys.stdin:
    hour, ip, count = line.strip().split('\t', 2)
    count = int(count)
    hourly_ip_count[hour][ip] += count


for hour, ip_counts in hourly_ip_count.items():
    start_time = datetime.strptime(hour, "%H")
    end_time = start_time + timedelta(hours=1) - timedelta(seconds=1)
    hour_range = f"{start_time.strftime('%H:%M:%S')} to {end_time.strftime('%H:%M:%S')}"
    sorted_ips = sorted(ip_counts.items(), key=itemgetter(1), reverse=True)
    top_3_ips = sorted_ips[:3]
    print(f"Top 3 IP address from {hour_range}:")
    for ip, count in top_3_ips:
        print(f"IP: {ip}, Count: {count}")
