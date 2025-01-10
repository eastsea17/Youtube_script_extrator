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
