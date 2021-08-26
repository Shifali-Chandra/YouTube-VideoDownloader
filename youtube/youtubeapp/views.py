from django.shortcuts import render
import pytube as pt

# Create your views here.
def download(url, SAVE_PATH = "D:/Downloads/"):
    yt = pt.YouTube(str(url)) 
    stream = yt.streams.get_by_itag(22)
    stream.download(SAVE_PATH) 
    print(yt.title,"Task Completed")

def playlistDownload(url):
    playlist = pt.Playlist(str(url))
    SAVE_PATH="D:/Downloads/"+str(playlist.title)+"/"
    for video_url in playlist.video_urls:
        download(video_url, SAVE_PATH)

def index(request):
    if request.method == 'POST':
        url = request.POST.get('ylink')
        if 'playlist' in url:
                playlistDownload(url)
        else:
            download(url)
        # try:
        #     if 'playlist' in url:
        #         playlistDownload(url)
        #     else:
        #         download(url)
        # except:
        #     print("Network Issue")
    return render(request, 'index.html')