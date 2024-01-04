#imports
import Analysis_repo
from Analysis_repo import notebook_import_library

# datafile URL
consumer_credit_data = notebook_import_library.pd.read_csv("Analysis_repo/Datasets/FRB_G13to23.csv", sep=",")
interest_rate_data = notebook_import_library.pd.read_csv("Analysis_repo/Datasets/FRB_InterestRate13to23.csv", sep=",")

# exception to catch what happens when dataset is called 
class datasetNotFoundException(Exception):
    pass 

# send data to notebook 
def sendConsumerCreditData():
    credit_analysis_data = consumer_credit_data
    return credit_analysis_data

def sendInterestRateData():
    int_rate_data = interest_rate_data
    return int_rate_data

# Code upgrading ideas
# connect data source via API COnnection instead of downloading dataset.


# Datset saving code
# # Save the DataFrame to a CSV file
#df.to_csv('dataset.csv', index=False)

# df.to_csv('Analysis_repo/Datasets/creditCardData_p2of2.csv', index=False)