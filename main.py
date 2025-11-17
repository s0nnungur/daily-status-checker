# subporocess - run system commands (ping)
# sokcet - resolves dns
# time - measure/pause time
# datetime - timestamp logs

import subprocess
import socket
import time
import os
from datetime import datetime
import json

def check_dns(host):
    try:
        start = time.time()
        ip = socket.gethostbyname(host)
        duration = round((time.time() - start) * 1000, 2)
        return True, ip, duration
    except Exception as e:
        return False, None, str(e)

def check_ping(host):
    try:
        start = time.time()
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "2000", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        duration = round((time.time() - start) * 1000, 2)

        if result.returncode == 0:
            return True, duration, result.stdout
        else:
            return False, None, result.stderr

    except Exception as e:
        return False, None, str(e)

    
def log_result(message):
    # if log directory missing
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    # filename creation based on current date
    filename = datetime.now().strftime("logs/%Y-%m-%d.txt")

    # timestamps
    timestamp = datetime.now().strftime("%H:%M:%S")

    # results
    with open(filename,"a") as f:
        f.write(f"[{timestamp}] {message}\n")

def check_target(host):
    # DNS CHECK
    dns_ok, ip, dns_info = check_dns(host)

    if dns_ok:
        log_result(f"DNS OK for {host} -> {ip} ({dns_info} ms)")
    else:
        log_result(f"DNS ERROR for {host} -> {dns_info}")
        return # STOP - no point ping if DNS fails
    
    # PING CHECK
    ping_ok, latency, info = check_ping(ip)

    if ping_ok:
        log_result(f"PING OK to {ip} -> {latency} ms")
    else:
        log_result(f"PING ERROR to {ip} -> {info}")


def main():

    with open("config.json", "r") as f:
        data = json.load(f)

    targets = data.get("targets", [])
    
    for host in targets:
        check_target(host)
    
if __name__ == "__main__":
   main()