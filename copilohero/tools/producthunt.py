import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the webpage to scrape
url = "https://www.producthunt.com/leaderboard/daily/2024/11/7/all"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all product items
products = soup.find_all('div', class_='styles_item__Dk_nz')

product_info = []

for product in products:
    title = product.find('strong').get_text(strip=True)
    votes = product.find('div', class_='styles_voteCountItem__zwuqk').get_text(strip=True)
    
    # Locate description more precisely by finding the 'a' tag with description content
    description_tag = product.find('a', class_='text-14 sm:text-16 md:text-16 font-normal text-dark-gray styles_noOfLines-2__k_Ta_ styles_titleTaglineItem__d5Rut block')
    description_text = description_tag.get_text(strip=True) if description_tag else ""
        
    # Split on the first occurrence of '—' to separate title and description
    description = description_text.split('—', 1)[-1].strip() if '—' in description_text else description_text
    
    link = urljoin(url, product.find('a')['href'])
    
    # Extract image or video poster
    image_tag = product.find('img')
    image = image_tag['src'] if image_tag else product.find('video').get('poster', '') if product.find('video') else ''
    
    # Extract tags
    tags = [tag.get_text(strip=True) for tag in product.find_all('a', class_='styles_underlinedLink__MUPq8')]

    # Append collected data to product_info
    product_info.append({
        'title': title,
        'votes': votes,
        'description': description,
        'link': link,
        'image': image,
        'tags': tags
    })

# Output each product's information
for product in product_info:
    print("Title:", product['title'])
    print("Votes:", product['votes'])
    print("Description:", product['description'])
    print("Link:", product['link'])
    print("Image:", product['image'])
    print("Tags:", product['tags'])
    print("\n")
