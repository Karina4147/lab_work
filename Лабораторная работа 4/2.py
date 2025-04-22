import json

# TODO решите задачу
def task() -> float:
    with open('input.json', encoding="utf-8") as f:
        json_data = json.load(f)
        all_score = [value["score"] * value["weight"] for value in json_data]
        result = round(sum(all_score),3)
        return result


print(task())
