import requests as req

# headers = {
#     "Ocp-Apim-Subscription-Key" : "23bbb74859824f9ba65ddeab73ffb7fa",
#     "Context-Type": "application/json",
#     "Accept" : "application/json"
# }

headers = {
    "Ocp-Apim-Subscription-Key": "b31364ab188641f78ac41a9678a3dd18",
    "Content-Type": "application/json",
    "Accept": "application/json"
}


endpoint = 'sentiment'
body = {
    "documents": [
        {
            "language": "en",
            "id": "1",
            "text": "Great atmosphere. Close to plenty of restaurants, hotels, and transit! Staff are friendly and helpful."
        },
        {
            "language": "en",
            "id": "2",
            "text": "Bad atmosphere. Not close to plenty of restaurants, hotels, and transit! Staff are not friendly and helpful."
        }
    ]
}

response = req.post("https://pythonapiazure.cognitiveservices.azure.com/text/analytics/v3.0/sentiment", headers=headers, json=body)

result = response.json()
print(result)
sentiment = result["documents"]

for i in range(len(sentiment)):
    print("Document {0}: Sentiment: {1} ".format(i + 1, sentiment[i]["sentiment"]))

print("Sentence Level Sentiment\n")
for i in range(len(sentiment)):
    for j in range(len(sentiment[i]["sentences"])):
        print("Document {0}: Sentence {1}: {2} -> Sentiment: {3} ".format(i + 1, j + 1, 
               sentiment[i]["sentences"][j]["text"], sentiment[i]["sentences"][j]["sentiment"]))


response = req.post("https://pythonapiazure.cognitiveservices.azure.com/text/analytics/v3.0/keyPhrases", headers=headers, json=body)
result = response.json()
keyPhrases = result["documents"]
for i in range(len(keyPhrases)):
    document_level_keyphrases = keyPhrases[i]["keyPhrases"]
    print("Document {}: KeyPhrases: {}".format(i+1, document_level_keyphrases))