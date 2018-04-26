import movie

if __name__ == '__main__':
    title = ''
    type = ''
    year = ''



    print('Enter a movie title to search for:')
    title = input().replace(' ', '+')
    type = 'movie'

    print('Enter the year of release or leave blank if unknown:')
    year = input()

    movieInfo = movie.OMDBApi(title, type, year)
    movie.parseJSON(movieInfo)
