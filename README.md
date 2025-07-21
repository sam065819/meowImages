# meowImages

An **incredibly simple** ShareX "CDN"/image hosting site.

## Backend Guide
1. Install Python 3.13
2. Create a directory called "uploads" in the same directory as the app.py file or:
3. Change UPLOAD_FOLDER in app.py to your folder name.
4. Run python3/py/python app.py
5. Server is now running on port 5000 on your computer/server's IP.

## ShareX Guide

1. Go to Destinations - Custom uploader settings
2. Create a new uploader
3. Set any name
4. Under "Request URL" put "https://yourip:yourport/upload"
5. Under "Method", keep POST
6. Set Destination type to Image uploader
7. Set "File form name" to file
8. Set "URL" at the bottom to {json:url}

## Currently planned features

* Documentation website
* Authentication
