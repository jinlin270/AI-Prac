import os
from google.cloud import translate_v2 as translate


def upload_and_translate(input_dir, output_dir, target_language):
    """
    Uploads all images in a directory, translates them using Google Translate, and downloads the translated images to a specified output directory.
    Args:
    input_dir: The directory containing the images to be translated.
    output_dir: The directory to which the translated images will be downloaded.
    target_language: The target language for the translation.
    """
    # Create a Google Translate client.
    client = translate.Client()

    # Get a list of all the files in the input directory.
    files = os.listdir(input_dir)

    # Iterate over the files and upload them to Google Translate.
    for file in files:
        with open(os.path.join(input_dir, file), "rb") as f:
            # Upload the image to Google Translate.
            response = client.translate_image(
                f,
                target_language=target_language,
            )

            # Download the translated image.
            with open(os.path.join(output_dir, file), "wb") as f:
                f.write(response.translated_image)
