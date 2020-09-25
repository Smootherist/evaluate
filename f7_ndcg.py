import f8_dcg
import f9_idcg

def ndcg(qrels_list, ret_list):
    dcg = f8_dcg.dcg(qrels_list, ret_list)
    idcg = f9_idcg.idcg(qrels_list, ret_list)

    ndcg_combine = []

    for index in range(len(dcg)):

        ndcg_list_4_each_query = []

        for index01 in range(len(dcg[index])):

            if index01 % 2 == 0:
                ndcg_list_4_each_query.append(dcg[index][index01])
            if index01 % 2 == 1:
                ndcg_list_4_each_query.append([dcg[index][index01][0]/idcg[index][index01][0]])

        ndcg_combine.append(ndcg_list_4_each_query)

    return ndcg_combine