import numpy

def dcg(qrels_list, ret_list):

    dcg_list_combine = []

    for result in ret_list:

        dcg_list_4_each_file = []

        for i in range(len(result)):
            for j in range(len(qrels_list)):
                if result[i] == qrels_list[j] and i%4 == 0 and j%2 == 0:

                    dcg_list_4_each_file.append(result[i])

                    for ret_id in range(len(result[i+1])):
                        if ret_id == 0:

                            dcg_value_4_each_query = 0

                            for rel_id in range(len(qrels_list[j + 1])):
                                if result[i+1][ret_id] == qrels_list[j+1][rel_id][0]:
                                    dcg_value_4_each_query = qrels_list[j+1][rel_id][1]

                        if ret_id > 0:
                            for rel_id in range(len(qrels_list[j + 1])):
                                if result[i+1][ret_id] == qrels_list[j+1][rel_id][0]:
                                    dcg_value_4_each_query += qrels_list[j+1][rel_id][1]/numpy.log2(ret_id+1)

                    dcg_list_4_each_file.append([dcg_value_4_each_query])
        dcg_list_combine.append(dcg_list_4_each_file)

    return dcg_list_combine