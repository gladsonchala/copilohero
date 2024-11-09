from googlesearch import search

class GoogleSearchHandler:
    def __init__(self, sleep_interval, results):
        self.sleep_interval = sleep_interval
        self.results = results

    def google_search(self, query):
        return search(query,
                      sleep_interval=self.sleep_interval,
                      num_results=self.results,
                      advanced=True)

# Example usage
if __name__ == "__main__":
    # Initialize the GoogleSearchHandler with a sleep interval of 2 seconds and 10 results
    handler = GoogleSearchHandler(sleep_interval=2, results=10)

    # Perform a Google search for the query "Python programming"
    query = "Python programming"
    results = handler.google_search(query)

    # Print the search results
    for result in results:
        print(result)
