from module import coinOpenCV


def coinDolar():
    """
    docstring
    """

    coin = coinOpenCV.CoinOpenCV(folder="image",name_image="dolar_original.png")
    
    coin.turnToGray()

    coin.blurryImage(blurry_type=True)

    coin.imageThreshold(limit=255,min=65)

    coin.morphologicalTreatment()

    coin.SimpleBlobDetector()

    coin.drawDetectedCircle(True)

    coin.saveImage(folder="image_result",name_image="dolar_result.png")

    print(f"Number of coins = {coin.numberOfCoins(True)}")

    coin.presentImages(version= True)
    

    pass


def coinReal():
    """
    docstring
    """

    coin = coinOpenCV.CoinOpenCV(folder="image",name_image="real_original.jpg")
    coin.turnToGray()
    coin.blurryImage(blurry_type=False)
    coin.detectCircle()
    coin.drawDetectedCircle()
    coin.saveImage(folder="image_result",name_image="real_result.jpg")

    print(f"Number of coins = {coin.numberOfCoins()}")

    coin.presentImages()
    pass
