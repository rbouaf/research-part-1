from openai import OpenAI
from data.topic_list.topic_list import list_topics
from data.aws.credentials import openai_api_key
with open('../data/topic_list/topic_list.txt', 'r') as file: topics = file.read()
client = OpenAI(openai_api_key)
thumbnails = ["https://scontent.cdninstagram.com/v/t51.29350-15/448057032_1066199521605936_1057061306196734606_n.jpg?stp=dst-jpg_e15&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi43MjB4MTI4MS5zZHIuZjI5MzUwIn0&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=Zc4vxvTyKWMQ7kNvgHFvsLs&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzM4NTQ4Mzg4MjI1NzA0Njg1OA%3D%3D.2-ccb7-5&oh=00_AYB6f_2Xh5YBUzYvUMU6e4H5zZe3hXAkGgpkOskeqryBOA&oe=6680F169&_nc_sid=10d13b", "https://scontent.cdninstagram.com/v/t51.29350-15/444885009_1163255358252264_668982721321306254_n.jpg?stp=dst-jpg_e15&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi40MTZ4NzQwLnNkci5mMjkzNTAifQ&_nc_ht=scontent.cdninstagram.com&_nc_cat=100&_nc_ohc=i1pAX-a27lwQ7kNvgETkuhZ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzM3MTM3OTEzMzg0OTk5NjQ3OQ%3D%3D.2-ccb7-5&oh=00_AYDRZLaZ3k6rMM_yPWcWgHQbuy05D3d4GqeDG5WGuQ0qaA&oe=6680F0FC&_nc_sid=10d13b"]
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

# one issue that could come up is the runtime, if i want to make decisions with it
# ie: should it continue watching the video or not? (if these are the topic it seeks)
# given that the code may take 5s to execute, it could skew our watch times. 