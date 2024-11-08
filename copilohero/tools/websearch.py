# tools/websearch.py

import logging
from googlesearch import search
from tools.base_tool import BaseTool

logger = logging.getLogger(__name__)

class WebSearchTool(BaseTool):
    """
    Performs a Google search and retrieves top results based on the query.
    """

    def invoke(self, input: dict) -> dict:
        query = input.get("query")
        num_results = input.get("num_results", 5)

        if not query:
            return {"error": "Query parameter is required."}

        try:
            # Perform Google search
            search_results = search(query, num_results=num_results)
            formatted_results = [
                {"title": result.title, "url": result.url, "description": result.description}
                for result in search_results
            ]
            return {"results": formatted_results}
        except Exception as e:
            logger.error(f"Error performing Google search: {str(e)}")
            return {"error": f"Exception during search: {str(e)}"}

    def get_schema(self) -> dict:
        """
        Returns the JSON schema for the web search tool's input parameters.
        """
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to perform."
                },
                "num_results": {
                    "type": "integer",
                    "description": "The number of search results to retrieve.",
                    "default": 5
                }
            },
            "required": ["query"]
        }
