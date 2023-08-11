import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

#variant e
X = [
    [1, 4, 6, 8],
    [0, 6, 7, 8],
    [4, 6, 9],
    [2, 4, 5],
    [0, 1, 8, 9],
    [2, 4, 5, 7],
    [2, 4, 5, 7],
    [1, 9],
    [3, 4, 5, 8],
    [3, 4]
]

data = [list(map(str, row)) for row in X]
te = TransactionEncoder()
te_ary = te.fit_transform(data)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)


rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)


print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules)