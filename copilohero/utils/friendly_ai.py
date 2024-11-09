# utils/friendly_ai.py

import requests
from config.settings import Config
from instruction import Instruction
import logging

logger = logging.getLogger(__name__)

class FriendlyAiResponse:
    """
    This class handles sending tool outputs to the AI API for user-friendly, refined responses.
    """

    @staticmethod
    def get_friendly_response(user_query, tool_output):
        """
        Send the user's original query and tool output to the AI API for a refined response.

        Args:
            user_query (str): The original query from the user.
            tool_output (str): The raw output from the tool.

        Returns:
            str: A human-friendly, refined response from the AI model.
        """
        headers = {"Authorization": f"Bearer {Config.API_TOKEN}"}
        inputs = [
            {"role": "system", "content": Instruction.system_prompt()},
            {"role": "user", "content": f"User Query: {user_query}"},
            {"role": "assistant", "content": f"Tool Response: {tool_output}"}
        ]

        try:
            # Sending request to AI API for refined response
            response = requests.post(
                f"{Config.API_BASE_URL}@cf/meta/llama-3-8b-instruct",
                headers=headers,
                json={"messages": inputs}
            )
            response.raise_for_status()
            response_data = response.json()
            logger.debug(f"AI API response data: {response_data}")
            
            # Extract the AI-generated friendly response
            if response_data.get('success', False):
                return response_data['result']['response']
            else:
                logger.error(f"AI API response error: {response_data.get('errors')}")
                return "Oops! The AI could not process the request successfully."
        except requests.RequestException as e:
            logger.error(f"AI API request failed: {e}")
            return "Oops! Something went wrong while refining the response."
