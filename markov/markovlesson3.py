import markovify
import pandas as pd
import re

def df_for_text(data):
    text=""
    for w in data:
        w = re.sub(r"[【】≪≫「」『』＠（）～＿・]", "", w)
        w = re.sub(r"[()\[\]@_~\"\'|]", "", w)
        w = re.sub(r"\u3000", "", w)
        w = re.sub(r" ", "", w)
        w = re.sub(r"。", "。\n", w)
        w += " "
        text += w
    #print(text)
    return text

def markoving(text):
    with open("model/text_model.json") as f:
        current_model=markovify.NewlineText.from_json(f.read())

    text_model = markovify.NewlineText(text,state_size=3)

    new_model=markovify.combine([current_model,text_model])

    print(re.sub(" ","",new_model.make_short_sentence(100,tries=100)))
    with open("model/text_model.json","w") as f:
        f.write(new_model.to_json())

while True:
    f_name=input("ファイル名>")
    if f_name== "end":
        break
    df =pd.read_csv(f_name)
    text=df_for_text(df.iloc[:,3])
    markoving(text)

