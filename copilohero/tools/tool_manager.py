# tools/tool_manager.py

import requests
from config.settings import Config
from tools.github import GitHubTool
from tools.stock import StockTool
from tools.websearch import WebSearchTool
from tools.crawler import CrawlerTool
from tools.producthunt import ProductHuntTool
from tools.screenshoter import ScreenshotTool

class ToolManager:
    def __init__(self):
        self.account_id = Config.ACCOUNT_ID
        self.api_token = Config.API_TOKEN
        self.url = Config.CLOUDFLARE_API_URL

        # Initialize available tools
        self.tool_mapping = self.load_tools()

    def load_tools(self):
        """
        Load all available tools into the tool mapping.
        """
        return {
            "getGithubUser": GitHubTool(),
            "getCurrentStockPrice": StockTool(),
            "performWebSearch": WebSearchTool(),
            "scrapeVisibleText": CrawlerTool(),
            "getProductHuntTrending": ProductHuntTool(),
            "takeScreenshotOfWebPage": ScreenshotTool(),
        }

    def prepare_tools_schema(self):
        """
        Prepare the tools schema for Cloudflare Function Calling.
        """
        tools_schema = []
        for tool_name, tool_instance in self.tool_mapping.items():
            tools_schema.append({
                "name": tool_name,
                "description": tool_instance.__doc__,
                "parameters": tool_instance.get_schema()
            })
        return tools_schema

    def process_query(self, user_query):
        """
        Process the user query by calling Cloudflare's API.
        """
        payload = {
            "messages": [{"role": "user", "content": user_query}],
            "tools": self.prepare_tools_schema(),
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_token}",
        }

        # Make a POST request to Cloudflare API
        response = requests.post(self.url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            tool_calls = data.get("result", {}).get("tool_calls", [])

            # Iterate over the tool calls and invoke corresponding tools
            for tool_call in tool_calls:
                tool_name = tool_call.get("name")
                arguments = tool_call.get("arguments", {})
                result = self.call_tool(tool_name, arguments)
                print(f"Result from {tool_name}: {result}")
        else:
            print(f"Error calling Cloudflare API: {response.status_code} - {response.text}")

    def call_tool(self, tool_name, arguments):
        """
        Invoke the corresponding tool function based on the tool name.

        Args:
            tool_name (str): Name of the tool to call.
            arguments (dict): Arguments to pass to the tool.

        Returns:
            dict: Result from the tool function.
        """
        tool_instance = self.tool_mapping.get(tool_name)
        if tool_instance:
            try:
                return tool_instance.invoke(arguments)
            except Exception as e:
                return {"error": f"Failed to invoke tool '{tool_name}': {str(e)}"}
        return {"error": f"Tool '{tool_name}' not found."}
