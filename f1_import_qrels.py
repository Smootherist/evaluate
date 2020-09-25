def load(filename):
    qrels = []

    file = open(filename, 'r')

    for line in file.readlines():
        line = line.strip()
        query_num = line.split(':')[0]
        qrels.append([query_num])
        query_rel = line.split(':')[1].strip().split(' ')

        list_for_tuples_elements = []

        for tuples in query_rel:
            if tuples != '':
                doc_id = tuples.strip('()').split(',')[0]
                rel_value = int(tuples.strip('()').split(',')[1])
                list_for_tuples_elements.append([doc_id, rel_value])

        qrels.append(list_for_tuples_elements)

    file.close()

    return qrels






