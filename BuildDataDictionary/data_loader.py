import os
import nltk
import string
from collections import Counter
import numpy as np
import tensorflow.keras as kr
#读取文件
def read_file(filename):
    '''
    从文件中读取标签和文本内容
    :param filename:数据集的路径
    :return: 数据和标签的list
    '''
    filenames = []#不同模块的路径
    labels = []#标签
    contents = []#内容
    sentences = []
    for dir in os.listdir(filename):
        if os.path.isdir(os.path.join(filename, dir)) and dir != '__pycache__':
            filenames.append(os.path.join(filename, dir))
    for dir in filenames:
        for file in os.listdir(dir):
            with open(os.path.join(dir, file), encoding = 'utf-8') as f:
                text = list(f)
                content = ''
                for line in text:
                    if line[:8] == 'label = ':
                        labels.append(line[8:-1])
                        contents.append(content)
                        content = ''
                    else:
                        content += line
    for content in contents:
        for i in string.punctuation:
            content = content.replace(i,' ')
        wordList = nltk.word_tokenize(content)
        sentences.append(wordList)
    return sentences, labels

#构建词汇表
def build_vocab(datadir, vocab_dir, vocab_size=5000):
    '''
    根据数据集构建词汇表，存储
    :param datadir: 数据集目录
    :param vocab_dir: 词汇表存储路径
    :param vocab_size: 词汇表的大小
    :return:
    '''
    dataset, _ = read_file(datadir)
    all_data = []
    for content in dataset:
        all_data.extend(content)
    counter  = Counter(all_data)
    count_pairs = counter.most_common(vocab_size - 1)
    words, _ = list(zip(*count_pairs))
    # 添加一个 <PAD> 来将所有文本pad为同一长度
    words = ['<PAD>'] + list(words)
    open(vocab_dir, mode='w', encoding='utf-8').write('\n'.join(words)+'\n')

def read_vocab(vocab_dir):
    """读取词汇表"""
    # words = open_file(vocab_dir).read().strip().split('\n')
    with open(vocab_dir, encoding='utf-8') as fp:
        # 如果是py2 则每个值都转化为unicode
        words = [_.strip() for _ in fp.readlines()]
    word_to_id = dict(zip(words, range(len(words))))
    return words, word_to_id

# def read_category():
#     """读取分类目录，固定"""
#     categories = ['警告', '一般错误', '严重错误', '及时处理']
#     cat_to_id = dict(zip(categories, range(len(categories))))
#
#     return categories, cat_to_id
#
# def to_words(content, words):
#     """将id表示的内容转换为文字"""
#     return ''.join(words[x] for x in content)
#
#
# def process_file(filename, word_to_id, cat_to_id, max_length=600):
#     """将文件转换为id表示"""
#     contents, labels = read_file(filename)
#
#     data_id, label_id = [], []
#     for i in range(len(contents)):
#         data_id.append([word_to_id[x] for x in contents[i] if x in word_to_id])
#         label_id.append(cat_to_id[labels[i]])
#
#     # 使用keras提供的pad_sequences来将文本pad为固定长度
#     x_pad = kr.preprocessing.sequence.pad_sequences(data_id, max_length)
#     y_pad = kr.utils.to_categorical(label_id, num_classes=len(cat_to_id))  # 将标签转换为one-hot表示
#
#     return x_pad, y_pad
#
#
# def batch_iter(x, y, batch_size=64):
#     """生成批次数据"""
#     data_len = len(x)
#     num_batch = int((data_len - 1) / batch_size) + 1
#
#     indices = np.random.permutation(np.arange(data_len))
#     x_shuffle = x[indices]
#     y_shuffle = y[indices]
#
#     for i in range(num_batch):
#         start_id = i * batch_size
#         end_id = min((i + 1) * batch_size, data_len)
#         yield x_shuffle[start_id:end_id], y_shuffle[start_id:end_id]


if __name__ == '__main__':
    build_vocab('./', 'all_log.txt')
    read_vocab('vocal.txt')
    #read_category()