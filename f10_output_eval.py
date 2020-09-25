import numpy

def output(p_10, r_50, R_p, ap_value, ndcg_10, ndcg_20):

    all_score = open('All.eval', 'w')
    all_score.write(' \tP@10\tR@50\tr-Precision\tAP\tnCCG@10\tnDCG@20')

    # Out put 1st file
    file_num = 0

    s = open('S1.eval', 'w')
    s.write(' \tP@10\tR@50\tr-Precision\tAP\tnCCG@10\tnDCG@20\n')

    mean_list = [[], [], [], [], [], []]

    for i in range(len(p_10[file_num])):
        if i % 2 == 1:
            s.write('%s' % p_10[file_num][i-1][0])
            s.write('\t%s' % round(p_10[file_num][i][0], 3))
            s.write('\t%s' % round(r_50[file_num][i][0], 3))
            s.write('\t%s' % round(R_p[file_num][i][0],3))
            s.write('\t%s' % round(ap_value[file_num][i][0], 3))
            s.write('\t%s' % round(ndcg_10[file_num][i][0], 3))
            s.write('\t%s\n' % round(ndcg_20[file_num][i][0], 3))

            mean_list[0].append(p_10[file_num][i][0])
            mean_list[1].append(r_50[file_num][i][0])
            mean_list[2].append(R_p[file_num][i][0])
            mean_list[3].append(ap_value[file_num][i][0])
            mean_list[4].append(ndcg_10[file_num][i][0])
            mean_list[5].append(ndcg_20[file_num][i][0])

    all_score.write('\nS1\t')

    s.write('mean\t')
    for i in range(len(mean_list)):
        s.write('%s\t' % round(numpy.mean(mean_list[i]), 3))
        all_score.write('%s\t' % round(numpy.mean(mean_list[i]), 3))

    s.close()





    # Out put 2nd file
    file_num += 1

    s = open('S2.eval', 'w')
    s.write(' \tP@10\tR@50\tr-Precision\tAP\tnCCG@10\tnDCG@20\n')

    mean_list = [[], [], [], [], [], []]

    for i in range(len(p_10[file_num])):
        if i % 2 == 1:
            s.write('%s' % p_10[file_num][i - 1][0])
            s.write('\t%s' % round(p_10[file_num][i][0], 3))
            s.write('\t%s' % round(r_50[file_num][i][0], 3))
            s.write('\t%s' % round(R_p[file_num][i][0], 3))
            s.write('\t%s' % round(ap_value[file_num][i][0], 3))
            s.write('\t%s' % round(ndcg_10[file_num][i][0], 3))
            s.write('\t%s\n' % round(ndcg_20[file_num][i][0], 3))

            mean_list[0].append(p_10[file_num][i][0])
            mean_list[1].append(r_50[file_num][i][0])
            mean_list[2].append(R_p[file_num][i][0])
            mean_list[3].append(ap_value[file_num][i][0])
            mean_list[4].append(ndcg_10[file_num][i][0])
            mean_list[5].append(ndcg_20[file_num][i][0])

    all_score.write('\nS2\t')

    s.write('mean\t')
    for i in range(len(mean_list)):
        s.write('%s\t' % round(numpy.mean(mean_list[i]), 3))
        all_score.write('%s\t' % round(numpy.mean(mean_list[i]), 3))

    s.close()





    # Out put 3rd file
    file_num += 1

    s = open('S3.eval', 'w')
    s.write(' \tP@10\tR@50\tr-Precision\tAP\tnCCG@10\tnDCG@20\n')

    mean_list = [[], [], [], [], [], []]

    for i in range(len(p_10[file_num])):
        if i % 2 == 1:
            s.write('%s' % p_10[file_num][i - 1][0])
            s.write('\t%s' % round(p_10[file_num][i][0], 3))
            s.write('\t%s' % round(r_50[file_num][i][0], 3))
            s.write('\t%s' % round(R_p[file_num][i][0], 3))
            s.write('\t%s' % round(ap_value[file_num][i][0], 3))
            s.write('\t%s' % round(ndcg_10[file_num][i][0], 3))
            s.write('\t%s\n' % round(ndcg_20[file_num][i][0], 3))

            mean_list[0].append(p_10[file_num][i][0])
            mean_list[1].append(r_50[file_num][i][0])
            mean_list[2].append(R_p[file_num][i][0])
            mean_list[3].append(ap_value[file_num][i][0])
            mean_list[4].append(ndcg_10[file_num][i][0])
            mean_list[5].append(ndcg_20[file_num][i][0])

    all_score.write('\nS3\t')

    s.write('mean\t')
    for i in range(len(mean_list)):
        s.write('%s\t' % round(numpy.mean(mean_list[i]), 3))
        all_score.write('%s\t' % round(numpy.mean(mean_list[i]), 3))

    s.close()





    # Out put 4th file
    file_num += 1

    s = open('S4.eval', 'w')
    s.write(' \tP@10\tR@50\tr-Precision\tAP\tnCCG@10\tnDCG@20\n')

    mean_list = [[], [], [], [], [], []]

    for i in range(len(p_10[file_num])):
        if i % 2 == 1:
            s.write('%s' % p_10[file_num][i - 1][0])
            s.write('\t%s' % round(p_10[file_num][i][0], 3))
            s.write('\t%s' % round(r_50[file_num][i][0], 3))
            s.write('\t%s' % round(R_p[file_num][i][0], 3))
            s.write('\t%s' % round(ap_value[file_num][i][0], 3))
            s.write('\t%s' % round(ndcg_10[file_num][i][0], 3))
            s.write('\t%s\n' % round(ndcg_20[file_num][i][0], 3))

            mean_list[0].append(p_10[file_num][i][0])
            mean_list[1].append(r_50[file_num][i][0])
            mean_list[2].append(R_p[file_num][i][0])
            mean_list[3].append(ap_value[file_num][i][0])
            mean_list[4].append(ndcg_10[file_num][i][0])
            mean_list[5].append(ndcg_20[file_num][i][0])

    all_score.write('\nS4\t')

    s.write('mean\t')
    for i in range(len(mean_list)):
        s.write('%s\t' % round(numpy.mean(mean_list[i]), 3))
        all_score.write('%s\t' % round(numpy.mean(mean_list[i]), 3))

    s.close()




    # Out put 5th file
    file_num += 1

    s = open('S5.eval', 'w')
    s.write(' \tP@10\tR@50\tr-Precision\tAP\tnCCG@10\tnDCG@20\n')

    mean_list = [[], [], [], [], [], []]

    for i in range(len(p_10[file_num])):
        if i % 2 == 1:
            s.write('%s' % p_10[file_num][i - 1][0])
            s.write('\t%s' % round(p_10[file_num][i][0], 3))
            s.write('\t%s' % round(r_50[file_num][i][0], 3))
            s.write('\t%s' % round(R_p[file_num][i][0], 3))
            s.write('\t%s' % round(ap_value[file_num][i][0], 3))
            s.write('\t%s' % round(ndcg_10[file_num][i][0], 3))
            s.write('\t%s\n' % round(ndcg_20[file_num][i][0], 3))

            mean_list[0].append(p_10[file_num][i][0])
            mean_list[1].append(r_50[file_num][i][0])
            mean_list[2].append(R_p[file_num][i][0])
            mean_list[3].append(ap_value[file_num][i][0])
            mean_list[4].append(ndcg_10[file_num][i][0])
            mean_list[5].append(ndcg_20[file_num][i][0])

    all_score.write('\nS5\t')

    s.write('mean\t')
    for i in range(len(mean_list)):
        s.write('%s\t' % round(numpy.mean(mean_list[i]), 3))
        all_score.write('%s\t' % round(numpy.mean(mean_list[i]), 3))

    s.close()





    # Out put 6th file
    file_num += 1

    s = open('S6.eval', 'w')
    s.write(' \tP@10\tR@50\tr-Precision\tAP\tnCCG@10\tnDCG@20\n')

    mean_list = [[], [], [], [], [], []]

    for i in range(len(p_10[file_num])):
        if i % 2 == 1:
            s.write('%s' % p_10[file_num][i - 1][0])
            s.write('\t%s' % round(p_10[file_num][i][0], 3))
            s.write('\t%s' % round(r_50[file_num][i][0], 3))
            s.write('\t%s' % round(R_p[file_num][i][0], 3))
            s.write('\t%s' % round(ap_value[file_num][i][0], 3))
            s.write('\t%s' % round(ndcg_10[file_num][i][0], 3))
            s.write('\t%s\n' % round(ndcg_20[file_num][i][0], 3))

            mean_list[0].append(p_10[file_num][i][0])
            mean_list[1].append(r_50[file_num][i][0])
            mean_list[2].append(R_p[file_num][i][0])
            mean_list[3].append(ap_value[file_num][i][0])
            mean_list[4].append(ndcg_10[file_num][i][0])
            mean_list[5].append(ndcg_20[file_num][i][0])

    all_score.write('\nS6\t')

    s.write('mean\t')
    for i in range(len(mean_list)):
        s.write('%s\t' % round(numpy.mean(mean_list[i]), 3))
        all_score.write('%s\t' % round(numpy.mean(mean_list[i]), 3))

    s.close()

    all_score.close()