#!/usr/bin/env python

import os
import platform
import subprocess
import socket
import psutil
import netifaces
import cpuinfo

# Command to get CPU info using subprocess is commented out as it is not needed anymore

kb = float(1024)
mb = float(kb ** 2)
gb = float(kb ** 3)

memTotal = int(psutil.virtual_memory().total / gb)
memFree = int(psutil.virtual_memory().available / gb)
memUsed = int(psutil.virtual_memory().used / gb)
memPercent = int(psutil.virtual_memory().percent)
storageTotal = int(psutil.disk_usage('/').total / gb)
storageUsed = int(psutil.disk_usage('/').used / gb)
storageFree = int(psutil.disk_usage('/').free / gb)
storagePercent = int(psutil.disk_usage('/').percent)

info = platform.processor()

def service():
    print()
    pidTotal = len(psutil.pids())
    print("Running processes: ", pidTotal)


def system():
    core_count = os.cpu_count()
    host_name = socket.gethostname()
    print()
    print('---------- System Info ----------')
    print()
    print("Hostname:", host_name)
    print("System:", platform.system(), platform.machine())
    print("Kernel:", platform.release())
    print('Compiler:', platform.python_compiler())
    print('CPU:', info, core_count, "(Core)")
    print("Memory:", memTotal, "GiB")
    print("Disk:", storageTotal, "GiB")

def memory():
    print()
    print('---------- RAM & Disk Usage ----------')
    print()
    print("RAM Used:", memUsed, "GiB /", memTotal, "GiB", "(", memPercent, "%", ")")
    print("Disk Used:", storageUsed, "GiB /", storageTotal, "GiB", "(", storagePercent, "%", ")")

def network():
    default_gateway = netifaces.gateways()['default'][netifaces.AF_INET][1]
    speed = psutil.net_io_counters(pernic=False)
    packets_sent = round(speed.bytes_sent / kb, 2)
    packets_received = round(speed.bytes_recv / kb, 2)

    print()
    print('---------- Network Stats ----------')
    print()

    print("Active interface:", default_gateway)
    print("Packets sent:", packets_sent, "KiB/s")
    print("Packets received:", packets_received, "KiB/s")

def main():
    service()
    system()
    memory()
    network()

main()
