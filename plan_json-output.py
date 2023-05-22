import requests
import os
import json

def get_plan_json(plan_id):
    
  """Gets the JSON output from the Terraform Cloud plan."""
  api_token = os.getenv('TF_API_TOKEN')
  url = "https://app.terraform.io/api/v2/plans/{}/json-output".format(plan_id)

  # Set your Terraform Cloud API token
  api_token = os.getenv('TF_API_TOKEN')
  headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/vnd.api+json",
  }

  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    return response.content.decode('UTF-8')
  else:
    raise Exception("Error getting plan info: {}".format(response.status_code))

if __name__ == "__main__":
  plan_id = "plan-CcWrgEdcZ7Rsq44W"
  plan_json = get_plan_json(plan_id)
  print(plan_json)