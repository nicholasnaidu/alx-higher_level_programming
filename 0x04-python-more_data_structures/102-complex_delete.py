98% of storage used … If you run out, you won't have enough storage to create, edit, and upload files. Get 100 GB of storage for R 34.99 R 8.99/month for 3 months.
#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for value_dic in list_keys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return (a_dictionary)
