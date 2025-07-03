# ========================================
# Author: Soohyun Lee
# Date: 2025-06-02
# ========================================


import os
from utils.parser import extract_korean_from_json, get_all_json_paths
from utils.gpt_client import get_chat_completion

# 프롬프트 불러오기
with open("/mnt/c/Users/Flitto/Documents/AC/멀티턴대화/QC/prompt/system.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

with open("/mnt/c/Users/Flitto/Documents/AC/멀티턴대화/QC/prompt/user.txt", "r", encoding="utf-8") as f:
    user_prompt_template = f.read()

# JSON 파일 순회
json_dir = "/mnt/c/Users/Flitto/Documents/AC/멀티턴대화/QC/dataset/"
output_dir = "/mnt/c/Users/Flitto/Documents/AC/멀티턴대화/QC/results/"


for path in get_all_json_paths(json_dir):
    dialogue = extract_korean_from_json(path)
    user_prompt = user_prompt_template.replace("{dialogue}", dialogue)

    result = get_chat_completion(system_prompt, user_prompt)
    
    print(f'파일명: {os.path.basename(path)}')
    print(f'결과: {'\n'+result}')

    fname = os.path.basename(path).replace(".json", "_result.txt")
    output_path = os.path.join(output_dir, fname)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("[대화 원문]\n")
        f.write(dialogue)
        f.write("\n\n[GPT 분석 결과]\n")
        f.write(result)

    print(f"처리 완료: {fname}")
