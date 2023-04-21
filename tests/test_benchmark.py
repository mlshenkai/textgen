# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import sys
import pytest
import os
import pandas as pd

sys.path.append('..')
from textgen import LlamaModel, ChatGlmModel

pwd_path = os.path.abspath(os.path.dirname(__file__))


def llama_generate_prompt(instruction):
    return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:{instruction}\n\n### Response:"""


def chatglm_generate_prompt(instruction):
    return f"""{instruction}\n答："""


sentences = open(os.path.join(pwd_path, '../examples/data/llm_benchmark_test.txt')).readlines()


def test_llama_7b_lora():
    m = LlamaModel('llama', "decapoda-research/llama-7b-hf", lora_name='ziqingyang/chinese-alpaca-lora-7b',
                   args={'use_lora': True}, )

    predict_sentences = [llama_generate_prompt(s) for s in sentences]
    res = m.predict(predict_sentences)
    res_dict = {}
    for s, i in zip(sentences, res):
        res_dict[s] = i
        print('input:', s, ' output:', i)
        print()

    df = pd.DataFrame.from_dict(res_dict, columns=['input', 'output'])
    df.to_json(os.path.join(pwd_path, 'llama_7b_lora_llm_benchmark_test_result.json'), force_ascii=False,
               orient='records', lines=True)


def test_llama_13b_lora():
    m = LlamaModel('llama', "decapoda-research/llama-13b-hf", lora_name='ziqingyang/chinese-alpaca-lora-13b',
                   args={'use_lora': True}, )
    predict_sentences = [llama_generate_prompt(s) for s in sentences]
    res = m.predict(predict_sentences)
    res_dict = {}
    for s, i in zip(sentences, res):
        res_dict[s] = i
        print('input:', s, ' output:', i)
        print()

    df = pd.DataFrame.from_dict(res_dict, columns=['input', 'output'])
    df.to_json(os.path.join(pwd_path, 'llama_13b_lora_llm_benchmark_test_result.json'), force_ascii=False,
               orient='records', lines=True)


def test_chatglm_6b():
    m = ChatGlmModel('chatglm', "THUDM/chatglm-6b", lora_name=None, args={'use_lora': False}, )
    predict_sentences = [chatglm_generate_prompt(s) for s in sentences]
    res = m.predict(predict_sentences)
    res_dict = {}
    for s, i in zip(sentences, res):
        res_dict[s] = i
        print('input:', s, ' output:', i)
        print()

    df = pd.DataFrame.from_dict(res_dict, columns=['input', 'output'])
    df.to_json(os.path.join(pwd_path, 'chatglm_6b_llm_benchmark_test_result.json'), force_ascii=False,
               orient='records', lines=True)


def test_chatglm_6b_lora():
    m = ChatGlmModel('chatglm', "THUDM/chatglm-6b", lora_name='shibing624/chatglm-6b-belle-zh-lora',
                     args={'use_lora': True}, )
    predict_sentences = [chatglm_generate_prompt(s) for s in sentences]
    res = m.predict(predict_sentences)
    res_dict = {}
    for s, i in zip(sentences, res):
        res_dict[s] = i
        print('input:', s, ' output:', i)
        print()

    df = pd.DataFrame.from_dict(res_dict, columns=['input', 'output'])
    df.to_json(os.path.join(pwd_path, 'chatglm_6b_lora_llm_benchmark_test_result.json'), force_ascii=False,
               orient='records', lines=True)
