import cv2


class BaseNode:
    def __init__(self, label, inputs=None, outputs=None, parameters=None):
        self.label = label
        self.inputs = inputs or []
        self.outputs = outputs or []
        self.parameters = parameters or {}

    def process(self, input_data):
        raise NotImplementedError()


class ThresholdNode(BaseNode):
    def __init__(self, label="Threshold", parameters=None):
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
                "type": "combo",
                "options": [
                    "BINARY",
                    "BINARY_INV",
                    "TRUNC",
                    "TOZERO",
                    "TOZERO_INV",
                ],
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
