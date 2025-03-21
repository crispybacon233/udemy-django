from django.shortcuts import render, HttpResponse

users = {
    1: {
        "id": 1,
        "name": "Alice Johnson",
        "education": "B.Sc. in Computer Science",
        "description": "Tech enthusiast who loves building apps.",
        "likes": ["coding", "hiking", "coffee"],
        "dislikes": ["bugs", "cold weather", "spam emails"]
    },
    2: {
        "id": 2,
        "name": "Brian Smith",
        "education": "M.A. in History",
        "description": "History buff who enjoys storytelling and museums.",
        "likes": ["books", "podcasts", "traveling"],
        "dislikes": ["loud noises", "long meetings", "procrastination"]
    },
    3: {
        "id": 3,
        "name": "Carla Rodriguez",
        "education": "B.A. in Graphic Design",
        "description": "Creative designer passionate about color and detail.",
        "likes": ["illustration", "fashion", "sushi"],
        "dislikes": ["messy workspaces", "deadlines", "monotony"]
    },
    4: {
        "id": 4,
        "name": "David Kim",
        "education": "Ph.D. in Physics",
        "description": "Researcher exploring quantum computing.",
        "likes": ["science fiction", "chess", "cooking"],
        "dislikes": ["traffic jams", "interruptions", "small talk"]
    },
    5: {
        "id": 5,
        "name": "Eva Patel",
        "education": "MBA in Marketing",
        "description": "Marketing strategist who loves connecting ideas.",
        "likes": ["networking", "yoga", "photography"],
        "dislikes": ["overthinking", "fast food", "bad WiFi"]
    },
    6: {
        "id": 6,
        "name": "Felix Brown",
        "education": "B.Sc. in Mechanical Engineering",
        "description": "Engineer who enjoys problem-solving and robotics.",
        "likes": ["3D printing", "cycling", "coffee"],
        "dislikes": ["humidity", "clutter", "excessive noise"]
    },
    7: {
        "id": 7,
        "name": "Grace Lee",
        "education": "B.A. in Literature",
        "description": "Writer and poet with a love for words and rhythm.",
        "likes": ["poetry", "nature walks", "tea"],
        "dislikes": ["rude people", "lateness", "pollution"]
    },
    8: {
        "id": 8,
        "name": "Henry Gonzalez",
        "education": "B.Sc. in Environmental Science",
        "description": "Environmentalist committed to sustainable living.",
        "likes": ["gardening", "documentaries", "clean energy"],
        "dislikes": ["wastefulness", "plastic pollution", "crowded places"]
    },
    9: {
        "id": 9,
        "name": "Isabella Moore",
        "education": "M.F.A. in Fine Arts",
        "description": "Painter with a passion for abstract art.",
        "likes": ["art galleries", "travel", "live music"],
        "dislikes": ["grey skies", "negativity", "routine"]
    },
    10: {
        "id": 10,
        "name": "Jack Wilson",
        "education": "B.Sc. in Information Technology",
        "description": "Tech geek who loves gaming and gadgets.",
        "likes": ["video games", "coding challenges", "pizza"],
        "dislikes": ["slow internet", "bugs in code", "math homework"]
    }
}




# Create your views here.
def homepage(request):
    return render(request, 'projects/homepage.html')


def projects(request):
    return render(request, 'projects/projects.html')


def project(request, slug):
    for user in users.values():
        if user['id'] == slug: break
    return render(request, 'projects/project.html', {'user': user})