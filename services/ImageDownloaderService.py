import requests
import os
import time

class ImageDownloaderService:
    def download_image(self, url: str, save_file_name: str, save_folder: str) -> None:

        if not os.path.exists(f"{save_folder}"):
            os.makedirs(save_folder)

        if os.path.exists(f"{save_folder}/{save_file_name}"):
            print(f"Image {save_file_name} already exists in {save_folder}. Skipping download.")
            return False
        
        response = requests.get(url)
        if response.status_code == 200:
            save_path = f"{save_folder}/{save_file_name}"
            with open(save_path, 'wb') as f:
                f.write(response.content)
        else:
            raise Exception(f"Failed to download image from {url}")
        
        print(f"Image {save_file_name} downloaded successfully to {save_folder}.")
        return True
    
    def download_images_from_list(self, file_name: str, save_folder: str) -> None:
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"The file {file_name} does not exist.")
        
        with open(file_name, 'r') as f:
            image_urls = f.readlines()
        
        for idx, url in enumerate(image_urls):
            url = url.strip()
            if url:
                try:
                    file_extension = url.split('.')[-1].split('?')[0]
                    save_file_name = f"image_{idx + 1}.{file_extension}"
                    
                    self.download_image(url, save_file_name, save_folder)
                    #adding a small delay of 2 seconds between downloads to be polite to the server after 5 downloads
                    if (idx + 1) % 5 == 0:
                        print("I am tired , sleeping for 2 seconds...")
                        time.sleep(2)
                    
                except Exception as e:
                    print(f"Failed to download image from {url}: {e}")