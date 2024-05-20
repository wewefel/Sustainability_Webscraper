<a name="top"></a>

# Sustainability Webscraper

## Table of Contents
1. [Overview](#overview)
   - [Features](#features)
   - [How it Works](#how-it-works)
2. [Setup](#setup)
   - [Prerequisites](#prerequisites)
   - [Running the script](#running-the-script)
3. [Limitations](#limitations)


## Overview
This project consists of a Python web scraper that searches for and extracts information related to environmental and sustainability efforts of a specified company from URLs that are not the company's official website.  
  
It utilizes various tools including Beautiful Soup for scraping, NLTK for text processing, and a BERT model for text classification.

### Features
- **Custom Bing Search API**: Leverages Bing's Custom Search JSON API to retrieve relevant URLs based on the query.
- **Content Filtering**: Excludes URLs that are from the company's official website or contain undesirable paths (e.g., downloads or lists).
- **Concurrency**: Uses `ThreadPoolExecutor` for concurrent scraping, enhancing the speed and efficiency of data collection.
- **Text Classification**: Employs a BERT-based model to classify sentences that are likely related to environmental or sustainability claims.



### How it Works


**1. Define google_search function which uses Bing's Custom Search API. Here are some reasons why we use it:**
   * Legal and Compliance Considerations:
     * The API is a legitimate method provided by Google to access its search results programmatically, allowing us to use an approved channel and comply with Google's terms of service. This helps us avoid legal issues or our IP being blocked.
   * Customization and Relevance:
     * The Custom Search JSON API allows you to create a customized search experience that can target specific websites or domains, exclude others, and fine-tune the search engine to focus on particular topics or types of content.
   * Efficiency and Structured Data:
     * When you use the API, you get structured JSON data in return, which is easier to handle and parse compared to scraping HTML content from a webpage. This structured format saves time and reduces the complexity of the data extraction process.
   * Reliability and Scalability:
     * The API provides a reliable and scalable way to handle search queries, granting more effective request management and avoiding errors and inconsistencies due to webpage changes or IP bans.
  
**2. Establish our text classification model made with BERT (will be replaced soon with different BERT model).**
   * BERT is a revolutionary NLP tool made by Google AI Language using language understanding, context awareness, transformers, and more.
   * The model takes an input sequence and decides whether the text is related to environmental claims or not.
     * This helps us only scrape useful sustainability information that will be considered in subsequent testing and scoring.
   * For more information, visit [here](https://huggingface.co/Vinoth24/environmental_claims).
   * (This text classification model will eventually be replaced with my own model, but for now we will be using this.)
  
**3. Search and scrape:**
   * First narrows search to only use URLs that are not the company's own official website (or branches).
   * Uses a 'ThreadPoolExecutor'to manage a pool of threads, executing calls asynchronously. This is particularly useful in I/O-bound and high-latency operations such as web scraping, where the script often waits for network responses.
  
**4. Process and classify:**
   * After fetching content from each URL, we pass the information to a new function which "cleans" our data and prepares it to be fed to our text classification model.
     * Examples of cleaning the data incldues stripping white spaces and breaking the block of text down to smaller chunks if necessary while maintaining sentence integrity.
   * If our BERT-based model decides that the block of text we gave is related to sustainability, it is written down in our text document.

[Back to Top](#top)

<!-- GETTING STARTED -->
## Setup

### Prerequisites

**1. Ensure Python 3.9 or 3.10 is installed (3.11 not working with our Transformers version):**
* Before starting, make sure Python 3.9.0 or any newer version is installed on your system. You can check this by running python3 --version in your terminal or command prompt. If it’s not installed, you should install it from the official Python website [here](https://www.python.org/downloads).

**2. Install Git:**
* If you don't already have Git installed on your computer, you'll need to install it first. You can download Git from [here](https://git-scm.com/).

**3. Create an account for Bing Custom Search API (HSG members: no need to create your own account and instance; just copy my key and ID from Slack).**
* Go [here](https://www.microsoft.com/en-us/bing/apis/bing-custom-search-api) and sign into your Microsoft account.
* Create 'New Instance'
* In Configuration, add an Active, Blocked, or Pinned URL (any arbitrary URL) so you can click 'Publish' in the top right.
* Then go to 'Production, then copy the Custom Configuration ID.
* Then click 'Click to issue free trial key' and follow the steps to obtain your API_KEY.
* Rename `.env.example` to `.env` in the root directory of your project and add your `API_KEY` and `CUSTOM_CONFIG_ID`.

**4. Clone Github Repo:**
* Go to the [Github repo](https://github.com/wewefel/Sustainability_Webscraper)
* Method 1: Click code, download as zip file, then extract all.
  * Method 2: Use 'git clone'
  * Open your terminal or command prompt
  * Navigate to the directory where you want to clone the repository (this example uses desktop as the directory, but feel free to change).  
  * On Windows:
   ``` sh
   cd Desktop
   ```
  * On Mac or Linux:
   ``` sh
   cd ~/Desktop
   ```
  * Then clone the repository:
   ``` sh
   git clone https://github.com/wewefel/Sustainability_Webscraper.git
   ```
**5. Install Requirements:**
* Open terminal or command prompt:
  ``` sh
  pip install requests==2.31.0 beautifulsoup4==4.12.3 nltk==3.8.1 transformers==4.38.2 python-dotenv==1.0.1 happytransformer==2.1.0
  ```
**6. Make sure the 'pip install ...' is being stored in the correct Python version.**
* You can check this by looking for a message in your command prompt that mentions where it is installed on your computer. For example:
  * Sample message to look for: 'Requirement already satisfied: colorama in c:\users\wefel\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages'
  * Make sure the Python version in the message is the version that you will be using to run the web scraper.

[Back to Top](#top)


### Running the Script

**1. Change the company name and website URL on the bottom cell of the .ipynb file.**

**2. Run each cell or press Run All. View results in scraped_data.txt.**
* The first time running the entire script may take a minute or two, but afterwards it will be pretty quick. After your first time running, all you need to do is alter and run the bottom cell that has the company name and website in it.

[Back to Top](#top)

## Limitations

* The current text classification model used ONLY detects environmental claims.
  * Topics such as charity/donations, governance, activism, and more may not be scraped if they are not also about the environment.
  * WILL SOON BE FIXED WITH ESG-BERT, JUST GIVE ME TIME.
* Only scrapes one company at a time.
  * Eventually, the script will be able to execute a list of company names at once.
    * Create single .csv file for all companies in batch.
