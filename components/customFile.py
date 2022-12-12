import pandas as pd
import pickle

class CustomFile:
    def __init__(self) -> None:
        self.trainFile = pd.read_csv('./datasets/Training.csv')
        self.nb_model = None
        self.medicineFile = pd.read_csv('./datasets/Disease_Medication-Testing.csv')

        with open('./models/nb_model.pkl', 'rb') as file:
            self.nb_model = pickle.load(file)
        # self.testFile = None


    def getFeatures(self):
        features = (self.trainFile.columns.values)[:-2]
        features = sorted([feature.replace("_", " ").capitalize() for feature in features])
        # features = {feature: feature.replace("_", " ").capitalize() for feature in features}

        return features

    def getEncoder(self):
        features = (self.trainFile.columns.values)[:-2]
        encoder = {feature.replace("_", " ").capitalize(): i for i, feature in enumerate(features)}

        return encoder

    def getPredictionClasses(self):
        classes = self.trainFile["prognosis"].unique()
        classes = sorted(classes)
        return classes

    def getMedication(self):
        medication = self.medicineFile.to_dict(orient="index")
        output = {row['prognosis']: row['Medication'] for _, row in medication.items()}
        # print(output)
        return output
