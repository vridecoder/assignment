from partion import Partionable

if __name__ == '__main__':
    # Inputs
    inputs = [
        [1, 2, 3, 4, 5, 6, 7],
        [1, 10, 5, 21, 4],
        [1, 10, 5, 21, 4, 1]]

    for arr in inputs:
        partion = Partionable(arr)
        if partion.canPartion() == True:
            print("Partionale")
        else:
            print("Non Partionable")
