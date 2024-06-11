from openai import OpenAI
with open('topiclist.txt', 'r') as file:
    content = file.read()
client = OpenAI(
    api_key="sk-proj-UIx0DjExZFZ3K8zNgOZmT3BlbkFJj0cGIb1imfb4V3840rQY"
)

url = ["https://scontent.cdninstagram.com/v/t51.29350-15/446106295_973084087661170_7214059202626489128_n.jpg?stp=dst-jpg_e15&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi43MjB4MTI4MC5zZHIuZjI5MzUwIn0&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=qkw7jtL1nDIQ7kNvgF5_HFd&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzM3MzU3MDgxNTI0NDc3MTUwOA%3D%3D.2-ccb7-5&oh=00_AYAZipEzjJ9bDVa3o_Frtdjp1_7tpRuTx3HDjiCb2qS91w&oe=666D269A&_nc_sid=10d13b",
       "https://scontent.cdninstagram.com/v/t51.29350-15/440887055_785620673556846_7600933474260140038_n.jpg?stp=dst-jpg_e15&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDE5MjAuc2RyLmYyOTM1MCJ9&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=Q6fQUsj4dPkQ7kNvgFHdxiu&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzM1NzM1NjcxMTU5NjgwNDYwMQ%3D%3D.2-ccb7-5&oh=00_AYBd2Or3ljuolpWx6ww2a8vA4koyaF2bGCDcdBRnR8ODrw&oe=666D14E9&_nc_sid=10d13b",
       "https://instagram.fymq3-1.fna.fbcdn.net/v/t51.29350-15/441173093_980635546299971_1102620968990156418_n.jpg?stp=dst-jpg_e15&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi43MjB4MTI4MC5zZHIuZjI5MzUwIn0&_nc_ht=instagram.fymq3-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=F4bDaTJV5L8Q7kNvgFdpi51&edm=AIBcDR0BAAAA&ccb=7-5&ig_cache_key=MzM1NzEyNjA0NjY4Mjc4Nzg1MA%3D%3D.2-ccb7-5&oh=00_AYCJPoIquv2FauY7wa-bWYK0CT0R5boGYiswKFzhE3JdRA&oe=666B2F57&_nc_sid=cf751b",
       "https://instagram.fymq3-1.fna.fbcdn.net/v/t51.29350-15/438804652_388244247443425_8754313467579439451_n.jpg?stp=dst-jpg_e15&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDE5MjAuc2RyLmYyOTM1MCJ9&_nc_ht=instagram.fymq3-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=r-0PKWRfZBMQ7kNvgHFvYYI&edm=AIBcDR0BAAAA&ccb=7-5&ig_cache_key=MzM0NzUzMDkyNTQ2NTgyMjIyMg%3D%3D.2-ccb7-5&oh=00_AYCW_y5mt6FGz1Py5Ovi3JyBnmLqBPy_B91581jQxcxOQQ&oe=666B1F7F&_nc_sid=cf751b",
       "https://instagram.fymq3-1.fna.fbcdn.net/v/t51.29350-15/433223423_6991436784317763_6987684144961819357_n.jpg?stp=dst-jpg_e15&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi43MjB4MTI3OC5zZHIuZjI5MzUwIn0&_nc_ht=instagram.fymq3-1.fna.fbcdn.net&_nc_cat=103&_nc_ohc=1lDqvIioEz8Q7kNvgFmZoqu&edm=AIBcDR0BAAAA&ccb=7-5&ig_cache_key=MzMyNDIyMjg2NDg4NTY2OTkzMDM0NzMwOTM1MDk5MjQyNg%3D%3D.2-ccb7-5&oh=00_AYBjmnpiJoOjdNTGOeXXnsBwHj5-eGodVv8itkcmd1ssJQ&oe=666B3342&_nc_sid=cf751b",
       "https://instagram.fymq3-1.fna.fbcdn.net/v/t51.29350-15/443527870_983292006360084_1763217397978210854_n.jpg?stp=dst-jpg_e15&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDE5MjAuc2RyLmYyOTM1MCJ9&_nc_ht=instagram.fymq3-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=tyD-RTD7ow4Q7kNvgGxzzdh&edm=AIBcDR0BAAAA&ccb=7-5&ig_cache_key=MzM2OTIyMTMzNTg0MzY4OTI4Nw%3D%3D.2-ccb7-5&oh=00_AYC-r3CKjrd8EmUlluO66SBIKQN4M-HAd2sbvvDivI79qA&oe=666B2A77&_nc_sid=cf751b",
       "https://instagram.fymq3-1.fna.fbcdn.net/v/t51.29350-15/447914481_822298523142539_6907059480475800554_n.jpg?stp=dst-jpg_e15&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4zMjB4NTY4LnNkci5mMjkzNTAifQ&_nc_ht=instagram.fymq3-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=sJf4bWlaX9UQ7kNvgE16kqt&edm=AIBcDR0BAAAA&ccb=7-5&ig_cache_key=MzM4NDQzMzI2NTQ5Mzk2MDY1Mg%3D%3D.2-ccb7-5&oh=00_AYBXvpvWNBp9kuh1bnLSscnvHxE96Mvk7Q8PIptATvjL5A&oe=666B18AE&_nc_sid=cf751b",
       "https://instagram.fymq3-1.fna.fbcdn.net/v/t51.29350-15/446545350_431146559638245_7286362065767784912_n.jpg?stp=dst-jpg_e15&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDE5MjAuc2RyLmYyOTM1MCJ9&_nc_ht=instagram.fymq3-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=5kmuCZuDGkQQ7kNvgGwC3-3&edm=AIBcDR0BAAAA&ccb=7-5&ig_cache_key=MzM3ODcwODMwNzgxOTIzOTA1Mw%3D%3D.2-ccb7-5&oh=00_AYC8bAlCUkcNCVCSSLqmIJaKhSNKCGLY8EGDuHmWR-g_Aw&oe=666B41BC&_nc_sid=cf751b"
       ]
n=0
while n < 8 :
  completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "system",
        "content": [{"type": "text",
                    "text": "You are a precise image analyst.  YOU MUST PICK 3 THINGS FROM THIS LIST OF TOPICS TO DESCRIBE THE IMAGE "+(content)+" AND ONLY FROM THIS LIST. IT WOULD REALLY HELP ME IN MY JOB TO AVOID GETTING FIRED. DO NOT RESPOND WITH ANY TEXT EXCEPT THESE 3 TOPICS, IN THIS FORMAT: topic1, topic2, topic3."}],
      },
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "What is in the image?"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": (url[n])
              }

              # simply push another image (our screenshot), prompt will still work

            }
          ]
        }
      ],
  )
  print(completion.choices[0].message)
  n+=1

  # make a 'check' function that verifies that the 3 categories
  # are in the list of topics and that they are unique (avoid hallucinations)

  # we can instead push to an array in the loop 
  # and print the array outside of the loop after
  # we can also stringify the completion choices to remove the useless stuff


  # print (the whole array that contains all of the clean completions)

  # run this code concurrently with the other code that scrolls reels? 
  # or run it after the scrolling is done? (current status quo)

  # we could use this code (the AI classifier) to itself choose what to watch or not

