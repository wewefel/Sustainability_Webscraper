# Sustainability_Webscraper
Searches a given company on Custom Google Search Engine and scrapes all 3rd party sustainability information (data from websites that are not the company's official website)

After gathering desired URLs, the script will modify each URL's HTML content into chunks. These chunks are fed to the HappyTextClassification model named Vinoth24/environment-claims to determine whether the content is related to environment and sustainability or not, retrieved from here: https://huggingface.co/Vinoth24/environmental_claims
