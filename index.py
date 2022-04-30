import requests
import os
from File_class import *

list_link = File_Interact('link.txt').read_file_list()
for link in list_link:
    id_video = link.split('?v=')[-1]
    path = r'./image'
    url = "https://img.youtube.com/vi/%s/0.jpg"%id_video
    res = requests.get(url).content
    name_video = "%s.jpg"%id_video
    with open(os.path.join(path,name_video),"wb") as f:
        f.write(res)