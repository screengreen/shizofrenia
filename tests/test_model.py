from model_inference.model.models import TestModel


def test_TestModel():
    input_ = 'test_input'
    model = TestModel()
    assert model(input_) == f'i got input: {input_}'