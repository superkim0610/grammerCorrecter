class WordCount:
    def __init__(self):
            self.count = 0
            self.text = []
    def add(self, text):
            t = text.strip().split()
            self.text += t
            self.count += len(t)
            print(len(t))

def main():
    wd = WordCount()
    with open('eng_task.txt', 'r', encoding='UTF-8') as f:
        for l in f:
            l = l.strip()
            if l.startswith('-'):
                l = l[2:]
                wd.add(l)
    print(wd.count)
    print(' '.join(wd.text))
    with open('eng_taks_final.txt', 'w', encoding='UTF-8') as f:
        f.write(' '.join(wd.text))
        

if __name__ == '__main__':
    main()