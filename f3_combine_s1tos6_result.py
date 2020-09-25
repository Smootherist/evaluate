import f2_import_result

def combine(qrels_list, relevant_num):
    '''
    If the value of "relevant_num" is "r", the function will use r-precision
    Extract top relevant_num of the retrieved documents from S[1-6].results documents and put them into a list.
    '''
    combined_result = [i for i in range(6)]

    combined_result[0] = f2_import_result.load("S1.results", relevant_num, qrels_list)
    combined_result[1] = f2_import_result.load("S2.results", relevant_num, qrels_list)
    combined_result[2] = f2_import_result.load("S3.results", relevant_num, qrels_list)
    combined_result[3] = f2_import_result.load("S4.results", relevant_num, qrels_list)
    combined_result[4] = f2_import_result.load("S5.results", relevant_num, qrels_list)
    combined_result[5] = f2_import_result.load("S6.results", relevant_num, qrels_list)


    return combined_result