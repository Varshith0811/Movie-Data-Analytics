from Movie import OMDBApi

if __name__ == '__main__':
    title = ''
    type = ''
    year = ''



    print('Enter a movie title to search for:')
    title = input().replace(' ', '+')
    type = 'movie'

    print('Enter the year of release or leave blank if unknown:')
    year = input()

    movie = OMDBApi(title, type, year)
    for k, v in movie.items():
        if k == "Ratings":
            print(k + ": ")
            for x in range(len(v)):
                for y, z in v[x].items():
                    if y == "Source":
                        temp = z
                    else:
                        print(temp + ": " + z)
        else:
            print(k + ": " + v)
