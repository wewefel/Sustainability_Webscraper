import os
import argparse
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
from tqdm import tqdm


class ScraperHelper:
    @staticmethod
    def create_search_url(query: str, excluded_website: str, custom_config_id: str) -> str:
        search_query = f"{query} -site:{excluded_website}" if excluded_website else query
        return f"https://api.bing.microsoft.com/v7.0/custom/search?q={search_query}&customconfig={custom_config_id}"

    @staticmethod
    def get_search_results(url: str, num_results: int, api_key: str) -> list:
        headers = {'Ocp-Apim-Subscription-Key': api_key}
        params = {'count': num_results}
        response = requests.get(url, headers=headers, params=params)
        return response.json().get('webPages', {}).get('value', []) if response.status_code == 200 else None

    @staticmethod
    def fetch_content(url: str) -> str:
        try:
            with requests.Session() as session:
                response = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20)
                return BeautifulSoup(response.text, 'html.parser').get_text() if response.status_code == 200 else None
        except requests.RequestException:
            return None

    @staticmethod
    def write_to_file(filepath: str, url: str, content: str):
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(f"URL: {url}\nContent:\n{content}\n\n")


def parse_arguments():
    parser = argparse.ArgumentParser(description='Search and scrape data.')
    parser.add_argument('--gpu_cpu', type=str, default='cpu', help='Choose between "cpu" and "gpu"')
    parser.add_argument('--company_name', type=str, default='nike', help='Name of the company')
    parser.add_argument('--company_website', type=str, default='nike.com', help='Website of the company')
    parser.add_argument('--num_results', type=int, default=2, help='Number of search results to return')
    return parser.parse_args()


def load_env_variables():
    load_dotenv()
    return os.getenv("API_KEY"), os.getenv("CUSTOM_CONFIG_ID")


def search_and_scrape(gpu_cpu, company_name, company_website, num_results, api_key, custom_config_id, max_threads=10):
    urls = ScraperHelper.get_search_results(
        ScraperHelper.create_search_url(f"intext:\"{company_name}\" company sustainability", company_website,
                                        custom_config_id), num_results, api_key)
    urls = urls if urls is not None else []
    urls = [item['url'] for item in urls]

    # Print the URLs here
    for item in urls:
        print('Found URL:', item)

    processor = __import__('cpu' if gpu_cpu == "cpu" else 'cuda')
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for url in tqdm(urls, desc="URLs processed"):  # apply tqdm here
            try:
                content = ScraperHelper.fetch_content(url)
                if content:
                    processed_content = processor.process_and_classify_content(content)
                    if processed_content:
                        ScraperHelper.write_to_file('scraped_data.txt', url, processed_content)
            except Exception as e:
                print(f"Error processing {url}: {e}")


args = parse_arguments()
api_key, custom_config_id = load_env_variables()
print(f"Searching with the following parameters:")
print(f"gpu_cpu:         {args.gpu_cpu}")
print(f"company_name:    {args.company_name}")
print(f"company_website: {args.company_website}")
print(f"num_results:     {args.num_results}")
search_and_scrape(args.gpu_cpu, args.company_name, args.company_website, args.num_results, api_key, custom_config_id)
