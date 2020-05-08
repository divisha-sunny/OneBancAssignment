import pandas as pd

def firstInput():
    input1 = pd.read_csv('Interview_Fresher_Any_Language\HDFC-Input-Case1.csv', sep='\t', header=None)
    input1.columns = ['Information']

    input1[['Date','Transaction_Desciption','Debit']] = input1.Information.str.split(",",expand=True,)
    del input1['Information']
    inputa=input1[4:9]
    inputa["Credit"] = 0
    inputa["CardName"] = "Rahul"
    inputa["Transaction"] = "Domestic"
    inputb = input1[20:26]
    inputb["Credit"] = 0
    inputb["CardName"] = "Rahul"
    inputb["Transaction"] = "International"
    inputc = input1[12:16]
    inputc["Credit"] = 0
    inputc["CardName"] = "Ritu"
    inputc["Transaction"] = "Domestic"
    answere = inputa.append(inputc, ignore_index=True)
    answere1 = answere.append(inputb, ignore_index=True)
    
    return answere1

def secondInput():
    input2 = pd.read_csv('Interview_Fresher_Any_Language\ICICI-Input-Case2.csv', sep='\t', header=None)
    input2.columns = ['Information']

    x = input2[4:10]
    x[['Date','Transaction_Desciption','Debit','Credit']] = x.Information.str.split(",",expand=True,)
    x["CardName"] = "Rahul"
    y = input2[12:23]
    y[['Date','Transaction_Desciption','Debit','Credit']] = y.Information.str.split(",",expand=True,)
    y["CardName"] = "Raj"
    del x['Information']
    del y['Information']
    y["Transaction"] = "Domestic"
    x["Transaction"] = "Domestic"
    xy = x.append(y, ignore_index=True)
    z = input2[27:33]
    z[['Date','Transaction_Desciption','Debit','Credit']] = z.Information.str.split(",",expand=True,)
    del z["Information"]
    z["CardName"] = "Raj"
    z["Transaction"] = "International"
    answere4 = xy.append(z, ignore_index=True)

    return answere4
    #answere4.to_csv('ICICI-Output-Case2.csv')  

def thirdInput():
    input3 = pd.read_csv('Interview_Fresher_Any_Language\Axis-Input-Case3.csv', sep='\t', header=None)
    input3.columns = ['Information']   

    input3[['Date','Debit','Credit','Transaction_Details']] = input3.Information.str.split(",",expand=True,)
    del input3['Information']
    input3a = input3[4:11]
    input3a["CardName"] = "Rahul"
    input3a["Transaction"] = "Domestic"
    input3b = input3[15:22]
    input3b["CardName"] = "Ritu"
    input3b["Transaction"] = "Domestic"
    input3c = input3[28:34]
    input3c["CardName"] = "Rahul"
    input3c["Transaction"] = "International"
    answere_a = input3a.append(input3b, ignore_index=True)
    answere2 = answere_a.append(input3c, ignore_index=True)
    answere2 = answere2[['Date','Transaction_Details','Debit','Credit','CardName','Transaction']]
    
    return answere2
    #answere2.to_csv('Axis-Output-Case3.csv')

def fourthInput():
    input4 = pd.read_csv('Interview_Fresher_Any_Language\IDFC-Input-Case4.csv', sep='\t', header=None)
    input4.columns = ['Information']    

    a=input4[6:9]
    a[['Transaction_Desciption','Date','Debit']] = a.Information.str.split(",",expand=True,)
    del a['Information']
    b=input4[10:16]
    b[['Transaction_Desciption','Date','Debit']] = b.Information.str.split(",",expand=True,)
    del b['Information']
    ab = a.append(b, ignore_index=True)
    ab["CardName"] = "Rahul"
    ab["Transaction"] = "Domestic"
    c=input4[22:28]
    d=input4[29:32]
    c[['Transaction_Desciption','Date','Debit']] = c.Information.str.split(",",expand=True,)
    del c['Information']
    d[['Transaction_Desciption','Date','Debit']] = d.Information.str.split(",",expand=True,)
    del d['Information']
    cd = c.append(d, ignore_index=True)
    cd["CardName"] = "Rajat"
    cd["Transaction"] = "Domestic"
    e = input4[37:43]
    e[['Transaction_Desciption','Date','Debit']] = e.Information.str.split(",",expand=True,)
    del e['Information']
    e["CardName"] = "Rahul"
    e["Transaction"] = "International"
    f = ab.append(cd, ignore_index=True)
    answere3 = f.append(e, ignore_index=True)
    answere3["Credit"] = 0
    answere3 = answere3[['Date','Transaction_Desciption','Debit','Credit','CardName','Transaction']]
    
    return answere3
    #answere3.to_csv('IDFC-Output-Case4.csv')
