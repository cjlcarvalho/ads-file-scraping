from Scraper import Scraper
import os

def main():
    folder = raw_input("Select your download folder: ")
    if not os.path.exists(folder):
        os.makedirs(folder)
    page = raw_input("Select your file page: ")
    scraper = Scraper(page, folder)
    scraper.getFiles()
    
main()
