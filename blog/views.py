from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Tomasz",
        "date": date(2021,7,21),
        "title": "Mountain Hiking",
        "excerpt": "Beautiful vies in the mountains",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Possimus, eum magnam! Ipsum voluptate ad libero, quam tempora rem? 
            Error, explicabo aliquam deserunt quis nihil iusto reiciendis nemo 
            ratione suscipit corrupti.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Possimus, eum magnam! Ipsum voluptate ad libero, quam tempora rem? 
            Error, explicabo aliquam deserunt quis nihil iusto reiciendis nemo 
            ratione suscipit corrupti.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Possimus, eum magnam! Ipsum voluptate ad libero, quam tempora rem? 
            Error, explicabo aliquam deserunt quis nihil iusto reiciendis nemo 
            ratione suscipit corrupti.
        """
    },
    {
        "slug": "funny",
        "image": "coding.jpg",
        "author": "Tomasz",
        "date": date(2021,7,15),
        "title": "Funny things about coding",
        "excerpt": "Coding is great",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Possimus, eum magnam! Ipsum voluptate ad libero, quam tempora rem? 
            Error, explicabo aliquam deserunt quis nihil iusto reiciendis nemo 
            ratione suscipit corrupti.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Possimus, eum magnam! Ipsum voluptate ad libero, quam tempora rem? 
            Error, explicabo aliquam deserunt quis nihil iusto reiciendis nemo 
            ratione suscipit corrupti.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Possimus, eum magnam! Ipsum voluptate ad libero, quam tempora rem? 
            Error, explicabo aliquam deserunt quis nihil iusto reiciendis nemo 
            ratione suscipit corrupti.
        """
    }
]

def get_date(post):
    return post["date"]

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
