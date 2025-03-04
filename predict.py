from transformers import AutoModelForSequenceClassification, AutoTokenizer

# directory path
model_dir = "checkpoint-1988"

# モデルとtokenizerを読み込み
model = AutoModelForSequenceClassification.from_pretrained(model_dir)
tokenizer = AutoTokenizer.from_pretrained(model_dir)

while True:
    # get input
    text = input("text(q to quit): ")
    if text == "q":
        break

    # tokenize
    inputs = tokenizer(text, return_tensors="pt")

    # Prediction
    outputs = model(**inputs)

    # ログを確認（分類タスクならargmaxを取る）
    logits = outputs.logits
    pred_id = logits.argmax(dim=-1).item()

    # result
    if pred_id == 0:
        print("\nThe given English is likely written by non-native\n")
    elif pred_id == 1:
        print("\nThe given English is likely written by native\n")
    else:
        print("\nFailed to predict\n")
