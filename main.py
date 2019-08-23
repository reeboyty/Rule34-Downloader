#!/usr/bin/env python3

"""
    Name: Rule34 downloader
    Author: Alessandro Nava -- Zeta314 - https://github.com/Zeta314
    Version: 1.0 alpha
    Date: 22/08/2019
"""

import rule34
import requests

import argparse
import logging

from pathlib import Path
from timeit import default_timer

LOGGING_LEVEL = logging.INFO

def list_diff(list1, list2):
    return (list(set(list1) - set(list2)))

def main(args):
    if args.verbose:
        LOGGING_LEVEL = logging.DEBUG

    # Prepare an instance of the logger for the current script instance
    logger = logging.getLogger("Rule34Downloader")
    logger.setLevel(LOGGING_LEVEL)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOGGING_LEVEL)

    # Set the format for the logger output
    formatter = logging.Formatter('[%(asctime)s] %(name)s %(levelname)s: %(message)s')
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    # =================================================================================

    logger.debug("Arguments: {}".format(args))

    # Override rule34sync with the synchronous wrapper
    rule34sync = rule34.Sync()

    # Convert the tags to a more convenient format
    if len(args.tags) > 1:
        args.tags = ' '.join(args.tags)
    else:
        args.tags = args.tags[0]

    logger.debug("Querying Rule34 apis...")
    images_count = rule34sync.totalImages(args.tags)

    # If the total images count received from the apis is 0, no image is found
    if images_count == 0:
        logger.error("No images found with those tags")
        return

    # Otherwise, let's proceed and download em' all
    logger.info("{} images found!".format(images_count))

    # Since there is a limit set, let's tell that to the user, just to be precise
    if args.limit > 0:
        logging.info("The download limit is capped to {} images".format(args.limit))

    logger.info("Gathering data from Rule34... "
                 "(this will take approximately {0:.3g} seconds)".format(0.002*images_count))

    fetch_start = default_timer() # To measure how much time does it take

    try:
        images = rule34sync.getImages(args.tags, singlePage=False)
    except Exception as e:
        logger.error("There was an error while gathering images.")
        logger.error("There's probably something wrong with this tag, try another one.")
        logger.debug(str(e))
        return

    fetch_end = default_timer()

    logger.info("This took exactly {0:.3g} seconds".format((fetch_end - fetch_start) / images_count))

    # If something has gone wrong during the images fetch
    if images is None:
        logger.error("Rule34 didn't give any image, this should not happen")
        return

    # Divide the videos from the images
    videos = [x for x in images if "webm" in x.file_url]

    # If the user doesn't want videos, remove them
    if not args.no_videos:
        images = list_diff(images, videos)

    destination_folder = Path(args.destination)

    logger.debug("Checking destination folder existence...")
    if not destination_folder.exists():
        logger.debug("Destination folder doesn't exist! Creating it...")
        destination_folder.mkdir()
        logger.debug("Destination folder created!")
    else:
        logger.debug("Destination folder exists! Checking if it's actually a directory...")
        if not destination_folder.is_dir():
            logger.error("The given destination folder isn't a folder!")
            return
        logger.debug("Destination folder is a directory!")

    downloaded_images = 0
    for image in images:
        # Check for the images limit
        if args.limit > 0 and downloaded_images >= args.limit:
            logger.warning("Downloaded images limit exceeded. Stopping...")
            return

        image_name = image.file_url.split("/")[-1]
        image_extension = image.file_url.rsplit('.', 1)[-1]

        output_name = Path(destination_folder, '.'.join([image.md5, image_extension]))
        logger.debug("Output file: {}".format(output_name))
        logger.info("Downloading {}...".format(image_name))

        response = requests.get(image.file_url, stream=True)
        logger.debug("API response is {}".format(response.status_code))

        if response.status_code != 200:
            logger.error("Error while downloading image! ({})".format(response.status_code))
            continue

        with open(output_name, 'wb') as output_file:
            for chunk in response.iter_content(1024):
                output_file.write(chunk)

        logger.info("{} downloaded!".format(image_name))
        downloaded_images += 1

# The actual "main" function of the script
if __name__ == "__main__":

    # Create an argument parser instance to handle the various inputs
    parser = argparse.ArgumentParser(description="Rule34 posts downloader")
    parser.add_argument('--tags', '-t', type=str, nargs='+', required=True,
            help='the actual tags to search')
    parser.add_argument('--destination', '-d', type=str, default='hentai',
            help='the destination folder of the downloaded material (default: hentai)')
    parser.add_argument('--limit', '-l', type=int, default=0,
            help='the maximum amount of material to download (default: illimited)')

    parser.add_argument('--no-videos', '-nv', action='store_true')

    parser.add_argument('--verbose', '-v', action='store_true', help='outputs debug messages')

    args = parser.parse_args()

    # Print the script logo
    logo = r'''    ____ _____ __ __  ____                      __                __
   / __ \__  // // / / __ \____ _      ______  / /___  ____ _____/ /__  _____
  / /_/ //_ </ // /_/ / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  / _ \/ ___/
 / _, _/__/ /__  __/ /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  __/ /
/_/ |_/____/  /_/ /_____/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/\___/_/     '''

    print(logo)
    print('='*len(max(logo.split('\n'), key=len)))
    print()

    # Let's pass the args to the actual script function
    main(args)
