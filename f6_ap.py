def ap(qrels_list, ret_list):
    '''
    This function will return AP value for each query in s[1-6].results files respectively.
    The format of return list is [sublist01, sublist02, ......], where sublist_n is [[query01], [AP01], [query02], [AP02], ...... ]
    '''

    ap_list_all = []

    for result in ret_list:
        ap_list_4_each_file = []
        for i in range(len(qrels_list)):
            for j in range(len(result)):

                if qrels_list[i] == result[j] and i%2 == 0 and j%4 == 0:
                    ap_list_4_each_file.append(qrels_list[i])
                    ap_sum, ap_n =0, 1
                    for doc_id_ret in range(len(result[j+1])):
                        for doc_id_rel in range(len(qrels_list[i+1])):
                            if result[j+1][doc_id_ret] == qrels_list[i+1][doc_id_rel][0]:
                                ap_sum += ap_n / int(result[j+2][doc_id_ret])
                                ap_n += 1
                    ap_list_4_each_file.append([ap_sum/len(qrels_list[i + 1])])
        ap_list_all.append(ap_list_4_each_file)

    return ap_list_all