import requests
from bs4 import BeautifulSoup

url = 'https://huntscreens.com/en/category/just-launched'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Alt-Used': 'huntscreens.com',
    'Connection': 'keep-alive',
    'Cookie': 'NEXT_LOCALE=en',
    'Host': 'huntscreens.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Assuming the products are listed within a specific HTML structure, e.g., divs with a certain class
    products = soup.find_all('div', class_='product-item')  # Replace 'product-item' with the actual class or tag

    for product in products:
        # Extract product details, e.g., title, link, description, etc.
        title = product.find('h2', class_='product-title').get_text(strip=True) if product.find('h2', class_='product-title') else 'No title'
        link = product.find('a', class_='product-link')['href'] if product.find('a', class_='product-link') else 'No link'
        description = product.find('p', class_='product-description').get_text(strip=True) if product.find('p', class_='product-description') else 'No description'

        print(f'Title: {title}')
        print(f'Link: {link}')
        print(f'Description: {description}')
        print('---')
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
