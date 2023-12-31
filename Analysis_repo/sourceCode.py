import Analysis_repo
from Analysis_repo import notebook_import_library

# datafile URL

#df = dd.read_csv('your_dataset.csv')
creditcardData_p1 = notebook_import_library.pd.read_csv("Analysis_repo/Datasets/creditCardData_p1of2.csv" , sep=",")
creditcardData_p2 = notebook_import_library.pd.read_csv("Analysis_repo/Datasets/creditCardData_p2of2.csv" , sep=",")
creditcardData_prediction = notebook_import_library.pd.read_csv("Analysis_repo/Datasets/creditCardData_prediction.csv", sep=",")


# exception to catch what happens when dataset is called 
class datasetNotFoundException(Exception):
    pass 

# imports 
def sendCreditCardData_part1():
    analysis_size_data = creditcardData_p1
    return analysis_size_data

def sendCreditCardData_part2():
    analysis_size_data = creditcardData_p2
    return analysis_size_data


def sendPredictionDataset():
    return creditcardData_prediction


import dask.dataframe as dd


# Datset saving code
# # Save the DataFrame to a CSV file
#df.to_csv('dataset.csv', index=False)


# creditcardData = pd.read_csv("C:/Users/stanf/OneDrive/Desktop/creditcard_mod.csv" , sep=",")
# df = creditcardData.iloc[45000:90000]
# print(df)


# df.to_csv('Analysis_repo/Datasets/creditCardData_p2of2.csv', index=False)