class Container:
    def __init__(self, id, image, name, status):
        self.name = name
        self.id = id
        self.image = image
        self.status = status

    def __str__(self):
        str = f'''
            {self.name}: {self.status}
        '''
        return str

    def readContainers(lines):
        containers = []
        print(lines)
        for line in lines:
            print(line)
            entries = line.split(" ")
            if "up" in entries[3]:
                containers.append(Container(entries[0], entries[1], entries[2], "up"))
            else:
                containers.append(Container(entries[0], entries[1], entries[2], "down"))
        return containers

    def checkStatus(self):
        return
    
    def setCustomCheckStatus(args): #pass in custom bash command to be executed to check the status. results piped directly into JSON response/push
        return
