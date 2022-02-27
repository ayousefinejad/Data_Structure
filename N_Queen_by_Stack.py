# Arshia_Yousefinezhad
# n queen by stack

n = int(input("Number : "))
while n < 4:
    n = int(input("Number: "))
# in the name of GOD

class stack:

    def __init__(self):
        lst = []
        for i in range(n):
            lst.append([0] * n)
        self._data = lst
        self.queen = 0
        self.n = 0
        self.nn = 0

# ------------------------------------------------------------------------------------------------------------------------
    def __len__(self):
        return len(self._data)

    def full(self):
        if self.nn == len(self._data):
            self.pop()
            self.push()
        return 0

    def found_nn(self):
        for i in range(len(self._data)):
            if self._data[self.n][i] == 1:
                self.nn = i

# MAIN______________________________________________________________________________________________________________________
# ------------------------------------------------------------------------------------------------------------------------
    def first(self):
        self._data[self.n][self.nn] = 1
        self.queen+=1


    def pop(self):
        self.nn -= 1
        self._data[self.n][self.nn] = 0
        self.queen -= 1
        self.n -= 1
        self.found_nn()
        # self.push()

    def push(self):
        self._data[self.n][self.nn] = 0
        self.nn +=1
        self.full()
        self._data[self.n][self.nn] = 1



    def add(self):
        self.nn = 0
        self.n += 1
        self._data[self.n][self.nn] = 1
        self.queen += 1
# ------------------------------------------------------------------------------------------------------------------------


# __________________________________________________________________________________________________________________________

    def column(self):
        for i in range(1, self.n+1):
            if self._data[self.n][self.nn] == self._data[self.n-i][self.nn] == 1:
                self.push()
                # self.show()
                return 0
        return 1


    def row(self):
        for i in self._data[self.n]:
            if i == 1:
                self.pop()
                return 0
        return 1

    def diameter1(self):
            if self.n > self.nn:
                for a in range(1, self.nn +1):
                    if self._data[self.n][self.nn] == self._data[self.n - a][self.nn - a] == 1:
                            self.push()
                            # self.show()
                            return 0


            else:
                for b in range(1, self.n + 1):
                    if self._data[self.n][self.nn] == self._data[self.n - b][self.nn - b] == 1:
                        self.push()
                        # self.show()
                        return 0
            return 1


    def diameter2(self):
        if self.n + self.nn < len(self._data):
            for a in range(1, self.n+1):
                if self._data[self.n][self.nn] == self._data[self.n-a][self.nn+a] == 1:
                    self.push()
                    # self.show()
                    return 0
        else:
            for b in range(1, len(self._data) - self.nn):
                if self._data[self.n][self.nn] == self._data[self.n-b][self.nn+b] == 1:
                    self.push()
                    # self.show()
                    return 0
        return 1
# ------------------------------------------------------------------------------------------------------------------------


    def show(self):
        for i in self._data:
            print(i)
        print()

    def act(self):
        for i in range(len(self._data)):
            line = ""
            for j in range(len(self._data)):
                if self._data[i][j] == 1:
                    line += " Q "
                else:
                    line += " - "
            print(line)
        print()


    def test(self):
        if self.nn > len(self._data):
            self.pop()

# HERE----------------------------------------------------------------------------------------------------------------
# _______________________________________________________________________________________________________________________
    def main(self):
        self.first()
        while self.queen < len(self._data):
            self.add()
            while True:
                self.column()
                self.diameter1()
                self.diameter2()
                if self.column() == self.diameter2() == self.diameter1() == 1:
                    # self.show()
                    break

# -----------------------------------------------------------------------------------------------------------------------


st = stack()
st.main()


print("Finisher")
st.show()
st.act()

