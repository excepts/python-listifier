def listify(text):
    l = ['\nLIST:\n']+text.split(' ')
    print(l[0]+str([i for i in l if l.index(i) != 0]))
    input()

if __name__ == '__main__':
	listify(input('TEXT:\n'))