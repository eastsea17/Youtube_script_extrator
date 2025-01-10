# YouTube Transcript Extractor

This Python script extracts the transcript (captions) from a YouTube video and saves it as a text file. It uses the `youtube-transcript-api` library to fetch the transcript data.

## Features

- Extracts transcripts from YouTube videos.
- Supports both `youtube.com` and `youtu.be` URL formats.
- Automatically detects available languages and tries to fetch the Korean transcript first, and if not available, falls back to the English transcript.
- Saves the transcript as a text file in the `transcripts` directory.
- Provides error handling for invalid URLs and other potential issues.

## Prerequisites

- Python 3.6 or higher
- `pip` package manager

## Installation

1.  Clone the repository (if applicable) or download the `script.py` file.
2.  Install the required library using `pip`:

    ```bash
    pip install youtube-transcript-api
    ```

## Usage

1.  Open the `script.py` file in a text editor.
2.  Locate the following section in the `if __name__ == "__main__":` block:
   
    ```python
    # Enter the YouTube video URL you want to extract the transcript from.
    video_url = "https://www.youtube.com/watch?v=your_video_id" # Enter the youtube url you want to use here.
    ```

3. Replace the example URL with the URL of the YouTube video you want to extract the transcript from. You can use either the full `youtube.com` URL or the short `youtu.be` URL. Make sure to uncomment the line of your URL and comment out the others by using `#`.

4.  Run the script from the command line:

    ```bash
    python script.py
    ```

5.  The extracted transcript will be saved in a text file named `<video_id>.txt` in the `transcripts` directory.


## Important Notes about `youtube-transcript-api`

- **Free but Unofficial Access:** This script uses the `youtube-transcript-api` library, which generally provides free access to YouTube transcripts. However, it often relies on unofficial methods of accessing YouTube's internal API.

- **Potential for Discontinuation:** Due to its unofficial nature, changes in YouTube's API or policies may cause the library and this script to stop working without prior notice.

- **No Guarantees:** There are no guarantees regarding the availability, accuracy, or stability of the transcript data. YouTube may change how transcripts are accessed or provided.

- **Rate Limiting:** While there might not be strict quota limitations with the unofficial method, sending too many requests in a short period can result in temporary IP blocks or other issues. Use the script responsibly and avoid making excessive requests.

- **Recommended API Key Usage:** For more reliable and stable operation, especially for commercial use or large-scale transcript extraction, it's recommended to use an official YouTube Data API key. You can set it up in the [Google Cloud Console](https://console.cloud.google.com/).

- **YouTube Terms of Service:** Always ensure that your usage complies with YouTube's Terms of Service and policies. Avoid any activity that violates their guidelines.

- **Transcript Quality:** The transcript quality depends on the accuracy of the subtitles provided by YouTube. The script cannot improve the accuracy of the transcripts themselves.

- **Error Handling:** While the script includes error handling, it may not cover all potential issues. Be prepared to handle edge cases and unexpected errors when using this script.
