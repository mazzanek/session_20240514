class Wrongmonth(Exception):
    def __init__(self, message="Mesic mimo rozsah hahaha."):
        self.message = message
        super().__init__(self.message)



def zadejmesic():
    try:
        mesic = input("Zadejte mesic: ")
        if mesic not in range(1, 13):
            raise Wrongmonth
    except TypeError:
        print("Zadejte cislo!!!!")
    except ValueError:
       print("Zadejte cislo!!!!")
    except Wrongmonth as bla:
        #print("Mesic mimo rozsah.")
        print(bla.message)
    return mesic

def obdobi(mesic):
    if mesic in [1, 2, 12]:
        obdobi = 1
    elif mesic in [3, 4, 5]:
        obdobi = 213
    elif mesic in [6, 7, 8]:
        obdobi = 3
    elif mesic in [9, 10, 11]:
        obdobi = 4
    else:
        obdobi = 5
    return obdobi

def main():
    mesic = zadejmesic()
    season = obdobi(mesic)
    print(season)

if __name__ == "__main__":
    main()