import psutil

class Status:
    def __init__(self):
        self.cpuPercent = 0
        self.vmemPercent = 0
        self.diskPercent = 0

    def updateCPU(self):
        self.cpuPercent = psutil.cpu_percent(interval=1)

    def updateDisk(self): 
        self.diskPercent = psutil.disk_usage('/')

    def updateVMem(self):
        self.memPercent = psutil.virtual_memory()

    def buildStatus(self):
        return {
            "cpu": self.cpuPercent,
            "memory": self.vmemPercent,
            "disk": self.diskPercent,
        }