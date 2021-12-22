def one():
    moviesin2016 = []
    with open('IMDB-Movie-Data.csv') as f:
        line = f.readline()
        line = f.readline()
        while line:
            line = line.split(',')
            if line[5] == '2016':
                moviesin2016.append((line[7], line[1]))
            line = f.readline()
    moviesin2016.sort(reverse=True)
    print('(1)')
    print(moviesin2016[:3])

def two():
    revenue = {}
    with open('IMDB-Movie-Data.csv') as f:
        line = f.readline()
        line = f.readline()
        while line:
            line = line.split(',')
            line[4] = [i.strip() for i in line[4].split('|')]
            for i in line[4]:
                if i in revenue:
                    revenue[i][0] += float(line[9]) if line[9] else 0
                    revenue[i][1] += 1
                else:
                    revenue[i] = [float(line[9]) if line[9] else 0, 1]
            line = f.readline()
    revenue = list(revenue.items())
    revenue.sort(key=lambda x: x[1][0] / x[1][1], reverse=True)
    m = revenue[0][1][0] / revenue[0][1][1]
    print('(2)')
    for i in revenue:
        if i[1][0] / i[1][1] >= m:
            print(i[0])
        else:
            break

def three():
    rating = []
    with open('IMDB-Movie-Data.csv') as f:
        line = f.readline()
        line = f.readline()
        while line:
            line = line.split(',')
            line[4] = [i.strip() for i in line[4].split('|')]
            for i in line[4]:
                if i == 'Emma Watson':
                    rating.append(float(line[7]))
            line = f.readline()
    print('(3)')
    print(sum(rating) / len(rating))

def four():
    director = {}
    with open('IMDB-Movie-Data.csv') as f:
        line = f.readline()
        line = f.readline()
        while line:
            line = line.split(',')
            line[4] = [i.strip() for i in line[4].split('|')]
            for i in line[4]:
                if line[3] in director:
                    if i not in director[line[3]]:
                        director[line[3]].append(i)
                else:
                    director[line[3]] = line[4]
            line = f.readline()
    director = list(director.items())
    director.sort(key=lambda x: len(x[1]), reverse=True)      
    print('(4)')
    temp = len(director[2][1])
    for i in director:
        if len(i[1]) >= temp:
            print(i[0], len(i[1]))
        else:
            break       

def five():
    genres = {}
    with open('IMDB-Movie-Data.csv') as f:
        line = f.readline()
        line = f.readline()
        while line:
            line = line.split(',')
            line[2] = [i.strip() for i in line[2].split('|')]
            line[4] = [i.strip() for i in line[4].split('|')]
            for i in line[4]:
                for j in line[2]:
                    if i in genres: 
                        genres[i].add(j)
                    else:
                        genres[i] = set([j])
            line = f.readline() 
    genres = list(genres.items())
    genres.sort(key=lambda x: len(x[1]), reverse=True)
    n = len(genres[1][1])
    print('(5)')
    for i in genres:
        if len(i[1]) >= n:
            print(i[0], len(i[1]))
        else:
            break

def six():
    gap = {}
    with open('IMDB-Movie-Data.csv') as f:
        line = f.readline()
        line = f.readline()
        while line:
            line = line.split(',')
            line[4] = [i.strip() for i in line[4].split('|')]
            line[5] = int(line[5])
            for i in line[4]:
                if i in gap:
                    if line[5] < gap[i][0]:
                        gap[i][0] = line[5]
                    elif line[5] > gap[i][1]:
                        gap[i][1] = line[5]
                else:
                    gap[i] = [line[5], line[5]]
            line = f.readline()
    gap = list(gap.items())
    gap.sort(key=lambda x: x[1][1] - x[1][0], reverse=True)
    print('(6)')
    temp = gap[2][1][1] - gap[2][1][0]
    for i in gap:
        g = i[1][1] - i[1][0]
        if g >= temp:
            print(i[0], g)

def seven():
    s = set(['Johnny Depp'])
    old_len = -1
    new_len = 0
    while new_len > old_len:
        old_len = new_len
        with open('IMDB-Movie-Data.csv') as f:
            line = f.readline()
            line = f.readline()
            while line:
                line = line.split(',')
                line[4] = [i.strip() for i in line[4].split('|')]
                for i in line[4]:
                    if i in s:
                        s = s.union(line[4])
                line = f.readline()
        new_len = len(s)
    print('(7)')
    print(len(s))
    print(s)

one()
two()
three()
four()
five()
six()
seven()