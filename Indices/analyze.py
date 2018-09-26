def analise(age,index=False, gdp=False):
    import pandas as pd
    import indic
    if age==False:
        print(indic.indices.replace("_", " ").replace(".xls",""))
        return
    ind = indic.indices.split()
    lista, k = [None]*len(ind), 0
    for i in ind:
        lista[k] = pd.read_excel(i, sheet_name='Data', header=3)
        k+=1
    data,k,indices = pd.DataFrame(lista[0]['Country Name']),0, ['Country']
    for i in lista:
        indices += [ind[k].replace("_"," ").replace(".xls","")]
        data = data.join(i[str(age)])
        data.columns = indices
        k+=1
    data.index = data["Country"]
    data = data.drop("Country",1)
    if index == False:
        return data
    elif gdp == False:
        return data[index]
    else:
        return data[[index,'GDP per capita']].dropna()