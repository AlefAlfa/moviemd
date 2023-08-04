
import os
import sys
from dotenv import load_dotenv
from moviemd.parse import parse_md
from moviemd.make import make_clips, make_output
from elevenlabs import set_api_key


def main():
    # load API key
    load_dotenv()  # load the .env file
    # get the ELEVEN_API_KEY from the .env file
    ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
    set_api_key(ELEVEN_API_KEY)

    if os.path.exists("output.mp4"):
        os.remove("output.mp4")

    file_path = sys.argv[1]
    md_data = parse_md(file_path)
    clips = make_clips(md_data, ELEVEN_API_KEY)
    make_output(clips)


if __name__ == "__main__":
    main()
