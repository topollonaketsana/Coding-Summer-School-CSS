
## Libraries
import os 
import shutil


source_dir = './messy_movie_files'
new_dir = './renamed_movies_files'


## ensure the directory exists
if not os.path.exists(source_dir):
    print('directory not found')


if not os.path.exists(new_dir):
    print('directory not found')
    os.makedirs(new_dir)                         ## create new director if its not there


## normalizing the file names eg star_wars!1977&Lucas
def normalize_filename(filename):

    ## remove the file extension
    name, ext = os.path.splitext(filename)
    print(f'{name} - extension: {ext}')


    ## replace common separators with space

    ## replace underscores with space
    name = name.replace('_', ' ')
    name = name.replace('!', ' ')
    name = name.replace('&', ' ')
    name = name.replace(';', ' ')
    name = name.replace('@', ' ')
    name = name.replace('-', ' ')

    parts = name.split()

    print(parts)


    ## Get a movie year
    year = None

    for part in parts:

        if part.isdigit() and len(part) == 4: 
            year = part
            print(f'year found: {year}')
            break

    if not year: 
        print(f"Skipping: {filename} - no year") 
        return None 

        
        
    ## get the movie title 
    title_parts = parts[:parts.index(year)]
    print(title_parts)
    movie_title = ' '.join(title_parts).strip().title()
    print(f'{movie_title}')

    ## get the director (everything after the year)
    movie_director = parts[parts.index(year) + 1:]
    print(f'{movie_director}')
    director = ' '.join(movie_director).strip().title()
    print(f'{director}')


    ## format the new file name
    new_name = f'{movie_title}({year}) - {director}{ext}'

    print(new_name)

    return new_name

## for loop to format all the files
for filename in os.listdir(source_dir):
    print(filename)
    old_path = os.path.join(source_dir, filename)

    if not os.path.isfile(old_path):
        continue

    new_name = normalize_filename(filename)
    


    #print(new_name)

    ## check old path
    if not new_name:
        print(f'skipping {filename}')
        continue

    ## new path
    new_path = os.path.join(new_dir, new_name)





    shutil.copy(old_path, new_path)
    print(f'copied and renamed {filename} -> {new_name}')






## call a function
normalize_filename('star_wars!1977&Lucas')   