import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

#variant a)
X_train = np.array([
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 1, 0]
])
y_train = np.array([0, 1, 1, 1, 0, 0, 1, 1, 0, 0])

sample = np.array([1, 1, 1, 1])

class PredictionMethod:
    def __init__(self, x, y):
        self.header = ['Q1', 'Q2', 'Q3', 'Q4']
        self.x = x
        self.y = y
        
    def format(self, data):
        return f"{self.__class__.__name__}: {self.predict(data)}\n\n"
    
    def predict(self):
        raise NotImplementedError

class OneRule(PredictionMethod):
    def predict(self, data):
        matches = np.sum(self.x.T == y_train, axis=1)
        reverse = np.sum(self.x.T != y_train, axis=1)
        
        best = max(np.max(matches), np.max(reverse))

        for key, value in enumerate(matches):
            if value == best:
                return f"S~ {self.header[key]} with {self.x.shape[0] - value} errors. Prediction: S = {data[key]}"

        for key, value in enumerate(reverse):
            if value == best:
                return f"S~ Not {self.header[key]} with {self.x.shape[0] - value} errors. Prediction: S = {1 - data[key]}"


class NaiveBayes(PredictionMethod):
    def __init__(self, X, y):
        self.classes = np.unique(y)
        self.priors = np.zeros(len(self.classes))
        self.likelihoods = []

        for i, c in enumerate(self.classes):
            self.priors[i] = np.sum(y == c) / len(y)

        for i in range(X.shape[1]):
            feature_likelihoods = []
            for c in self.classes:
                X_c = X[y == c]
                feature_likelihood = (np.sum(X_c[:, i] == 1) + 1) / (len(X_c) + 2)  # Згладжування Лапласа
                feature_likelihoods.append(feature_likelihood)
            self.likelihoods.append(feature_likelihoods)

    def predict(self, X):
        predictions = []
        for x in X.reshape(1, -1):
            posteriors = []
            for i, c in enumerate(self.classes):
                posterior = np.log(self.priors[i]) + sum(np.log(self.likelihoods[j][i] if x[j] == 1 else 1 - self.likelihoods[j][i]) for j in range(len(x)))
                posteriors.append(posterior)
            predictions.append(self.classes[np.argmax(posteriors)])
        ret = "Class Priors:\n"
        for i, c in enumerate(self.classes):
            ret += f"P({c}) = {self.priors[i]}\n"

        ret += "\nFeature Likelihoods:\n"
        for i in range(len(self.likelihoods)):
            ret += f"Feature {i+1}:\n"
            for j, c in enumerate(self.classes):
                ret += f"P(X_{i+1} = 1 | {c}) = {self.likelihoods[i][j]}\n"

        return f"{ret}\nResult: {predictions[0]}"
    
class DecisionTree(PredictionMethod):
    def predict(self, X):
        self.tree = DecisionTreeClassifier()
        self.tree.fit(self.x, self.y)
        self.print_tree_structure(0, 0)
        return self.tree.predict(X.reshape(1, -1))[0]
    
    def print_tree_structure(self, node, depth):
        structure = self.tree.tree_
        indent = "  " * depth
        if structure.feature[node] == -2:
            print(f"{indent}Leaf node. Class: {structure.value[node]}")
        else:
            print(f"{indent}Split on feature {structure.feature[node]}. Threshold: {structure.threshold[node]}")
            self.print_tree_structure(structure.children_left[node], depth + 1)
            self.print_tree_structure(structure.children_right[node], depth + 1)


class KNN(PredictionMethod):
    def predict(self, X, k=3):
        self.knn = KNeighborsClassifier(n_neighbors=k)
        self.knn.fit(self.x, self.y)
        
        return f"{self.knn.kneighbors_graph()}\nResult: {self.knn.predict(X.reshape(1, -1))[0]}"
        


def main():
    for method in (OneRule, NaiveBayes, DecisionTree, KNN):
        print(method(X_train, y_train).format(sample))
    

main()
