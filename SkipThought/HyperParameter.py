#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : HyperParameter.py
# @Author: harry
# @Date  : 18-8-4 下午2:24
# @Desc  : HyperParameter wrapper class


class HyperParameter(object):
    def __init__(self):
        # 超参数
        self.rnn_size = 256
        self.num_layers = 2
        self.embedding_size = 256
        self.batch_size = 32
        self.learning_rate = 0.001
        self.epochs = 200
        self.teacher_forcing = False
        self.teacher_forcing_probability = 0.5

        # Data filepath
        self.data_txt = 'data/data.txt'
        self.dictionary_txt = 'data/dictionary.txt'

        # Saver config
        self.model_dir = 'model/'
        self.steps_per_checkpoint = 20
        self.max_to_keep = 3
        self.max_save_loss = 6.0

        # Other
        self.print_loss_steps = 20
        self.beam_size = 3
