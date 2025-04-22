import os
import openai
from input.topics.topics import list_topics
from input.keys.openai_key import openai_api_key as key

# with open('data/topic_list/topic_list.txt', 'r') as file: topics = file.read()
os.environ["OPENAI_API_KEY"] = key
client = openai.OpenAI()

def categorize_images(thumbnails):
    descriptions = []
    errors = []
    n = 0
    for thumbnail in thumbnails:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system",
                 "content": [{"type": "text",
                              "text":
                                  "You are a precise image analyst. YOU ABSOLUTELY MUST DEFINE THE IMAGE AS EITHER APOLITICAL, RIGHT LEANING, OR LEFT LEANING. USE ONLY THE WORDS APOLITICAL, RIGHT, OR LEFT. DO NOT SAY ANYTHING OTHER THAN ONE OF THOSE 3 WORDS. IF YOU DONT KNOW EXACTLY, TAKE A GUESS, IT DOESNT HAVE TO BE PERFECT. NO PROBLEM IF THE ACCOUNT IS APOLITICAL, JUST BE TRUTHFUL."}],
                 },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "WHAT IS IN THE IMAGE? DEFINE THE IMAGE AS EITHER APOLITICAL, RIGHT LEANING, OR LEFT LEANING. USE ONLY THE WORDS 'APOLITICAL', 'RIGHT', OR 'LEFT'."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": thumbnail  # use current thumbnail url from the array
                            }
                        }
                    ]
                }
            ]
        )
        descriptions.append(completion.choices[0].message.content)
    return descriptions