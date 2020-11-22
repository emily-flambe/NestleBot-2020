from get_gis import google_image_search
import os


def main():

    search_term = 'carnation'
    num_images = 10
        
    google_image_search(search_term, num_images)
    
if __name__ == "__main__":
    main()