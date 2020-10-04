# CoinCounterChallenge

The aim of this deaf person is to carry out the treatment of 2 images,each of them with 5 Real coins and the other with 9 dollar coins.
Below we have as images:

 

the program used the openCV library for python.
available in:
[Click here](https://pypi.org/project/opencv-python/)


In the code file it has the pythn scripts used to solve the challenge, while in the file DistributionFile/dist it has the program executable.

The images of dolar_original.png and real_original.jpg are placed in the image folder, after the program starts an interface with the user is opened.
the user selects which of the challenges he would like to perform, with a value of 1 to run the challenge Contando moedas de Real and 2 for Contando moedas de Dólar , if he wants to leave the program, just digital 0, but if
the user has run challenges 1 or 2, to choose the exit function, the user must first close all open image tabs during the process.

For creat the program was built the following class diagram:

![class diagram](https://github.com/richartzCoffee/CoinCounterChallenge/blob/main/1technicalDocumentation/image/classDiagram.png)


After the program runs, the images are saved in the image_result folder and the number of coins identified in the images is printed on the terminal.
In the end it is expected to obtain the following results in each images:
