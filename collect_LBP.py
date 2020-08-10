import pandas as pd
import instaloader

L = instaloader.Instaloader()
hashtag = instaloader.Hashtag.from_name(L.context, "backpain")
posts = hashtag.get_posts()

def parse_post(post):
    caption = post.caption
    owner = post.owner_profile.username
    owner_bio = post.owner_profile.biography
    date = post.date
    post_type = post.typename
    is_video = post.is_video
    video_views = post.video_view_count
    likes = post.likes
    num_comments = post.comments
    
    return [post_type, 
            owner, 
            owner_bio, 
            date, 
            caption, 
            likes, 
            num_comments, 
            is_video, 
            video_views]

# The following code block loops through a sample of 1000 posts with the hashtag "#backpain" on Instagram, parses the post using the parse_post() function, and appends the returned list object to a list of lists.
list_posts = []
i = 0
for post in posts:
    if i < 1000:
        list_posts.append(parse_post(post))
        i += 1
        print(i)
    else:
        break

df = pd.DataFrame(list_posts, columns=["post_type", "owner", "owner_bio", "date", "caption", "num_likes", "num_comments", "is_video", "video_views"])
df.to_csv('ig_LBP.csv', index=True)