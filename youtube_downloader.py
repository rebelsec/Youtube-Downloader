import pytube
import os


def single_link():
    video = pytube.YouTube(url)
    looping = 0
    while looping < 1:
        mode = input("""
Silahkan pilih Resolusi :
1. Lowest Resolution
2. Highest Resolution
3. Audio Only
""")

        print("Downloading ....")
        if mode == "1":
            video.streams.get_lowest_resolution().download('./Download/')
            print(video.title, " --- has been downloaded --- ")
            looping += 1

        elif mode == "2":
            video.streams.get_highest_resolution().download('./Download/')
            print(video.title, " --- has been downloaded --- ")
            looping += 1

        elif mode == "3":
            video.streams.get_audio_only().download('./Download')
            print(video.title, " --- has been downloaded --- ")
            looping += 1

        else:
            print("\nResolusi yang Anda pilih salah!!!")


def playlist():
    pl = pytube.Playlist(url)
    looping = 0
    while looping < 1:
        mode = input("""
Silahkan pilih Resolusi :
1. Lowest Resolution
2. Highest Resolution
3. Audio Only
""")
        print("Downloading ....")

        if mode == "1":
            for videos in pl.videos:
                videos.streams.get_lowest_resolution().download('./Download')
                print(videos.title, " --- has been downloaded --- ")
                looping += 1

        elif mode == "2":
            for videos in pl.videos:
                videos.streams.get_highest_resolution().download('./Download')
                print(videos.title, " --- has been downloaded --- ")
                looping += 1

        elif mode == "3":
            for videos in pl.videos:
                videos.streams.get_audio_only().download('./Download')
                print(videos.title, " --- has been downloaded --- ")
                looping += 1

        else:
            print("\nResolusi yang Anda pilih salah!!!")


print("""

Youtube Downloader By :
 ____      _          _
|  _ \ ___| |__   ___| |___  ___  ___
| |_) / _ \ '_ \ / _ \ / __|/ _ \/ __|
|  _ <  __/ |_) |  __/ \__ \  __/ (__
|_| \_\___|_.__/ \___|_|___/\___|\___|

""")
looping = 0
while looping < 1:
    url = input("Masukkan URL Youtube : ")
    if url == "":
        print("URL Youtube tidak boleh kosong !!!")
    else:
        looping += 1

looping = 0
while looping < 1:
    mode_download = input("""
Silahkan Pilih Mode
1. Single Mode
2. Playlist Mode
""")
    if mode_download == "1":
        print("Please Wait ...")
        looping += 1
        single_link()
    elif mode_download == "2":
        print("Please Wait ...")
        looping += 1
        playlist()
    else:
        print("Silahkan pilih Mode yang sesuai !!!")


if not os.path.exists('Download'):
    os.mkdir('Download')

print("\nDone ^_^ ")
