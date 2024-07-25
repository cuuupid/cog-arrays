from cog import BasePredictor, Path, Input
import numpy as np

class Predictor(BasePredictor):

    def setup(self):
        return None

    def predict(self,
        array: list[int] = Input(description="numerical array", default=[]),
        numpy: Path = Input(description=".npy file")
    ) -> str:
        arr = np.load(numpy, allow_pickle=True)
        return f'array: {len(array)}, numpy: {arr.shape}'
