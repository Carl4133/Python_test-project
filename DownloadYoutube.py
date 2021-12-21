import argparse
from pytube import YouTube
from os import path
import platform

def onProgress(stream, chunk, remaining):
    total = stream.filesize
    precent = (total - remaining) / total * 100
    print('下載中...{:05.2f}%'.format(precent),end='\r')

def download_video(yt, args):
    filter = yt.streams.filter
    if args.hd:
        target = filter(type='video', resolution='720p').first()
    elif args.fhd:    
        target = filter(type='video', resolution='1080p').first()
    elif args.sd:
        target = filter(type='video', resolution='480p').first()
    elif args.a:
        target = filter(type='audio').first()
    else:
        target = filter(type='video').first()

    # target.download()
    target.download(output_path=pyTube_folder())

def pyTube_folder():
    sys = platform.system()
    home = path.expanduser('~') #使用者家目錄

    
    if sys == 'Windows':  #C:\Users\e32lsm\Videos\PyTube
        folder = path.join(home, 'Videos','PyTube')
    elif sys == 'Darwin':
        folder = path.join(home,'Movies', 'PyTube')

    # print(folder)
    if not path.isdir(folder):
        path.makedirs(folder)
    return folder

def main():  
    parser = argparse.ArgumentParser()
    parser.add_argument('url',help="指定YouTube視訊網址")
    parser.add_argument('-sd',action="store_true",help="480p畫質")
    parser.add_argument('-hd',action="store_true",help="720p畫質")
    parser.add_argument('-fhd',action="store_true",help="1080p畫質")
    parser.add_argument('-a',action="store_true",help="僅下載聲音")
    
    args = parser.parse_args()

    yt = YouTube(args.url,on_progress_callback=onProgress)
    # on_progress_callback在有更新進度下載時，自動被程式呼叫執行
    #當發生某事件而自動被呼叫執行的函式，統稱為回呼函式

    download_video(yt,args)

main()

