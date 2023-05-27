from src.utils import load_operations, get_five_last_operations, sorted_by_date, information_output
filename = '../data/operations.json'
def main():
    json_dict = load_operations(filename)
    list_sorted = sorted_by_date(json_dict)
    last_5 = get_five_last_operations(list_sorted)
    print(information_output(last_5))
main()
