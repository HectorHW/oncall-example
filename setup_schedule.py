import requests
import datetime
from itertools import cycle

DOMAIN = "http://localhost:8080"

API = f"{DOMAIN}/api/v0"

#users

requests.post(f"{API}/users", json={
    "name": "vsredkin"
})
requests.put(f"{API}/users/vsredkin", json={
    "contacts": {
        "call": "+7 999-123-4567",
        "email": "vsredkin@example.com",
        "slack": "vsredkin",
        "sms": "+7 999-123-4567"
    },
    "full_name": "Vladimir Redkin",
    "time_zone": "EU/Moscow",
    "active": 1
})

requests.post(f"{API}/users", json={
    "name": "drzakirov"
})
requests.put(f"{API}/users/drzakirov", json={
    "contacts": {
        "call": "+7 999-111-4567",
        "email": "drzakirov@student.com",
        "slack": "drzakirov",
        "sms": "+7 999-111-4567"
    },
    "full_name": "Danis Zakirov",
    "time_zone": "EU/Moscow",
    "active": 1
})

requests.post(f"{API}/users", json={
    "name": "etoelvin"
})
requests.put(f"{API}/users/etoelvin", json={
    "contacts": {
        "email": "eeelvin@student.com",
        "slack": "etoelvin"
    },
    "full_name": "Elvina Rakhmatullina",
    "time_zone": "EU/Moscow",
    "active": 1
})

requests.post(f"{API}/users", json={
    "name": "betsy"
})
requests.put(f"{API}/users/betsy", json={
    "contacts": {
        "email": "betsy@google.com",
        "slack": "betsy"
    },
    "full_name": "Betsy Beyer",
    "time_zone": "US/Pacific",
    "active": 1
})

def create_team(username: str, password: str, team_name: str):
    sess = requests.Session()
    resp = sess.post(f"{DOMAIN}/login", data={
        "username": username,
        "password": password
    })

    csrf = resp.json()["csrf_token"]

    sess.post(f"{API}/teams", json={
        "name": team_name,
        "scheduling_timezone": "EU/Moscow",
    }, headers={
        "X-CSRF-TOKEN": csrf
    })

create_team("vsredkin", "vsredkin", "team_alpha")
create_team("betsy", "betsy", "team_beta")

requests.post(f"{API}/teams/team_alpha/rosters", json={
    "name": "roster1",
})

workgroup = ["drzakirov", "vsredkin", "etoelvin"]

for person in workgroup:
    requests.post(f"{API}/teams/team_alpha/rosters/roster1/users", json={
        "name": person,
    })

SECONDS_IN_HOUR = 60 * 60

SECONDS_IN_DAY = SECONDS_IN_HOUR * 24

def next_weekday(d, weekday):
    days_ahead = (weekday - d.weekday()) % 7
    return d + datetime.timedelta(days_ahead)

next_monday = next_weekday(datetime.datetime.now(), 0)

next_monday_morning = datetime.datetime.combine(next_monday.date(), datetime.time(hour=8))
if next_monday_morning < datetime.datetime.now():
    next_monday_morning += datetime.timedelta(days=7)

time = next_monday_morning

def rotate(l, n):
    return l[n:] + l[:n]

people = zip(cycle(workgroup), cycle(rotate(workgroup, 1)))

DURATION = datetime.timedelta(days=2)

while time < datetime.datetime.now() + datetime.timedelta(days=60):

    primary_person, secondary_person = next(people)

    requests.post(f"{API}/events", json={
        "start": int(time.timestamp()),
        "end": int((time+DURATION).timestamp()),
        "user": primary_person,
        "role": "primary",
        "team": "team_alpha"
    })

    requests.post(f"{API}/events", json={
        "start": int(time.timestamp()),
        "end": int((time+DURATION).timestamp()),
        "user": secondary_person,
        "role": "secondary",
        "team": "team_alpha"
    })

    time += DURATION


