def p_value(qrels_list, ret_list):
    '''
    Return the list with multiple sub list.
    Each sub list contains the precision value for s[1-6].results respectively.

    The format of whole list is [[sub list 01], [sub list 02], ...... ]
    The format of sub list is [[query01], [precision01], [query02], [precision02], ...... ]
    '''

    p_value_list_combine = []

    for result in ret_list:

        p_value_list = []

        for i in range(len(result)):
            for j in range(len(qrels_list)):
                if result[i] == qrels_list[j] and i%4 == 0 and j%2 == 0:

                    ret_doc_num = len(result[i+1])
                    rel_doc_num = 0

                    p_value_list.append(result[i])

                    for ret in result[i+1]:
                        for rel_list in qrels_list[j+1]:
                            if ret == rel_list[0]:
                                rel_doc_num += 1
                    p_value_list.append([rel_doc_num/ret_doc_num])

        p_value_list_combine.append(p_value_list)

    return p_value_list_combine







    #
    #
    #
    #
    #     for i in range(len(result)):
    #
    #         if i % 4 == 0:
    #             relevant_doc = 0
    #             p_value_list.append(result[i])
    #         elif i % 4 == 1:
    #             retrieved_doc = len(result[i])
    #
    #
    #
    #
    #
    #
    #
    #
    #             for doc_id_ret in result[i]:
    #                 for j in range(len(qrels_list)):
    #                     if j % 2 == 1:
    #                         for doc_id_qrels in qrels_list[int(i/4)*2+1]:
    #                             if doc_id_qrels[0] == doc_id_ret:
    #                                 relevant_doc += 1
    #             p_value_list.append([relevant_doc / retrieved_doc])
    #
    #     p_value_list_combine.append(p_value_list)
    #
    # return p_value_list_combine

