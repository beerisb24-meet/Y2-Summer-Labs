
def create_youtube_video(title, description):
	video={"title":title, "description":description, "likes":0, "dislikes":0, "comments":{}}
	return(video)

def like():
	if "likes" in video:
		video["likes"]=video["likes"]+1
	return(video)

def dislike():
	if "dislikes" in video:
		video["dislikes"]=video["dislikes"]+1
	return(video)

def add_comment(username, comment_text):
	video["comments"].update({username:comment_text})
	return(video)

def new_video():
	create_youtube_video("title","description")
	for i in range(456):
		like()
	add_comment("Be'eri", "hello")

