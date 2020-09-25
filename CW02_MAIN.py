import numpy
import f1_import_qrels
import f3_combine_s1tos6_result
import f4_precision
import f5_recall
import f6_ap
import f7_ndcg
import f10_output_eval


qrels = f1_import_qrels.load("qrels.txt")

# Calculate the P@10
result_10 = f3_combine_s1tos6_result.combine(qrels, 10)
result_10_p = f4_precision.p_value(qrels, result_10)

# Calculate the R@50
result_50 = f3_combine_s1tos6_result.combine(qrels, 50)
result_50_r = f5_recall.r_value(qrels, result_50)

# Calculate the r-precision
result_R = f3_combine_s1tos6_result.combine(qrels, "r")
result_R_p = f4_precision.p_value(qrels, result_R)

# Calculate the AP
result_ap = f3_combine_s1tos6_result.combine(qrels, "all")
result_ap_value = f6_ap.ap(qrels, result_ap)

# Calculate the nDCG@10
result_10_ndcg = f7_ndcg.ndcg(qrels, result_10)

# Calculate the nDCG@20
result_20 = f3_combine_s1tos6_result.combine(qrels, 20)
result_20_ndcg = f7_ndcg.ndcg(qrels, result_20)

# Out put eval file
f10_output_eval.output(result_10_p, result_50_r, result_R_p, result_ap_value, result_10_ndcg, result_20_ndcg)

