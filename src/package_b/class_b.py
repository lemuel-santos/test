class Class_B:
    def __init__(self, num):
        self.num = num*2
        
    def __str__(self):
        return str(self.num)

def main():
    print(Class_B(5))

if __name__ == '__main__':
    main()