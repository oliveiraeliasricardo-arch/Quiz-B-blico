# -*- coding: utf-8 -*-
"""
Script to generate the complete 1,000 Bible Quiz questions from Genesis to Revelation.
Outputs:
- /src/data/questionsData.json
- /src/data/questions.ts
"""

import json
import os
import sys

questions = []

def add_q(q, c, w1, w2, w3, diff, book, testament, section, ref, exp):
    idx = len(questions) + 1
    # Rotate correct answer evenly across 0, 1, 2, 3
    target_pos = (idx - 1) % 4
    opts = ["", "", "", ""]
    opts[target_pos] = c
    wrongs = [w1, w2, w3]
    w_idx = 0
    for i in range(4):
        if i != target_pos:
            opts[i] = wrongs[w_idx]
            w_idx += 1
            
    questions.append({
        "id": idx,
        "question": q,
        "options": opts,
        "correctIndex": target_pos,
        "difficulty": diff,
        "book": book,
        "testament": testament,
        "section": section,
        "reference": ref,
        "explanation": exp
    })

print("Starting generation of 1,000 Biblical Questions...")
