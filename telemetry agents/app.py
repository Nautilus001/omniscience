#get all info
import subprocess
from status import Status
from container import Container
import requests

url = "https://omni.nautilius.com/api/"

payload = {
    
}

result = subprocess.getoutput(
    ["docker", "ps", "--format", "'{{.ID}} {{.Image}} {{.Names}} {{.Status}}'"],
)

print(result)

containers = Container.readContainers(result.lower().split("\n"))

for container in containers:
    payload[container.id] = {
        "name": container.name,
        "image": container.image,
        "status": container.status
    }

print(payload)

try:
    response = requests.post(url, json=payload, timeout=5)

    response.raise_for_status()

    print("Telemetry sent successfully!")
    print("Server response: ", response.json())

except requests.exceptions.RequestException as e:
    print(f"Failed to send telementry: {e}")





