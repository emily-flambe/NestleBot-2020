from google_images_search import GoogleImagesSearch
import os
import glob

def google_image_search(search_term, num_images):
    
    # get GCS API key and CX id from environment variables
    GCS_DEVELOPER_KEY=os.getenv("GCS_DEVELOPER_KEY")
    GCS_CX=os.getenv("GCS_CX")
    
    # create GoogleImagesSearch object
    gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)
        
    # define search params:
    _search_params = {
         'q': search_term
        ,'num': num_images
        ,'imgType': 'photo'
    }
        
    #create or empty target directory (where we will be saving images from Google Image Search)
    if not os.path.exists(f"images/{search_term}"):
        print(f"creating folder images/{search_term}...")
        os.makedirs(f"images/{search_term}")
    
    else:
        print(f"folder images/{search_term} already exists - clearing contents...")
        files = glob.glob(f"images/{search_term}/*")
        for f in files:
            os.remove(f)
            
    # generate path for image download
    download_path=os.getcwd()+'/images/'+search_term
    
    # search, download, and resize:
    gis.search(search_params=_search_params
               , path_to_dir=download_path
               , width=300
               , height=300)