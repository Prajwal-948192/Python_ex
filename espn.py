import calci
#print("from espn", __name__)
def main():
    eng1 = 250 #runs
    ind1 = 220
    eng2 = 180

    total_eng = calci.add(eng1, eng2)
    ind2 = calci.sub(total_eng , ind1)
    target = calci.add(ind2, 1)

    print("runs to win:", target)

if __name__ == "__main__":
    main()
