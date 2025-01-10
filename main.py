from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import os
from urllib.parse import urlparse, parse_qs

def get_youtube_transcript(video_url, output_dir="transcripts"):
    """
    Extracts the transcript (captions) from a YouTube video URL and saves it as a text file.

    Args:
        video_url: The YouTube video URL.
        output_dir: The directory to save the transcripts (default: "transcripts").
    """
    try:
        # Parse the URL
        parsed_url = urlparse(video_url)

        if parsed_url.netloc == "youtu.be":
           video_id = parsed_url.path[1:] # The part after the first '/' in the path is the video_id
        elif "youtube.com" in parsed_url.netloc:
            # Extract query parameters
            query_params = parse_qs(parsed_url.query)
            if 'v' in query_params:
                video_id = query_params['v'][0]
            else:
              raise ValueError("Invalid YouTube URL: cannot find video ID")
        else:
           raise ValueError("Invalid YouTube URL: not a youtube url")

        # Get the transcript
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Print available transcript languages
        print("Available transcripts languages:")
        for transcript in transcript_list:
             print(f"- {transcript.language} ({transcript.language_code})")
        
        # Try to get Korean transcript, otherwise get English
        try:
             transcript = transcript_list.find_generated_transcript(['ko'])
        except:
             transcript = transcript_list.find_generated_transcript(['en'])
        
        # Format transcript to text
        formatter = TextFormatter()
        text_formatted = formatter.format_transcript(transcript.fetch())

        # Create the output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Set the file name and save the transcript
        file_name = f"{video_id}.txt"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text_formatted)
        
        print(f"Transcript saved to: {file_path}")

    except Exception as e:
        print(f"Error processing video {video_url}: {e}")


if __name__ == "__main__":
    # Enter the YouTube video URL you want to extract the transcript from.
    video_url = "https://youtu.be/EBTmNAxBOoY?si=js7yWw7Y0JFYbDX7"  # Enter URL
    get_youtube_transcript(video_url)
