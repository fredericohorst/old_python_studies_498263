import glob
import pandas as pd
import matplotlib.pyplot as plt
if __name__ == '__main__':


    # Reading all files in the directory

    fileNames=[]

    for file in glob.glob("/home/frederico/PycharmProjects/banking/banking_files/*.csv"):
        fileNames.append(file)

    fileNames.sort()


    # Reading the content of each file
    period = -1
    dictPanel = {}
    for fileName in fileNames:
        period = period+1
        print(period)
        df = pd.read_csv(fileName, skiprows=8, thousands='.', decimal=',', sep=';', error_bad_lines=False)
        # I remove all the lines in which the first column is not an integer (the id of the bank)
        df = df[df.ix[:, 0].apply(lambda x: str(x).isdigit())]

        myBankData = [0, 2, 10, 29]

        df = df.ix[:, myBankData]

        df.columns = ['id', 'institution', 'totalAsset', 'totalDeposits']

        dictPanel[period] = df

    # Transforming the dictionary in a typical panel data format

    for n, df in dictPanel.items():
        df['period'] = n

    panelDF = pd.concat([df for df in dictPanel.values()], ignore_index=True)
    panelDFSort = panelDF.sort_values(['institution', 'period'])

    # Printing results
    panelPrint = panelDFSort.set_index(['id', 'period', 'institution', 'totalAsset', 'totalDeposits'])

    panelPrint.to_csv('panelFile.csv', sep='\t')

    # Ploting results for Banco do Brasil
    # Note that the Id of Banco do Brasil is 99000000

    bbDF = panelDF.loc[panelDF['id'] == '99000000']
    BBtotalDepositsDF = bbDF.as_matrix(columns=['period', 'totalDeposits'])

    print (BBtotalDepositsDF)
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.plot(BBtotalDepositsDF[:, 0], BBtotalDepositsDF[:, 1]/100000000.0, 'bo-', markersize=4, markeredgewidth=0)
    ax1.set_ylabel('Total Deposits of BB')
    ax1.set_xlabel('Periods')