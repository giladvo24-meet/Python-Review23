def create_youtube_video(title, description):
	youtube_video = {title: "", description: "", "likes": 0, "dislikes": 0, "comments": {}, "hashtags": []}
	hashtag1 = input("Enter a hashtag: ")
	hashtag2 = input("Enter another hashtag: ")
	youtube_video["hashtags"].append(hashtag1)
	youtube_video["hashtags"].append(hashtag2)
	return youtube_video

def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] = youtube_video["likes"]+1
	return youtube_video

def dislike(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"] = youtube_video["dislikes"]+1

def add_comment(youtube_video, username, comment_text):
	youtube_video["comments"]["username"] = comment_text
	return youtube_video

uno = create_youtube_video("ahir", "bahir")
for i in range(495):
	like(uno)
print(uno)
#Bonus
def similarity_to_video(vid1, vid2):
	original_list1 = vid1["hashtags"]
	original_list2 = vid2["hashtags"]

	common_elements = set(original_list1).intersection(set(original_list2))
	num_common_elements = len(common_elements)
 
	total_elements = set(original_list1).union(set(original_list2))
	num_total_elements = len(total_elements)

	percentage_similarity = (num_common_elements / num_total_elements) * 100
 
	print("Percentage similarity among lists is : {:.2f}".format(percentage_similarity))

dos = create_youtube_video("siraj", "bahir")

print(similarity_to_video(uno, dos))