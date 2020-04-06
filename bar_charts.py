import matplotlib.pylab as plt
import numpy as np

col_count = 3
bar_width = .15

korea_scores = (554, 536, 538)
canada_score = (518, 523, 525)
china_score = (613, 570, 580)
france_score = (495, 505, 499)
poland_score = (518, 518, 526)

index = np.arange(col_count)

k1 = plt.bar(index, korea_scores, bar_width, alpha=.4, label='Korea')
c1 = plt.bar(index + 0.15, canada_score, bar_width, alpha=.4, label='Canada')
ch1 = plt.bar(index + 0.3, china_score, bar_width, alpha=.4, label='China')
f1 = plt.bar(index + 0.45, france_score, bar_width, alpha=.4, label='France')
p1 = plt.bar(index + 0.6, canada_score, bar_width, alpha=.4, label='Poland')


def create_labels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width() / 2., height * 1.05, '%d' % int(height), ha='center', va='bottom')


create_labels(k1)
create_labels(c1)
create_labels(ch1)
create_labels(f1)
create_labels(p1)

plt.ylabel('Mean score in PISA 2012')
plt.xlabel('Subjects')
plt.title('Test Scores by Country')

plt.xlim(- .2, 2.8)
plt.ylim(0, 680)
plt.xticks(index + .6 / 2, ('Mathematics', 'Reading', 'Science'))
plt.legend(frameon=False, bbox_to_anchor=(1, 1), loc=2)
plt.grid(True)

plt.show()
