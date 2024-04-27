class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.friends = set()

    def create_post(self, content):
        post_ = Post(content, self.username)
        self.posts.append(post_)
        return post_

    def comment_on_post(self, post, content):
            comment = Comment(content, self.username)
            post.add_comment(comment)

    def like_post(self, post):
            post.add_like(self.username)


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []
        self.likes = set()

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self, username):
        self.likes.add(username)


class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author


# Usage
user1 = User("User1")
user2 = User("User2")

user1.friends.add(user2)
user2.friends.add(user1)

post1 = user1.create_post("First post by user1")
user2.comment_on_post(post1, "Nice post")
user1.like_post(post1)

post2 = user1.create_post("Second post by user1")
user2.like_post(post2)

print("User1's posts:")
for post in user1.posts:
    print(f"Content: {post.content}, Likes: {len(post.likes)}, Comments: {len(post.comments)}")
