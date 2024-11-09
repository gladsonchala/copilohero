# tools/tool_manager.py

import requests
from config.settings import Config
from utils.friendly_ai import FriendlyAiResponse
from tools.github import GitHubTool
from tools.stock import StockTool
from tools.websearch import WebSearchTool
from tools.crawler import CrawlerTool
from tools.producthunt import ProductHuntTool
from tools.screenshoter import ScreenshotTool
from tools.translator import TranslatorTool
from tools.generic_ai_response import GenericAiResponseTool

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
            "translateText": TranslatorTool(),
            "genericAiResponse": GenericAiResponseTool(),
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
        Process the user query by calling Cloudflare's API and handle both tool calls and direct responses.
        """
        payload = {
            "messages": [{"role": "user", "content": user_query}],
            "tools": self.prepare_tools_schema(),
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_token}",
        }

        try:
            # Call Cloudflare API to determine response
            response = requests.post(self.url, json=payload, headers=headers)
            response.raise_for_status()
            # print(response.text)

            data = response.json()
            result = data.get("result", {})

            # Handle tool calls if present
            tool_calls = result.get("tool_calls", [])
            if tool_calls:
                for tool_call in tool_calls:
                    tool_name = tool_call.get("name")
                    arguments = tool_call.get("arguments", {})
                    raw_tool_output = self.call_tool(tool_name, arguments)

                    # Use AI to refine the tool's output for user-friendly response
                    friendly_response = FriendlyAiResponse.get_friendly_response(
                        user_query=user_query,
                        tool_output=str(raw_tool_output)
                    )
                    print(f"{friendly_response}")
                return

            # Check for direct AI response
            ai_response = result.get("response", None)
            if ai_response:
                print(f"{ai_response}")
            else:
                print("No direct response from AI.")

        except Exception as e:
            print(f"Error processing query: {str(e)}")



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
