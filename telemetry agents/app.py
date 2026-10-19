#get all info
import subprocess
from status import Status
from container import Container
import requests

url = "https://omni.nautilius.online/graphql/"
PROJECT_ID = 1

result = subprocess.getoutput(
    ["docker", "ps", "--format", "'{{.ID}} {{.Image}} {{.Names}} {{.Status}}'"],
)

print(result)

containers = Container.readContainers(result.lower().split("\n"))

mutation = """
mutation ReportContainer($name: String!, $image: String!, $status: Boolean!, $projectId: Int!) {
    upsertContainer(name: $name, image: $image, status: $status, projectId: $projectId) {
        container {
            id
            name
            status
        }
    }
}
"""

for container in containers:
    variables = {
        "name": container.name,
        "image": container.image,
        "status": container.status,
        "projectId": PROJECT_ID
    }

    try: 
        response = requests.post(
            url,
            json = {
                'query': mutation, 
                'variables': variables
            }
        )
        res_data = response.json()

        if "errors" in res_data:
            print(f"Failed to report {container.name}: {res_data['errors']}")
        else:
            saved_container = res_data['data']['upsertContainer']['container']
            print(f"Synced: {saved_container['name']} (ID: {saved_container['id']})")
    except Exception as e:
        print(f"Failed with: {e}")







