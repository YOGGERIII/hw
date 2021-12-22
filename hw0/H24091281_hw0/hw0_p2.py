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
one()

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
two()

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
                    rating.append(line[7])
            line = f.readline()
    sum = 0
    for rate in rating:
        rate = float(rate)
        sum = rate + sum
    average = sum / len(rating)
    print('(3)')
    print(average)


one()
two()
three()