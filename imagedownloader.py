import argparse
import urllib.request

def download_image(url, save_path):
    try:
        urllib.request.urlretrieve(url, save_path)
        print(f"Image downloaded successfully and saved as {save_path}")
    except Exception as e:
        print(f"Error occurred while downloading the image: {e}")

def main():
    parser = argparse.ArgumentParser(description='Image Downloader')
    parser.add_argument('url', help='URL of the image')
    parser.add_argument('-o', '--output', help='Output file path')

    args = parser.parse_args()
    url = args.url
    output_path = args.output

    if output_path is None:
        output_path = url.split('/')[-1]  # Use the last part of the URL as the default output file name

    download_image(url, output_path)

if __name__ == '__main__':
    main()
