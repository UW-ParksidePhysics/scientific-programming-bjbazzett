code_snippets = {
    "working_dict": {
        "code": """numbers = {}\nnumbers[0] = -5\nnumbers[1] = 10.5""",
        "explanation": (
            "It works because dictionaries allow whatever you want without pre-defined elements"),"fix": None},
    "non_working_list": {
        "code": """other_numbers = []\nother_numbers[0] = -5\nother_numbers[1] = 10.5""",
        "explanation": (
            "IndexError due to the list not being large enough to fit said index, cant assign an index 0/1 to an empty list"),
        "fix": """other_numbers = [0, 0]\nother_numbers[0] = -5\nother_numbers[1] = 10.5"""}}

def display_snippets(snippets):
    for key, info in snippets.items():
        print(f"--- Code snippet: {key} ---")
        print("Code:")
        print(info["code"])
        print("\nExplanation:")
        print(info["explanation"])
        if info["fix"]:
            print("\nFixed Version:")
            print(info["fix"])
        print("\n")

if __name__ == '__main__':
    display_snippets(code_snippets)