import os
import random

# Return CPU temperature as a character string                                     

def getCPUtemp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = round(float(tempFile.read()) / 1000, 1)
    tempFile.close()
    return cpu_temp   
# Return RAM information (unit=kb) in a list                                      
# Index 0: total RAM                                                              
# Index 1: used RAM                                                                
# Index 2: free RAM                                                                
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])
  
# Return % of CPU used by user as a character string                               
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))
  
# Return information about disk space as a list (unit included)                    
# Index 0: total disk space                                                        
# Index 1: used disk space                                                        
# Index 2: remaining disk space                                                    
# Index 3: percentage of disk used                                                 
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])
  

def getUpTime():
    
    res = float(os.popen("cat /proc/uptime").readline().split()[0])
    return(round(res / 60))
#     


def get_pi_info():
    # CPU informatiom
    CPU_temp = getCPUtemp()
    CPU_usage = float(getCPUuse())
    UP_time = getUpTime() 

    # RAM information
    # Output is in kb, here I convert it in Mb for readability
    RAM_stats = getRAMinfo()
    RAM_total = round(int(RAM_stats[0]) / 1000,1)
    RAM_used = round(int(RAM_stats[1]) / 1000,1)
    RAM_free = round(int(RAM_stats[2]) / 1000,1)
    
    # Disk information
    DISK_stats = getDiskSpace()
    DISK_total = DISK_stats[0]
    DISK_used = DISK_stats[1]
    DISK_remain = float(DISK_stats[2].strip('G'))
    DISK_perc = DISK_stats[3]

    pdata = {
        'cpu_temperature': CPU_temp,
        'cpu_usage': CPU_usage,
        'remain_storage': DISK_remain,
        'UpTime': UP_time
        }
    return pdata

if __name__ == '__main__':
    print(get_pi_info())
    
