def r_value(qrels_list, ret_list):
    r_value_list_combine = []

    for result in ret_list:

        r_value_list = []

        for i in range(len(result)):
            for j in range(len(qrels_list)):
                if result[i] == qrels_list[j] and i % 4 == 0 and j % 2 == 0:

                    all_rel_doc_num = len(qrels_list[j+1])
                    rel_doc_num = 0

                    r_value_list.append(result[i])

                    for ret in result[i + 1]:
                        for rel_list in qrels_list[j + 1]:
                            if ret == rel_list[0]:
                                rel_doc_num += 1
                    r_value_list.append([rel_doc_num / all_rel_doc_num])

        r_value_list_combine.append(r_value_list)

    return r_value_list_combine