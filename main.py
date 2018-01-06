import os

WORKING_DIR = os.getcwd()
PATHS = {
    'media_path': '',
    'tv_shows_path': '',
    'movies_path': ''
}

def create_media_dir(path):
    print("Would you like to create the media directory under" + path)
    userinput = input('yes/no: ')
    if userinput == 'yes':
        PATHS['media_path'] = path + '\Media'
        os.makedirs(PATHS['media_path'])
        print('Media file created successfully')

def create_directory(key, path, name):
    print('Creating ' + name + ' under the path ' + path +'\\' + name)
    PATHS[key] = path + '\\' + name
    os.makedirs(PATHS[key])
    print(name + ' created successfully')


create_media_dir(WORKING_DIR)
create_directory('tv_shows_path', PATHS['media_path'], 'TV shows')
create_directory('movies_path', PATHS['media_path'], 'Movies')

