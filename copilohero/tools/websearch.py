import logging
from googlesearch import search

logger = logging.getLogger(__name__)

class WebSearcher:
    def __init__(self, sleep_interval=1, num_results=10):
        self.sleep_interval = sleep_interval
        self.num_results = num_results

    def google_search(self, query):
        try:
            search_results = search(query,
                                    sleep_interval=self.sleep_interval,
                                    num_results=self.num_results,
                                    advanced=True)
            return search_results
        except Exception as e:
            logger.error(f"Error performing Google search: {e}")
            return []

    def format_search_results(self, search_results):
        formatted_results = []
        for result in search_results:
            formatted_result = {
                "title": result.title,
                "url": result.url,
                "description": result.description
            }
            formatted_results.append(formatted_result)
        return formatted_results

    def perform_search(self, query):
        search_results = self.google_search(query)
        formatted_results = self.format_search_results(search_results)
        return formatted_results

# Example usage
if __name__ == "__main__":
    searcher = WebSearcher(sleep_interval=1, num_results=5)
    query = "What's the weather in London now?"
    results = searcher.perform_search(query)
    for result in results:
        print(f"Title: {result['title']}")
        print(f"URL: {result['url']}")
        print(f"Description: {result['description']}")
        print("-" * 40)
