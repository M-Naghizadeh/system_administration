#####monitoring cpu
import psutil

## o
psutil.cpu_count()

psutil.cpu_count(logical = False)

## return system cpu times

psutil.cpu_times()

psutil.cpu_times(percpu = True)

## return cpu utilization as a percentage   

psutil.cpu_percent(interval = 1)  #for system cpu

psutil.cpu_percent(interval = 1, percpu = True) #for each cpu

mydata = []     #for each cpu with one seconds between calls
for x in range(50):
    mydata.append(psutil.cpu_percent(interval = 1, percpu = True))


## visualize the percentage usage of the cpu

mydata

import pandas as pd

mydf = pd.DataFrame(mydata)

%matplotlib

import matplotlib.pyplot as plt

plt.hist(mydf[0])

mydata

mydf = pd.DataFrame(mydata)

plt.hist(mydf[1])

import seaborn as sns

sns.kdeplot(mydf[1])

##

psutil.cpu_times_percent()

psutil.cpu_times_percent(interval = 1, percpu = True)

mydata = []
for i in range(3):
    mydata.append(psutil.cpu_times_percent(interval = 1, percpu= True))
mydata

##Various cpu statistics
psutil.cpu_stats()

##cpu frequency
psutil.cpu_freq()

psutil.cpu_freq(percpu = True)

##average system load over the last 1,5 and 15 min

psutil.getloadavg()

import os
os.getloadavg()

# get percentage
[x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
##

#####


#####Monitoring system memory

psutil.virtual_memory()

mem= psutil.virtual_memory()
mem.available

threshold = 100 * 1024 *1024 #100MB

if mem.available <= threshold:
    print('warning')

psutil.swap_memory()
#####

#####Monitoring disks

psutil.disk_partitions()


psutil.disk_usage('/')

psutil.disk_io_counters(perdisk = False)

#####

#####Monitoring system network

psutil.net_io_counters()

psutil.net_io_counters(pernic = True)

psutil.net_connections(kind = 'inet')

for d in psutil.net_connections(kind = 'inet'):
    print(d.laddr)

for d in psutil.net_connections(kind = 'inet'):
    print(d.pid)

psutil.net_if_addrs()

psutil.net_if_stats()
#####


#####Monitoring system sensors

psutil.sensors_temperatures()

psutil.sensors_fans()

psutil.sensors_battery()

#####


#####Monitoring other system info

##boot time
psutil.boot_time()

import datetime

datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')


psutil.users()

##

##Process management

psutil.pids()

list(psutil.process_iter())

list(psutil.process_iter(['pid', 'name', 'username']))

for process in psutil.process_iter(['pid','name', 'username']):
    print(process.info)

p = psutil.Process(5394)

p.exe()

p.cwd()

p.pid

p.children()

p.parent()

p.parents()

p.status()

p.terminal()

p.username()

p.uids()

p.gids()

p.cpu_times()

psutil.pid_exists(5394)

p.cpu_affinity()

p.memory_percent()

p.memory_info()

p.memory_full_info()

p.memory_maps()

p.memory_percent()

p.io_counters()

p.open_files()

p.connections()

p.num_threads()

p.num_fds()

p.nice()

p.is_running()

p.terminate()

p.kill()

p.wait()

p.suspend()

psutil.test()

##

##popen

from subprocess import PIPE
p = psutil.Popen(['/usr/bin/python3', '-c', 'print("hello")'], stdout = PIPE)

p.communicate()

p.name()

###
#####


