from utils import load_operations, get_five_last_operations, sorted_by_date, information_output

filename = "../data/operations.json"

if __name__ == '__main__':

    json_dict = load_operations(filename)
    date_sorted = sorted_by_date(json_dict)
    last_5 = get_five_last_operations(date_sorted)
    print(information_output(last_5))
