

def data_preparation(sample_name, form_dict):
    transitional_data_storrage = []
    transitional_data_storrage.append(sample_name)
    transitional_data_storrage.extend(form_dict.get(sample_name))
    return(transitional_data_storrage)


def prep_data_to_push(transitional_data_storrage):
    insert_data = ''
    for number, value in enumerate(transitional_data_storrage):
        if number <= len(transitional_data_storrage)-2:
            insert_data = insert_data + value + ', '
        else:
            insert_data = insert_data + value
    return(insert_data)


def data_writer(insert_data):
    with open('Data_Table_Diagn.csv', 'a+') as f:
        f.write(insert_data)
        f.write('\n')


form_dict = {
    "abc": ['ab', 'bc', 'cd'],
    "def": ['de', 'ef', 'fg'],
    "acb": ['ab', 'ab', 'bc']
}


samples_from_protocol = sorted(form_dict.keys())
for sample_name in samples_from_protocol:
    insert_data = prep_data_to_push(data_preparation(sample_name, form_dict))  # now we can push or write data on each step of cycle
    print(insert_data, "===> pushed")
    data_writer(insert_data)

