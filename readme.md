# HTML Page Reading Time Estimator

This Python script allows you to estimate the reading time of an HTML page by extracting the text content and using an average reading speed in words per minute.

## Installation

1. Clone this repository to your local machine or download the source code.

2. Navigate to the project directory in your terminal.

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ``` 
4. Activate the virtual environment:
- On Windows:
    ```
    venv\Scripts\activate```
- On macOS and Linux:
    ```
    source venv/bin/activate
    ```
5. Install project dependencies using the provided requirements.txt file:
```
pip install -r requirements.txt
```
## Usage
To estimate the reading time of an HTML page, you can run the script from the command line with the following syntax:
```bash
python page_reader.py [URL] [--words_per_minute WORDS_PER_MINUTE]
```

- [URL]: Replace this with the URL of the HTML page you want to analyze.
- [--words_per_minute WORDS_PER_MINUTE]: (Optional) Specify the average reading speed in words per minute. The default is 200 words per minute.

## Output
The script will provide an estimated reading time for the specified HTML page. It will display the estimated reading time in minutes based on the provided or default reading speed.

## Acknowledgments
- Beautiful Soup: For HTML parsing.
- Requests: For making HTTP requests.