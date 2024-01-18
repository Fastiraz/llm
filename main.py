import time
from rag.pipeline import build_rag_pipeline
import json

# ANSI color codes
KNRM = "\x1B[0m"
KRED = "\x1B[31m"
KGRN = "\x1B[32m"
KYEL = "\x1B[33m"
KBLU = "\x1B[34m"
KMAG = "\x1B[35m"
KCYN = "\x1B[36m"
KWHT = "\x1B[37m"
LRED = "\x1B[91m"

def get_rag_response(query, chain):
  response = chain({'query': query})
  res = response['result']
  start_index = res.find('{')
  end_index = res.rfind('}')
  if start_index != -1 and end_index != -1 and end_index > start_index:
    json_fragment = res[start_index:end_index + 1]
    try:
      json_data = json.loads(json_fragment)
      return json_data
    except json.JSONDecodeError as e:
      print(f"Error parsing JSON: {e}")
  else:
    print("No JSON object found in the string.")
  return res

if __name__ == "__main__":
  while(1):
    prompt = input(f'\n{KMAG}Prompt{KNRM} \033[36m➜\033[0m ')
    start = time.time()
    qa_chain = build_rag_pipeline()
    print('Retrieving answer...')
    answer = get_rag_response(prompt, qa_chain)
    end = time.time()
    print(f'\n{LRED}UsercubeAI:{KNRM}')
    print(answer)
    print('_' * 50)
    print(f"Time to retrieve answer: {end - start}")