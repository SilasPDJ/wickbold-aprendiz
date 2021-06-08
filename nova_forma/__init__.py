import pandas as pd

f = pd.read_excel('C:\\Users\\f2900039\\Desktop\\NOVA_FORMA_IMPORTAR\\Pasta1.xlsx')
df = f.to_dict()

a_partir_atual = 0

def dale():
    for k, items in df.items():
        for e, val in enumerate(items.values()):
            if e >= a_partir_atual:
                yield val
