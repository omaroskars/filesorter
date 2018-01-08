import os, shutil, pprint

WORKING_DIR = os.getcwd()
PATHS = {
    'media_path': '',
    'tv_shows_path': '',
    'movies_path': '',
    'data_path': os.path.join(WORKING_DIR, 'TestData')
}

def move_file(source, destination):
    shutil.copy(source, destination)

def create_directory(key, path, name):
    print('Creating ' + name + ' under the path ' + os.path.join(path, name))
    if os.path.isdir(path + '\\' + name) == True:
            print(name + " folder aldready exists\n")
            PATHS[key] = os.path.join(path, name)
    else:
        PATHS[key] = os.path.join(path, name)
        os.makedirs(PATHS[key])
        print(name + ' created successfully\n')

def init():
    media_path = os.path.join(WORKING_DIR, 'Media')
    if os.path.isdir(media_path) == True:
        print('deleting all in ' + media_path)
        shutil.rmtree(media_path)
        print('Deleted Media folder successfully\n')

def main():
    init()

    create_directory('media_path', WORKING_DIR, 'Media')
    create_directory('tv_shows_path', PATHS['media_path'], 'TV shows')
    create_directory('movies_path', PATHS['media_path'], 'Movies')

    pprint.pprint(PATHS)

    print(os.path.isfile(os.path.join(PATHS['data_path'], 'Peaky Blinders S01E01 Episode 1.avi')))
    move_file(os.path.join(PATHS['data_path'], 'Peaky Blinders S01E01 Episode 1.avi'), PATHS['tv_shows_path'])

main()