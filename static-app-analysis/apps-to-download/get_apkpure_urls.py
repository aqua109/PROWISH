import re
import glob
import pandas as pd


def get_urls_from_text(file_path):
    """
    Extracts all URLs from a given text file using regular expressions.
    """
    # A common regex pattern to match URLs starting with http or https
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Use re.findall to get all occurrences of the pattern
        urls = re.findall(url_pattern, content)
    
    return urls

def main():
    text_files = glob.glob("*.txt")
    print(text_files)

    for file in text_files:
        all_urls = get_urls_from_text(file)
        sorted_urls = []

        for url in all_urls:
            if "apkpure.com" in url and url[-8:] != "download":
                if url not in sorted_urls:
                    sorted_urls.append(url)

        print(len(sorted_urls))


        df = pd.DataFrame(sorted_urls)
        csv_file = f'{file.replace('.txt', '')}.csv'
        df.to_csv(csv_file, header=False ,index=False)

if __name__ == '__main__':
    main()