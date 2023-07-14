import pickle
import config
import numpy as np

class Wine():
    def __init__(self,fixed_acidity,volatile_acidity,citric_acid,residual_sugar,
                 chlorides,free_sulfur_dioxide,total_sulfur_dioxide,pH,sulphates,alcohol):
        
        self.fixed_acidity=fixed_acidity
        self.volatile_acidity=volatile_acidity
        self.citric_acid=citric_acid
        self.residual_sugar=residual_sugar         
        self.chlorides=chlorides
        self.free_sulfur_dioxide=free_sulfur_dioxide
        self.total_sulfur_dioxide=total_sulfur_dioxide
        self.pH=pH
        self.sulphates=sulphates
        self.alcohol=alcohol

    def __load_data(self):
        with open (config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

    def get_predicted_quality(self):
        self.__load_data()

        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = self.fixed_acidity
        test_array[0,1] = self.volatile_acidity
        test_array[0,2] = self.citric_acid
        test_array[0,3] = self.residual_sugar
        test_array[0,4] = self.chlorides
        test_array[0,5] = self.free_sulfur_dioxide
        test_array[0,6] = self.total_sulfur_dioxide
        test_array[0,7] = self.pH
        test_array[0,8] = self.sulphates
        test_array[0,9] = self.alcohol

        predicted_quality = np.around(self.model.predict(test_array)[0])
        return predicted_quality