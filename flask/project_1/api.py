from transformers import pipeline

class API:

    def __init__(self):
        self.ner_model = pipeline(
            "ner",
            model="dslim/bert-base-NER",
            aggregation_strategy="simple"
        )

    def ner(self, text):
        result = self.ner_model(text)
        return result