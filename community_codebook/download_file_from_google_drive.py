def download_file_from_google_drive(id, destination):
    '''
    Function Author: @turdus-merula, from https://stackoverflow.com/questions/25010369/wget-curl-large-file-from-google-drive/39225039#39225039
    
    Docstring Author: Harry Hawkes (GH: @hph220), Lehigh Class of 2020
    
    Purpose: A solution for sharing large files with your group or future users.
    
    Solution:
    1. Upload (compressed) files to Lehigh Google Drive. (A non-Lehigh google drive
    will work too, but has limitations on space.)
    
    2. Turn on sharing for the file by right clicking it and selecting "get shareable link", 
    but you don't need to give edit access.
    
    3. Turn on sharing for users outside of Lehigh University, but you don't need to give 
    edit access.
    
    4. Get the ID from the sharing link (found at the end of the sharing URL), you'll need to
    put that into your code. 
    
    5. In your file that uses this data:
    
        import os
        from download_file_from_google_drive import download_file_from_google_drive
        
        # download the file to your computer if you haven't already
        
        filepath_to_download_to = 'my_big_file.csv' # replace with your preferred name/path
        if not os.path.exists(filepath_to_download_to)
            download_file_from_google_drive(<put the ID here>, filepath_to_download_to)
    
        # open it
        <open the file, exact method depends on file type>   
    '''  
  
    import requests
    
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    


if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 3:
        print("Usage: python google_drive.py drive_file_id destination_file_path")
    else:
        # TAKE ID FROM SHAREABLE LINK
        file_id = sys.argv[1]
        # DESTINATION FILE ON YOUR DISK
        destination = sys.argv[2]
        download_file_from_google_drive(file_id, destination)
