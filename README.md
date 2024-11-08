# CopiloHero

**CopiloHero** is a dynamic tool aggregator that utilizes Cloudflare's AI Function Calling to provide various functionalities like GitHub user info retrieval, stock analysis, and web scraping. It leverages multiple APIs and web scraping tools to fetch real-time information, offering a robust integration with Cloudflare’s Function Calling capabilities.

## 🚀 Features

- **Cloudflare AI Integration**: Dynamically call functions using Cloudflare's AI model with tool descriptions.
- **GitHub User Info**: Fetch public details of GitHub users.
- **Stock Analysis**: Retrieve real-time stock data, company profiles, and analyst recommendations.
- **Web Scraping**: Extract visible text and metadata from webpages.
- **Product Hunt Leaderboard**: Get the latest trending products on Product Hunt.
- **Web Search**: Perform Google search and retrieve top results.

## 🛠️ Setup

### Prerequisites

- **Python 3.8+**
- **ChromeDriver** installed for Selenium usage.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/gladsonchala/copilohero.git
   cd copilohero
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - Copy the `.env.sample` to `.env`:
     ```bash
     cp .env.sample .env
     ```
   - Update the `.env` file with your Cloudflare `ACCOUNT_ID` and `API_TOKEN`.

### Example `.env` File:
   ```
   ACCOUNT_ID=your_account_id_here
   API_TOKEN=your_api_token_here
   MODEL_NAME=@hf/nousresearch/hermes-2-pro-mistral-7b
   ```

## ⚙️ Usage

1. **Run the Main Script**:
   ```bash
   python main.py
   ```

2. **Example Query**:
   - Retrieve GitHub user info:
     ```python
     user_query = "Get information about the GitHub user 'octocat'."
     ```

3. **Cloudflare API Integration**:
   - The application utilizes Cloudflare’s Function Calling to dynamically choose tools based on the user query. This ensures a seamless and context-aware response.

## 🧩 Available Tools

- **GitHub User Info**: Fetch GitHub user details.
- **Stock Info**: Get current stock prices and company profiles.
- **Web Search**: Perform Google searches and fetch results.
- **Web Scraping**: Extract text from a given URL.
- **Product Hunt**: Retrieve trending products from Product Hunt’s daily leaderboard.

## 📈 Contributing

Feel free to fork this project, open issues, and submit PRs. Contributions are welcome!

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 📧 Contact

For any inquiries, please contact: [gladsonchala@gmail.com](mailto:gladsonchala@gmail.com)