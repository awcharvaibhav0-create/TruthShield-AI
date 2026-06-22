import json
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "source_scores.json"
)

with open(file_path, "r") as f:
    SOURCE_SCORES = json.load(f)


def analyze_source(source_name):

    source = source_name.lower()

    for key, score in SOURCE_SCORES.items():

        if key in source:
            return {
                "source": source_name,
                "score": score
            }

    return {
        "source": source_name,
        "score": SOURCE_SCORES["unknown"]
    }