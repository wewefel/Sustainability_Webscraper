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
  * The API is a legitimate method provided by Google to access its search results programmatically. This means you're using an approved channel to obtain data, which is crucial for complying with Google's terms of service. Unauthorized scraping of Google's search results page via other methods can lead to legal issues or your IP being blocked.
* Customization and Relevance:
  * The Custom Search JSON API allows you to create a customized search experience that can target specific websites or domains, exclude others, and fine-tune the search engine to focus on particular topics or types of content. This is particularly useful for a project focused on sustainability as it can help ensure the results are more relevant to the specific queries.
* Efficiency and Structured Data:
  * When you use the API, you get structured JSON data in return, which is easier to handle and parse compared to scraping HTML content from a webpage. This structured format saves time and reduces the complexity of the data extraction process.
* Reliability and Scalability:
  * The API provides a reliable and scalable way to handle search queries. It manages the load and the frequency of requests more effectively than manual scraping, which can be prone to errors and inconsistencies due to webpage changes or IP bans.

[Back to Top](#top)

<!-- GETTING STARTED -->
## Setup

### Prerequisites

1. Ensure Python 3.9.0 or greater is installed:
* Before starting, make sure Python 3.9.0 or any newer version is installed on your system. You can check this by running python3 --version in your terminal or command prompt. If it’s not installed, you should install it from the official Python website [here](https://www.python.org/downloads).
2. Install Git:
* If you don't already have Git installed on your computer, you'll need to install it first. You can download Git from [here](https://git-scm.com/).
3. Open Your Terminal or Command Prompt: Navigate to the directory where you want to clone the repository (this example uses desktop as the directory, but feel free to change).
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


### Virtual Environment

_Creating a virtual environment is important for maintaining its own dependencies independent of other projects. This prevents conflicts between package versions that can lead to bugs and compatibility issues._

1. If Triton_Bot is on your desktop, use this command to navigate to the directory:
* Windows:
  ``` sh
  cd Desktop\Sustainability_Webscraper
  ```
* Mac or Linux:
  ``` sh
  cd ~/Desktop/Sustainability_Webscraper
  ```
2. Once you are inside the Sustainability_Webscraper directory, create the virtual environment using:
   ``` sh
   python3 -m venv env
   ```
* This command creates a new folder in the TritonBot directory called 'env' where the virtual environment files will be stored.
3. Activate the Virtual Environment:
* Windows:
  ``` sh
  env\Scripts\activate
  ```
* Mac or Linux:
  ``` sh
  source env/bin/activate
  ```
4. Install Requirements:
* With the virtual environment activated, install all the packages listed in the requirements.txt file by running:
  ``` sh
  pip install -r requirements.txt
  ```
5. Make sure the script is being run in your virtual environment. For example, in VS Code it should say 'Python 3.9.0 env' at the bottom of your screen, and in the VS Code command prompt you should see '(env)' before your username.

[Back to Top](#top)

