import requests


website="https://jsonplaceholder.typicode.com/posts/2"
print(requests.get(website).json())
response=requests.put(website,data={
    "id":2,
    "userId":12,
    "title":"My new post ,my home work",
    "body":"body for my home work post ",
    #"photo" :{"1.jpg","2.jpg"}
})

print(response.json())



