from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
    1 : {"Title" : "Atomic habits", "Content": "Self help book with awesome habit tricks"},
    2 : {"Title" : "Psychology of Money", "Content": "Finance Book"},
    3 : {"Title" : "Deep Work", "Content": "Focus and productivity in a distracted world"},
    4 : {"Title" : "Rich Dad Poor Dad", "Content": "Mindset lessons about money and investing"},
    5 : {"Title" : "Think Like a Monk", "Content": "Mental clarity, purpose, and discipline"},
    6 : {"Title" : "The Alchemist", "Content": "A journey about dreams and destiny"},
    7 : {"Title" : "Ikigai", "Content": "Finding purpose and balance in life"},
    8 : {"Title" : "The Power of Now", "Content": "Living in the present moment"},
    9 : {"Title" : "Can't Hurt Me", "Content": "Mental toughness and self-discipline"},
    10: {"Title" : "Zero to One", "Content": "Startup thinking and innovation"}
}

#GET method with limit query parameter
@app.get("/posts")
def get_all_posts(limit : int):
    return list(text_posts.values())[:limit]

#GET method with path parameter and HTTPException.
@app.get("/posts/{id}")
def get_post(id : int):
    if id not in text_posts:
        raise HTTPException(status_code = 404,detail= "Post not found")
    return text_posts.get(id)