from django.shortcuts import render
from dataclasses import dataclass
from typing import Dict,List

@dataclass
class Team:
    name: str
    desc: str
    members: List[str]

teams: Dict[str, Team] = {
    "management":Team(
        "Management Team",
        "As the Management team we are required to manage all of the chores for each day and who does them. This includes cleaning the kitchen, taking out the trash, sweeping the main lobby and the back hallway/classrooms, wiping all the tables which includes the kitchen tables.",
        ["Chris Skeen", "Aiden Swendsen", "Kilan Miller", "Tanner Jones"]
    ),
    "procurement":Team(
        "Procurement Team",
        "The procurement team's job is to keep the students fed while managing our weekly budget.",
        ["Jacob Allen", "Aaron Tapley", "Markel Gladney", "Arthur Fielder"]
    ),
    "documentation":Team(
        "Documentation Team",
        "Documentation team is responsible for taking photos of guest speakers, community events, unit projects, and managing the year book. Afterwords, we decide which social media to post them on depending on the event pictured.",
        ["Jason Woodruff", "Patrick Gonzalez"]
    ),
    "community":Team(
        "Community Team",
        "Our job is to plan events that bring people together, build lasting relationships, and promote engagement.",
        ["Ariannna Kennedy", "Peyton Schmidt"]
    ),
}

def team(request, name:str=None):
    if name:
        team = teams.get(name)
        return render(request, "team.html", {'team':team})
    
    
    return render(request, "team.html", {'teams': teams.keys()})