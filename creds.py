import pickle
import secure


def getCreds():
    data = {}
    try:
        with open("creds.pickle", "rb") as dataLoad:
            data = pickle.load(dataLoad)

    except FileNotFoundError:
        print("You have no data . . .")
        secure.pickleOutData()
        with open("creds.pickle", "rb") as dataLoad:
            data = pickle.load(dataLoad)

    finally:
        return data['email'], data['password']


# print(getCreds())
