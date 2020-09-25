def load(filename, k_value, qrels_list):
    '''
    If the value of k_value is "r", the function will use the number of relevant document as k value for each query.
    If the value of k_value is "all", the function will contain all the retrieved documents.
    Return format: list
    [[query01], [doc_id01, doc_id02, ...], [doc_rank01, doc_rank02, ...], [doc_p01, doc_p02, ...], [query02], [doc_id01, ...], ...]
    '''
    result = []

    file = open(filename, 'r')

    identical_variable = 1
    query_num = []

    if k_value == "r":
        index = 1
        doc_length = len(qrels_list[index])

    for line in file.readlines():
        if identical_variable == 1:
            doc_id, doc_p, doc_rank = [], [], []

            query_num = line.strip().split(' ')[0]
            result.append([query_num])

            doc_id.append(line.strip().split(' ')[2])
            doc_rank.append(line.strip().split(' ')[3])
            doc_p.append(line.strip().split(' ')[4])

            identical_variable +=1

        elif query_num != line.strip().split(' ')[0]:
            if k_value == "r":
                index += 2
                doc_length = len(qrels_list[index])

            result.append(doc_id)
            result.append(doc_rank)
            result.append(doc_p)
            doc_id, doc_p, doc_rank = [], [], []

            query_num = line.strip().split(' ')[0]
            result.append([query_num])

            doc_id.append(line.strip().split(' ')[2])
            doc_rank.append(line.strip().split(' ')[3])
            doc_p.append(line.strip().split(' ')[4])

        elif query_num == line.strip().split(' ')[0]:

            if k_value != "all" and k_value != "r":
                if len(doc_id) >= k_value:
                    continue

            if k_value == "r":
                if len(doc_id) >= doc_length:
                    continue

            doc_id.append(line.strip().split(' ')[2])
            doc_rank.append(line.strip().split(' ')[3])
            doc_p.append(line.strip().split(' ')[4])

    result.append(doc_id)
    result.append(doc_rank)
    result.append(doc_p)

    file.close()

    return result

