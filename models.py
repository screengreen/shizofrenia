import joblib

class TestModel():
    def __call__(self, input_):
        print(input_)
        return input_
    

class ResponseModel():

    def __call__(self, input_):
        return NotImplementedError
    


class ModelLoader:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ModelLoader, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, model_path):
        if not self._initialized:
            self.model_path = model_path
            self.model = None
            self._initialized = True

    def load_model(self):
        if self.model is None:
            # self.model = joblib.load(self.model_path)
            self.model = TestModel()
        return self.model
    

# Создайте экземпляр ModelLoader и загрузите модель
model_loader = ModelLoader('path/to/your/model.pkl')