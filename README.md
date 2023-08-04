# MovieMD

MovieMD is a simple yet powerful tool that allows you to create videos with images and spoken content without having to manually record any audio or edit video. The real magic behind MovieMD lies in the use of the **Eleven Labs API**, which provides a state-of-the-art text-to-speech service. All you need to do is create a markdown document in a specific format, and MovieMD, powered by Eleven Labs, will take care of the rest!

## How it works

MovieMD works by parsing a markdown document that you provide. It extracts image URLs and text from this document, and then generates an audio clip for each block of text using the Eleven Labs text-to-speech API. It pairs each audio clip with its corresponding image to create a video clip. Finally, it concatenates all of these video clips together to create a final video.

## How to use

1. Create a markdown document in the following format:

```markdown
![Image description](image_url "Text to be converted to speech.")
```

- The `Image description` is optional and won't affect the final video. It's good practice to include this for accessibility.
- `image_url` should be the path to an image on your local machine. This image will be displayed in the final video while the corresponding text is being spoken.
- The `Text to be converted to speech` should be enclosed in quotation marks. This text will be converted to speech using the Eleven Labs API.

2. You need to get your Eleven Labs API key and set it in a `.env` file in your project's root directory. The file should contain a line like this:

```env
ELEVEN_API_KEY=your_api_key_here
```

3. Run the `main.py` script with the path to the folder containing your markdown file and images as an argument. This will generate a file called `output.mp4` in your project's root directory.

```bash
python main.py path/to/your/folder
```

4. Enjoy your automatically generated video!

## Requirements

- Python 3.7 or later
- Eleven Labs API key
- The following Python packages, which can be installed with `pip install -r requirements.txt`:
  - pydub
  - elevenlabs
  - python-dotenv
  - moviepy
  - etc.

 Absolutely, here's how you can add a section about the MIT license to your `README.md` file:

---

## License

This project is licensed under the terms of the MIT license. For more information, see the [LICENSE](LICENSE) file in the project's root directory.

By using MovieMD, you agree to the terms of this license.
