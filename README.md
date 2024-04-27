<a name="top"></a>

# Sustainability Webscraper




## Overview
This project consists of a Python web scraper that searches for and extracts information related to environmental and sustainability efforts of a specified company from URLs that are not the company's official website.  
  
It utilizes various tools including Beautiful Soup for scraping, NLTK for text processing, and a BERT model for text classification.

### Features
- **Custom Google Search**: Leverages Google's Custom Search JSON API to retrieve relevant URLs based on the query.
- **Content Filtering**: Excludes URLs that are from the company's official website or contain undesirable paths (e.g., downloads or lists).
- **Concurrency**: Uses `ThreadPoolExecutor` for concurrent scraping, enhancing the speed and efficiency of data collection.
- **Text Classification**: Employs a BERT-based model to classify sentences that are likely related to environmental or sustainability claims.



### How it Works


1. Define google_search function which uses Google's Custom Search JSON API. Here are some reasons why we use it:
   * Legal and Compliance Considerations:
     * The API is a legitimate method provided by Google to access its search results programmatically, allowing us to use an approved channel and comply with Google's terms of service. This helps us avoid legal issues or our IP being blocked.
   * Customization and Relevance:
     * The Custom Search JSON API allows you to create a customized search experience that can target specific websites or domains, exclude others, and fine-tune the search engine to focus on particular topics or types of content.
   * Efficiency and Structured Data:
     * When you use the API, you get structured JSON data in return, which is easier to handle and parse compared to scraping HTML content from a webpage. This structured format saves time and reduces the complexity of the data extraction process.
   * Reliability and Scalability:
     * The API provides a reliable and scalable way to handle search queries, granting more effective request management and avoiding errors and inconsistencies due to webpage changes or IP bans.
2. Establish our text classification model made with BERT.
   * BERT is a revolutionary NLP tool made by Google AI Language using language understanding, context awareness, transformers, and more.
   * The model takes an input sequence and decides whether the text is related to environmental claims or not.
     * This helps us only scrape useful sustainability information that will be considered in subsequent testing and scoring.
   * For more information, visit [here](https://huggingface.co/Vinoth24/environmental_claims).
   * (This text classification model will eventually be replaced with my own model, but for now we will be using this.)
4. Search and scrape:
   * First narrows search to only use URLs that are not the company's own official website (or branches).
   * Uses a 'ThreadPoolExecutor'to manage a pool of threads, executing calls asynchronously. This is particularly useful in I/O-bound and high-latency operations such as web scraping, where the script often waits for network responses.
5. Process and classify:
   * After fetching content from each URL, we pass the information to a new function which "cleans" our data and prepares it to be fed to our text classification model.
     * Examples of cleaning the data incldues stripping white spaces and breaking the block of text down to smaller chunks if necessary while maintaining sentence integrity.
   * If our BERT-based model decides that the block of text we gave is related to sustainability, it is written down in our text document.

[Back to Top](#top)

<!-- GETTING STARTED -->
## Setup

### Prerequisites

**1. Ensure Python 3.9.0 or greater is installed:**
* Before starting, make sure Python 3.9.0 or any newer version is installed on your system. You can check this by running python3 --version in your terminal or command prompt. If it’s not installed, you should install it from the official Python website [here](https://www.python.org/downloads).

**2. Install Git:**
* If you don't already have Git installed on your computer, you'll need to install it first. You can download Git from [here](https://git-scm.com/).

**3. Create Google Cloud account with access to the Custom Search JSON API.**
* Go [here](https://developers.google.com/custom-search/v1/overview) to get your API key and CSE ID.
* Rename `.env.example` to `.env` in the root directory of your project and add your `API_KEY` and `CSE_ID`.

**4. Open Your Terminal or Command Prompt:**
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
[Back to Top](#top)


### Virtual Environment (Optional) and Running the Script

_Creating a virtual environment is important for maintaining its own dependencies independent of other projects. This prevents conflicts between package versions that can lead to bugs and compatibility issues._
  
_However, you may skip the virtual environment and do step 4 in your command prompt if you're lazy (me)._

**1. If Sustainability_Webscraper is on your desktop, use this command to navigate to the directory:**
* Windows:
  ``` sh
  cd Desktop\Sustainability_Webscraper
  ```

* Mac or Linux:
  ``` sh
  cd ~/Desktop/Sustainability_Webscraper
  ```
**2. Once you are inside the Sustainability_Webscraper directory, create the virtual environment using:**
   ``` sh
   python3 -m venv venv
   ```
* This command creates a new folder in the project directory called 'venv' where the virtual environment files will be stored.
**3. Activate the Virtual Environment:**
* Windows:
  ``` sh
  venv\Scripts\activate
  ```
* Mac or Linux:
  ``` sh
  source venv/bin/activate
  ```
**4. Install Requirements:**
* With the virtual environment activated, install all the packages listed in the requirements.txt file by running:
  ``` sh
  pip install -r requirements.txt
  ```
**5. Make sure the script is being run in your virtual environment.**
* For example, in VS Code it should say '3.9.0 ('venv': venv) at the bottom of your screen, and in the VS Code command prompt you should see '(venv)' before your username.

**6. Change the company name and website URL on the bottom cell of the .ipynb file, then run. View results in scraped_data.txt.**
* The first time running the entire script may take a minute or two, but afterwards it will be pretty quick. After your first time running, all you need to do is alter and run the bottom cell that has the company name and website in it.

[Back to Top](#top)

## Limitations

* The current text classification model used ONLY detects environmental claims.
  * Topics such as charity/donations, governance, activism, and more may not be scraped if they are not also about the environment.
  * I have a few ideas on how to fix this, but they have not been implemented yet (4/26/2024).
* Only scrapes one company at a time.
  * Eventually, the script will be able to take a list of company names (or maybe dictionary so we use a {company_name: company_website} format).
    * Probably create a new .txt file for each company.
* Needs more testing.
