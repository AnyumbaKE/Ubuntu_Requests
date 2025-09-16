# Ubuntu_Requests

**The Wisdom of Ubuntu: "I am because we are"**

This project is inspired by the Ubuntu philosophy, which emphasizes community, respect, and sharing.  
The script in this repository connects to the global web community to respectfully fetch shared images and organize them locally for later appreciation.

---

## Features

- **Community**: Connects to the internet and fetches shared images.  
- **Respect**: Handles errors gracefully without crashing.  
- **Sharing**: Stores downloaded images neatly in the `Fetched_Images` directory.  
- **Practicality**: Provides a lightweight and useful tool for everyday use.  

---

## Requirements

- Python 3.7+
- `requests` library

Install dependencies:
```bash```
pip install requests


## Usage

1. Clone the repository:
```
git clone https://github.com/your-username/Ubuntu_Requests.git
cd Ubuntu_Requests
```


2. Run the script:
```
python fetch_image.py
```

3. Enter the URL of an image when prompted.

4. The image will be saved in the Fetched_Images directory.

## Example
```
Enter the URL of the image: https://example.com/picture.jpg
Image successfully saved as Fetched_Images/picture.jpg
```
## Error Handling

The script respects unreliable connections and handles errors gracefully:

- Invalid URL

- HTTP errors (404, 500, etc.)

- Connection issues

- Timeout