import numpy

def idcg(qrels_list, ret_list):

    idcg_list_combine = []

    for result in ret_list:

        idcg_list_4_each_file = []

        for i in range(len(result)):
            for j in range(len(qrels_list)):
                if result[i] == qrels_list[j] and i % 4 == 0 and j % 2 == 0:

                    idcg_list_4_each_file.append(result[i])

                    for rel_id in range(len(qrels_list[j + 1])):
                        if rel_id < len(result[i + 1]):
                            if rel_id == 0:
                                idcg_value_4_each_query = qrels_list[j+1][rel_id][1]

                            if rel_id > 0:
                                idcg_value_4_each_query += qrels_list[j+1][rel_id][1]/numpy.log2(rel_id + 1)
                    idcg_list_4_each_file.append([idcg_value_4_each_query])
        idcg_list_combine.append(idcg_list_4_each_file)

    return idcg_list_combine