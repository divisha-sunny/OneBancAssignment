import pandas as pd

from python import firstInput
from python import secondInput
from python import thirdInput
from python import fourthInput

input1 = pd.read_csv('Interview_Fresher_Any_Language\HDFC-Input-Case1.csv', sep='\t', header=None)
input1.columns = ['Information']

input2 = pd.read_csv('Interview_Fresher_Any_Language\ICICI-Input-Case2.csv', sep='\t', header=None)
input2.columns = ['Information']

input3 = pd.read_csv('Interview_Fresher_Any_Language\Axis-Input-Case3.csv', sep='\t', header=None)
input3.columns = ['Information']

input4 = pd.read_csv('Interview_Fresher_Any_Language\IDFC-Input-Case4.csv', sep='\t', header=None)
input4.columns = ['Information']

inputFile = 'input1'

def StandardizeStatement(inputFile):

    if(inputFile == 'input1'):
        return firstInput()

    if(inputFile == 'input2'):
        return secondInput()

    if(inputFile == 'input3'):
        return thirdInput()

    else:
        return fourthInput()

        
