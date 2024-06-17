from openai import OpenAI
from file_list_topics import list_topics
with open('topic_list.txt', 'r') as file: topics = file.read()
client = OpenAI(api_key="sk-proj-UIx0DjExZFZ3K8zNgOZmT3BlbkFJj0cGIb1imfb4V3840rQY")
thumbnails = ["https://instagram.fymq2-1.fna.fbcdn.net/v/t51.29350-15/447812387_835561961812626_7109181616597521791_n.jpg?stp=dst-jpg_e15&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi43MjB4MTI4MC5zZHIuZjI5MzUwIn0&_nc_ht=instagram.fymq2-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=sC_BLUYAI04Q7kNvgGzGmZK&edm=APb0JzIBAAAA&ccb=7-5&ig_cache_key=MzM4Mzg5NjkyNDU0ODM1MDUwOA%3D%3D.2-ccb7-5&oh=00_AYBx28ZmMlyzc2yLx8lNLM0dGpjH6AEoqGzqVmIxPXAElg&oe=66763EA8&_nc_sid=cf751b","https://instagram.fymq2-1.fna.fbcdn.net/v/t51.29350-15/446100134_827185172728333_6074243709158091986_n.jpg?stp=dst-jpg_e15&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi43MjB4MTI4MC5zZHIuZjI5MzUwIn0&_nc_ht=instagram.fymq2-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=_WiIWMopUGwQ7kNvgF309E8&edm=APb0JzIBAAAA&ccb=7-5&ig_cache_key=MzM3NTg1MTI4OTE5ODYzOTgzOQ%3D%3D.2-ccb7-5&oh=00_AYCuGEeWFqmEnfsLviTjr2ZV6KmwyNlU9kvk6KffFT-dBw&oe=667657FD&_nc_sid=cf751b"]
posts = []
errors = []
n=0

while n < len(thumbnails) :
  completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "system",
        "content": [{"type": "text",
                    "text": 
                    "You are a precise image analyst. YOU ABSOLUTELY MUST PICK 3  OF THE MOST RELEVANT TOPICS FROM THE FOLLOWING LIST: "+(topics)+" . DO NOT SAY ANYTHING IF ITS NOT A TOPIC FROM THIS LIST. IF YOU DONT KNOW EXACTLY, TAKE A GUESS, IT DOESNT HAVE TO BE PERFECT. IF THE PICTURE HAS A CAPTION, IT POSSIBLY INCLUDES THE 'COMEDY' TOPIC."}],
      },
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "WHAT IS IN THE IMAGE? DESCRIBE IT USING 3 TOPICS FROM THE AFORMENTIONED LIST, IN THIS FORMAT: topic1, topic2, topic3"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": (thumbnails[n]) # will need to replace with current screenshot (n)
              }

              # simply push another image (our screenshot), prompt will still work

            }
          ]
        }
      ]
  )
  cur_post = completion.choices[0].message.content.split(", ")
  for index, value in enumerate(cur_post):
    if value not in list_topics:
        errors.append(f"Invalid topic at entry {n}, {index}, contained {value} from {cur_post}")

  posts.append(completion.choices[0].message.content) 
  n+=1

print(posts)
print(errors)  

# run this code concurrently with the other code that scrolls reels? 
# we could use this topic classifier for our agent to choose what to watch

# i am going to have to implement selenium to download the thumbnails from the reels
# then i'll need to get the downloaded tn into the gpt4-o request, maybe by link
  # if I need the link, i'll likely upload to aws s3 which would take a bit of effort and $0.00Xs

# i'll then need to figure out how to get a screenshot t+3 seconds into the reel
  # same process to upload/input file into gpt request, with the hope of more accuracy

# one issue that could come up is the runtime, if i want to make decisions with it
# ie: should it continue watching the video or not? (if these are the topic it seeks)
# given that the code may take 5s to execute, it could skew our watch times. 