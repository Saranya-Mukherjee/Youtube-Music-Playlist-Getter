import os
from googleapiclient.discovery import build

api_key = "PUT YOUR API KEY HERE"

url=input("Enter the playlist URL: ")
st=url+"&"
pl_id=st[st.find("list=")+5:st.find("&")]

yt = build('youtube', 'v3', developerKey=api_key)
request = yt.playlistItems().list(
        part='contentDetails',
        playlistId=pl_id,
        maxResults=50
    )

print("Fetching playlist...")

response = request.execute()
l=response['items']
n=[]
for items in l:
    n.append(items['contentDetails']['videoId'])
l=[]

print("Fetching videos...")

for item in n:
    request = yt.videos().list(
        part='snippet',
        id=item
    )
    response1 = request.execute()
    response1 = response1['items'][0]['snippet']['title']
    l.append(response1)
print(response)
print(l)
print(len(l))

s={}
c=1
for item in l:
   s[item]=str(c)+". " +item
   c+=1
print(s)
x=input("Confirm renaming? (y/n): ")

if x == "n":
    print("Quiting...")
    exit(101)

illegal='\<>*?":|'

print("Renaming...")
des=input("Enter path of files: ")
p=des+"\\"
for item in l:
    src=item+".wav"
    for i in illegal:
        src=src.replace(i,"_")
    src=p+src
    if os.path.exists(src):
        des = s[item] + ".wav"
        for i in illegal:
            if i!="?":
                des=des.replace(i, "_")
            else:
                des=des.replace(i, "")
        des=p+des
        os.rename(src,des)

print("DONE!")