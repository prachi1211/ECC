
import sys
from collections import defaultdict
from operator import itemgetter

hourly_ip_count = defaultdict(int)

start_hour, end_hour = map(int, sys.argv[1].split('-'))

for line in sys.stdin:
    line = line.strip()
    hour, ip, count = line.split('\t', 2)
    count = int(count)
    hour_int = int(hour[-2:])
    
    if start_hour <= hour_int < end_hour:
        hourly_ip_count[ip] += count

sorted_ips = sorted(hourly_ip_count.items(), key=itemgetter(1), reverse=True)[:3]
print(f"Top 3 IP address from {start_hour:02}:00:00 to {(end_hour-1):02}:59:59:")
for ip, count in sorted_ips:
    print(f"    IP: {ip}, Count: {count}")
