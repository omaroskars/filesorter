import os
import pprint

WORKING_DIR = os.getcwd()
PATHS = {
    'media_path': '',
    'tv_shows_path': '',
    'movies_path': ''
}

def scan_tv_shows()
    
def create_directory(key, path, name):
    print('Creating ' + name + ' under the path ' + os.path.join(path, name))
    if os.path.isdir(path + '\\' + name) == True:
            print(name + " folder aldready exists")
            PATHS[key] = os.path.join(path, name)
    else:
        PATHS[key] = os.path.join(path, name)
        os.makedirs(PATHS[key])
        print(name + ' created successfully')
    
    print()

def main():
    create_directory('media_path', WORKING_DIR, 'Media')
    create_directory('tv_shows_path', PATHS['media_path'], 'TV shows')
    create_directory('movies_path', PATHS['media_path'], 'Movies')

    pprint.pprint(PATHS)


main()

