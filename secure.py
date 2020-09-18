import pickle


def getCredentials():
    print('here')
    eMail = input("Enter Your Email\n>>>")
    print()
    print()
    passWd = input("Enter Your password\n>>>")
    return eMail, passWd


def pickleOutData():
    eMail, passWd = getCredentials()
    data = {
        "email": eMail,
        "password": passWd
    }

    with open("creds.pickle", "wb") as file:
        pickle.dump(data, file)


if __name__ == "__main__":
    pickleOutData()