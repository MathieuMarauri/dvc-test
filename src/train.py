import pandas as ps
from joblib import dump
from sklearn.ensemble import RandomForestClassifier

if __name__ == "__main__":

	# on récupère les données
	train = ps.read_csv("data/prepared/train.csv")

	# split features/traget
	y = train.Survived
	X = train.drop('Survived', axis=1)

	# apprentissage d'un modèle
	clf = RandomForestClassifier(
		max_depth=1,
		n_estimators=1,
		max_features=1,
		criterion='gini',
		random_state=0)
	clf.fit(X, y)
	dump(clf, "model/model.joblib")
