import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    """Extract filename from URL or generate one"""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:
        filename = "downloaded_image.jpg"
    return filename

def file_already_exists(filepath, content):
    """Check for duplicate by comparing file hash"""
    if not os.path.exists(filepath):
        return False
    
    # Hash the new content
    new_hash = hashlib.md5(content).hexdigest()
    
    # Hash the existing file
    with open(filepath, "rb") as f:
        existing_hash = hashlib.md5(f.read()).hexdigest()
    
    return new_hash == existing_hash

def fetch_image(url):
    try:
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        # Check headers for safety (basic example: content-type, size)
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (not an image): {url}")
            return
        
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > 10 * 1024 * 1024:  # 10 MB limit
            print(f"✗ Skipped (file too large): {url}")
            return

        # Extract filename
        filename = get_filename_from_url(url)
        filepath = os.path.join("Fetched_Images", filename)

        # Check for duplicates
        if os.path.exists(filepath) and file_already_exists(filepath, response.content):
            print(f"✗ Duplicate skipped: {filename}")
            return

        # Save image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    urls = input("Please enter image URLs (separated by commas): ").split(",")
    urls = [u.strip() for u in urls if u.strip()]

    for url in urls:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
