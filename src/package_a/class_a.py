class Class_A:
    def __init__(self, num):
        self.num = num
        
    def __str__(self):
        return str(self.num)

def main():
    print(Class_A('A'))

if __name__ == '__main__':
    main()