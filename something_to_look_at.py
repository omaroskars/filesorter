from guessit import guessit
import os
import shutil
import glob
import sys

#def orginize(path, target):
path = str(sys.argv[1])
target = str(sys.argv[2])
video_file_extensions = ('.avi', '.mp4', '.mkv','.MP4', '.AVI', '.m4v','.nfo', '.srt', '.rm')
    

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith((video_file_extensions)):
            os.rename(os.path.join(root, file), os.path.join(root, '.'.join(file.split())))

for root, dirs, files in os.walk(path):
    for file in files:
        try:
            if file.endswith((video_file_extensions)):
                video = (guessit(file))
                videoTitle = str(video['title']).title()
                if video['type'] is 'episode':
                    if 'season' in video:
                        videoSeason = str(video['season'])
                        final_path = os.path.join(target, 'Tv-Shows', videoTitle, 'Season ' + videoSeason)
                    else:
                        final_path = os.path.join(target, 'Tv-Shows', videoTitle)
                elif 'format' in video:
                    if video['format'] == 'BluRay':
                        final_path = os.path.join(target, 'BluRay Movies', videoTitle)
                else:
                    final_path = os.path.join(target, 'Movies & Other', videoTitle)
                if not os.path.isdir(final_path):
                    os.makedirs(final_path)
                file = str('/'+file)
                if os.path.isfile(final_path+'/'+file):
                    os.remove(path + file)
                    continue
                print('Moving ' + file)
                shutil.move(root + file, final_path)
        except:
            print('Skip ' + file + ' !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            pass


