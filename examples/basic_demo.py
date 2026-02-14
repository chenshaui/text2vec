# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
This basic example loads a pre-trained model from the web and uses it to
generate sentence embeddings for a given list of sentences.
"""

import sys

sys.path.append('..')
from text2vec import SentenceModel

if __name__ == "__main__":
    model = SentenceModel("shibing624/text2vec-base-chinese")
    embs = model.encode(['你好', '世界'])
    print(embs)
    print(embs.shape)


