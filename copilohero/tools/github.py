# tools/github.py

import requests
from tools.base_tool import BaseTool

class GitHubTool(BaseTool):
    """
    Fetches publicly available information about a GitHub user.
    """

    def invoke(self, input: dict) -> dict:
        username = input.get("username")
        if not username:
            return {"error": "Username parameter is required."}

        try:
            response = requests.get(f"https://api.github.com/users/{username}")
            if response.status_code == 200:
                return response.json()
            return {"error": f"GitHub user not found, status code: {response.status_code}"}
        except Exception as e:
            return {"error": f"Exception fetching GitHub user data: {str(e)}"}

    def get_schema(self) -> dict:
        """
        Returns the JSON schema for the GitHub tool's input parameters.
        """
        return {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": "The GitHub username to fetch information for."
                }
            },
            "required": ["username"]
        }
