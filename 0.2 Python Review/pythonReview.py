title=input("what is the video's title?")
description=input("what is the video's description?")
video={"title":title, "description":description, "likes":0, "dislikes":0, "comments":{}}
def create_youtube_video():
	print(video)

def like():
	if "likes" in video:
		video["likes"]=video["likes"]+1
	print(video)

def dislike():
	if "dislikes" in video:
		video["dislikes"]=video["dislikes"]+1
	print(video)

def add_comment():
	username=input("what is your name?")
	comment_text=input("what is your comment?")
	video["comments"].update({username:comment_text})
	print(video)

