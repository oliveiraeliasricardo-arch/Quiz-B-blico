# -*- coding: utf-8 -*-
import json
import random
import os
import scripts.gen_pentateuch as p
import scripts.gen_historical as h
import scripts.gen_poetic as po
import scripts.gen_prophets as pr
import scripts.gen_gospels as g
import scripts.gen_epistles as e
import scripts.gen_revelation as r

def build_questions():
    # Deterministic seed for reproducible builds
    random.seed(42)

    p_q = p.get_pentateuch_questions()     # 160
    h_q = h.get_historical_questions()     # 160
    po_q = po.get_poetic_questions()       # 130
    pr_q = pr.get_prophets_questions()     # 150
    g_q = g.get_gospels_questions()        # 200
    e_q = e.get_epistles_questions()       # 140
    r_q = r.get_revelation_questions()     # 60

    raw_list = p_q + h_q + po_q + pr_q + g_q + e_q + r_q
    print(f"Total raw questions: {len(raw_list)}")
    assert len(raw_list) == 1000, f"Expected 1000, got {len(raw_list)}"

    # Balance difficulty so that:
    # Fácil has ~360, Médio has ~360, Difícil has ~280
    # We calibrate based on original hint or index within each section
    final_questions = []

    # Map rotating correct index: 0, 1, 2, 3
    pattern = [0, 1, 2, 3, 2, 1, 0, 3, 1, 2]

    for idx, item in enumerate(raw_list):
        q_id = idx + 1
        
        # Difficulty calibration
        orig_diff = item.get("diff", "facil")
        if orig_diff == "dificil":
            assigned_diff = "dificil"
        elif orig_diff == "medio":
            # 50% keep medio, 50% shift to dificil if question text or ref has high specificity
            if idx % 3 == 0:
                assigned_diff = "dificil"
            else:
                assigned_diff = "medio"
        else: # orig_diff == "facil"
            # Distribute across facil (50%), medio (30%), dificil (20%)
            mod = (idx * 7 + 3) % 10
            if mod in [0, 1, 2, 3]:
                assigned_diff = "facil"
            elif mod in [4, 5, 6]:
                assigned_diff = "medio"
            else:
                assigned_diff = "dificil"

        # Determine correct position
        target_pos = pattern[idx % len(pattern)]

        # Collect choices
        correct_val = item["c"].strip()
        wrongs = [item["w1"].strip(), item["w2"].strip(), item["w3"].strip()]
        # Shuffle wrong answers deterministically
        random.shuffle(wrongs)

        options = [None, None, None, None]
        options[target_pos] = correct_val
        w_idx = 0
        for i in range(4):
            if options[i] is None:
                options[i] = wrongs[w_idx]
                w_idx += 1

        # Check options uniqueness
        if len(set(options)) != 4:
            print(f"Warning: Non-unique options in Q#{q_id}: {options}")

        final_questions.append({
            "id": q_id,
            "question": item["q"].strip(),
            "options": options,
            "correctIndex": target_pos,
            "difficulty": assigned_diff,
            "book": item["book"].strip(),
            "testament": item["testament"].strip(),
            "section": item["section"].strip(),
            "reference": item["ref"].strip(),
            "explanation": item["exp"].strip()
        })

    os.makedirs("src/data", exist_ok=True)
    out_file = "src/data/questionsData.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(final_questions, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(final_questions)} questions to {out_file}")

    # Print summary
    from collections import Counter
    diff_counts = Counter(q["difficulty"] for q in final_questions)
    sec_counts = Counter(q["section"] for q in final_questions)
    pos_counts = Counter(q["correctIndex"] for q in final_questions)

    print("Difficulty distribution:", diff_counts)
    print("Section distribution:", sec_counts)
    print("Correct index distribution:", pos_counts)

if __name__ == "__main__":
    build_questions()
