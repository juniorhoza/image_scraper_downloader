# Image Scraper

This project is a lightweight Python tool that scrapes a webpage and extracts all images found on a given URL.

It is intended for educational and personal use only.
Please ensure you have permission before scraping any website.

## ⚠️ Legal Warning

Downloading or scraping images from external websites may violate their Terms of Service or copyright laws.

Always check the site’s policies and obtain permission before scraping.
Unauthorized scraping may lead to legal consequences.

**Features**

- Fetches all image URLs on a specific webpage

- Downloads each image automatically

- Simple and easy to run

- Uses requests and BeautifulSoup for web scraping

## Setup Instructions

1. Create a Virtual Environment

```python -m venv venv```

2. Activate the Virtual Environment

Windows:

```source venv\Scripts\activate```


Linux / macOS:

```source venv/bin/activate```

3. Install Dependencies
```pip install -r requirements.txt```

### Usage

Run the Script
```python main.py```


Once executed, the script will:

1. Ask for a URL

2. Verify if webpage allows scraping 

3. Scrape the webpage

4. Extract all image links found in webpage

5. download all images and save in a folder (optional)

### Project Structure
.
├── main.py
├── requirements.txt
├── README.md
└── images/          # Downloaded images (auto-created)
└── services/
    └── ImageDownloaderService.py
    └── ImageScrapingService.py

### Requirements

- Python 3.8+

- Internet connection

- Required packages in requirements.txt:

- requests

- beautifulsoup4

### License

This project is provided for educational purposes only.
You are responsible for ensuring your usage complies with applicable laws and website policies.