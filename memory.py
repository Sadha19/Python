import psutil
from datetime import timedelta

def cpu_time():
    cpu_times = psutil.cpu_times()

    return{
        k: str(timedelta(seconds=v))
        for k, v in cpu_times._asdict(). items()
         }    

print(cpu_time())

def memory_usage():
    mem = psutil.virtual_memory()
    return {
        k: f"{v / (1024 ** 3):.2f} GB"
        for k, v in mem._asdict().items()
    }

print(memory_usage())

def disk_usage():
    disk = psutil.disk_usage('/')
    return {
        k :f"{v / (1024 ** 3): .2f} GB"
        for k, v in disk._asdict().items()
    }

print(disk_usage())

print(f" Disk Used: {disk_usage()['free']}")