import youtube_dl
import sys
import concurrent.futures

"""
    Function responsible for converting the current pwd to /home/{user}
"""


def correct_path(entire_url: list) -> str:
    return '/'.join(entire_url[0].split("/")[:3])


"""
    Where the magic begins. 
"""


def mp3machine(video_url):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': f'{correct_path(sys.path)}/Music/{filename}',
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))


if __name__ == '__main__':
    urls = sys.argv[1:]

    # Threading part.
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(mp3machine, urls)
