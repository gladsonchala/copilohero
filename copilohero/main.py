# main.py

from tools.tool_manager import ToolManager
from config.settings import Config

def main():
    print("Welcome to CopiloHero! You can ask queries like:")
    print("1. Get information about a GitHub user 'octocat'.")
    print("2. Get the current stock price of 'AAPL'.")
    print("3. Capture a screenshot of a webpage 'https://example.com'.")
    print("4. Fetch trending products from Product Hunt.")
    print("5. Perform a Google search query.")
    
    user_query = input("Enter your question: ")
    
    # Initialize the Tool Manager
    tool_manager = ToolManager()
    print("Processing your query with Cloudflare AI Function Calling...")
    
    # Process the query using Cloudflare's API
    tool_manager.process_query(user_query)

if __name__ == "__main__":
    Config.validate()  # Ensure configuration is loaded properly
    main()
