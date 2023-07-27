import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

def crawl_naver_blog(url):
    # Send a GET request to the provided URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all blog post elements
    blog_posts = soup.find_all('li', class_='bx')
    
    results = []
    for post in blog_posts:
        try:
            # Extract the blog address, post title, and posting date
            blog_address = unquote(post.find('a')['href'].split('url=')[1])
            post_title = post.find('a', class_='api_txt_lines total_tit').text
            post_date = post.find('span', class_='sub_time').text.strip()
            
            results.append({
                'blog_address': blog_address,
                'post_title': post_title,
                'post_date': post_date
            })
        except Exception as e:
            # Handle exceptions if any element is missing
            print("Error:", e)
    
    return results

if __name__ == "__main__":
    search_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query={%EB%A7%A5%EB%B6%81%EC%97%90%EC%96%B4}"
    search_results = crawl_naver_blog(search_url)
    
    for idx, result in enumerate(search_results, 1):
        print(f"Result {idx}:")
        print("Blog Address:", result['blog_address'])
        print("Post Title:", result['post_title'])
        print("Post Date:", result['post_date'])
        print()
