from services.ImageScrapingService import ScrapingService
from services.ImageDownloaderService import ImageDownloaderService

def scrap_images():
    url=str(input("Enter the URL of the website to scrap images from: "))   

    if not url:
        print("URL cannot be empty. Please enter a valid URL.")
        return
    if not url.startswith("http://") and not url.startswith("https://"):
        print("Invalid URL. Please make sure to include http:// or https://")
        return 
    scraper = ScrapingService(url)
    
    try:
        print("Checking robots.txt for scraping permissions...")

        if not scraper.is_allowed_to_scrap(url):
            print("""

            ⚠️  IMPORTANT NOTICE: WEB SCRAPING WARNING

            You are about to perform a web scraping operation on a site that does not allow scraping.

            Unauthorized scraping of websites may violate:
            • The website’s Terms of Service
            • Robots.txt access rules
            • Copyright or data usage laws

            Proceeding without proper authorization may result in:
            • IP blocking or restricted access
            • Legal notices or enforcement actions
            • Permanent denial of service by the website owner

            Please ensure you have explicit permission to scrape the target website 
            before continuing.

            Do you wish to proceed? (yes/no):

            """)
           
            choice = input().strip().lower()
            match choice:
                case 'yes':
                    print("Proceeding… Your choice! If someone in a suit knocks on your door, remember: YOU said yes. 😅")
                case 'no':
                    print("Good call. Scraping aborted. No legal drama today. 😌")
                    return
                case _:
                    print("Invalid choice. Scraping cancelled. When in doubt, don’t poke the internet police. 🚔")
                    return
          
        
        results = scraper.scrape()

        if results:
            print("Image scraping completed successfully.")
        
        print("You can now use the ImageDownloaderService to download the scraped images.")
        print("""

    ⚠️  IMPORTANT NOTICE: IMAGE DOWNLOAD WARNING

    You are about to download images from an external website.

    Downloading or using images without proper authorization may violate:
    • The website’s Terms of Service
    • Copyright and intellectual property laws
    • Usage and licensing restrictions

    Proceeding without permission may result in:
    • Legal liability or copyright claims
    • Removal requests or takedown notices
    • Blocking or restricted access from the website

    Please ensure you have the legal right and explicit permission 
    to download and use these images before continuing.

    Do you wish to proceed with downloading the images? (yes/no):

    """)

        choice = input().strip().lower()
        match choice:
            case 'yes':
                print("Alright, downloading the images… You chose this path. If copyrights come knocking, remember who pressed YES. 😅")
                download_images()
            case 'no':
                print("Download aborted. Wise choice — no unexpected lawyers today. 😌")
                return
            case _:
                print("Invalid choice. Operation cancelled. Better safe than explaining things to the internet police. 🚔")
                return
    except Exception as e:

        print(f"An error occurred during scraping: {e}")
        e.with_traceback()

def download_images():
    downloader = ImageDownloaderService()
    save_folder = str(input("Enter the folder name to save downloaded images (default: downloaded_images): "))
    if not save_folder:
        save_folder = "downloaded_images"
    try:
        downloader.download_images_from_list('images_links.txt', save_folder)
        print("Image downloading process completed.")
    except Exception as e:
        print(f"An error occurred during image downloading: {e}")
        e.with_traceback()


if __name__ == "__main__":
    scrap_images()