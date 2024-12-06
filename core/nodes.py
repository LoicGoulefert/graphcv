import cv2


class BaseNode:
    def __init__(self, label, inputs=None, outputs=None, parameters=None):
        self.label = label
        self.inputs = inputs or []
        self.outputs = outputs or []
        self.parameters = parameters or {}

    def process(self, input_data):
        raise NotImplementedError()


class ImageInputNode(BaseNode):
    def __init__(self, label):
        pass


class ThresholdNode(BaseNode):
    def __init__(self, label="Threshold"):
        default_parameters = {
            "threshold": {
                "value": 128,
                "min_value": 0,
                "max_value": 255,
                "type": "int",
            },
            "max_value": {
                "value": 255,
                "min_value": 0,
                "max_value": 255,
                "type": "int",
            },
            "threshold_type": {
                "value": "BINARY",
                "type": "enum",
                "options": [
                    "BINARY",
                    "BINARY_INV",
                    "TRUNC",
                    "TOZERO",
                    "TOZERO_INV",
                ],
            },
            "otsu": {"value": False, "type": "bool"},
        }
        inputs = ["Grayscale image"]
        outputs = ["Th image"]

        super().__init__(
            label,
            inputs=inputs,
            outputs=outputs,
            parameters=default_parameters,
        )


class AdaptativeThresholdNode(BaseNode):
    def __init__(self, label="Adaptative Threshold"):
        default_parameters = {
            "method": {
                "value": "MEAN",
                "type": "enum",
                "options": ["MEAN", "GAUSSIAN"],
            },
            "blockSize": {
                "value": 5,
                "type": "int",
            },
            "C": {
                "value": 2,
                "type": "int",
            },
        }
        inputs = ["Grayscale image"]
        outputs = ["Th image"]

        super().__init__(
            label,
            inputs=inputs,
            outputs=outputs,
            parameters=default_parameters,
        )
