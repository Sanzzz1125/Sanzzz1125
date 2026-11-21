"""Draw this profile's activity artwork from GitHub contribution data."""
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET

THEME = 'source-material'
LEVELS = ('NONE', 'FIRST_QUARTILE', 'SECOND_QUARTILE', 'THIRD_QUARTILE', 'FOURTH_QUARTILE')
QUERY = """
query($user: String!, $start: DateTime!, $end: DateTime!) {
  user(login: $user) {
    year: contributionsCollection(from: $start, to: $end) {
      contributionCalendar { totalContributions }
    }
    rolling: contributionsCollection {
      contributionCalendar {
        weeks { contributionDays { weekday contributionLevel } }
      }
    }
  }
}
"""
PALETTES = {
    'night-express': ('#122633', '#f9edce', '#a7d9ca', '#30414a', '#ffd291'),
    'source-material': ('#e9e6db', '#171918', '#373a25', '#c6c3b6', '#435616'),
    'after-hours': ('#382a33', '#ffebca', '#e2c4b4', '#5e4850', '#f4b980'),
}


def fetch():
    now = datetime.now(timezone.utc).replace(microsecond=0)
    start = now.replace(month=1, day=1, hour=0, minute=0, second=0)
    variables = {'user': 'Sanzzz1125', 'start': start.isoformat(), 'end': now.isoformat()}
    req = Request('https://api.github.com/graphql',
                  data=json.dumps({'query': QUERY, 'variables': variables}).encode(),
                  headers={'Authorization': 'Bearer ' + os.environ['GH_TOKEN'],
                           'Content-Type': 'application/json', 'User-Agent': 'Sanzzz1125-profile'})
    with urlopen(req, timeout=30) as response:
        data = json.load(response)
    if data.get('errors'):
        raise RuntimeError(data['errors'])
    user = data['data']['user']
    weeks = []
    for week in user['rolling']['contributionCalendar']['weeks'][-26:]:
        levels = [None] * 7
        for day in week['contributionDays']:
            levels[day['weekday']] = LEVELS.index(day['contributionLevel'])
        weeks.append(levels)
    if not weeks:
        raise ValueError('GitHub returned an empty calendar')
    return now.date().isoformat(), user['year']['contributionCalendar']['totalContributions'], weeks


def render(theme, date, annual, weeks):
    bg, ink, secondary, quiet, accent = PALETTES[theme]
    svg = ET.Element('svg', xmlns='http://www.w3.org/2000/svg', width='1080', height='246',
                     viewBox='0 0 1080 246', role='img')
    def element(tag, **attrs):
        return ET.SubElement(svg, tag, {k: str(v) for k, v in attrs.items()})
    def rect(x, y, w, h, color):
        return element('rect', x=x, y=y, width=w, height=h, fill=color)
    def circle(x, y, r, color):
        element('circle', cx=x, cy=y, r=r, fill=color)
    def text(x, y, value, size, color, family='monospace', weight='normal'):
        node = element('text', x=x, y=y, fill=color, **{'font-size':size, 'font-family':family, 'font-weight':weight})
        node.text = str(value)

    active = sum(bool(level) for week in weeks for level in week)
    best = run = 0
    for week in weeks:
        for level in week:
            if level is not None:
                run = run + 1 if level else 0
                best = max(best, run)

    element('title').text = f'{annual} contributions this year. {active} active days and a best streak of {best} days in the last 26 weeks. Updated {date}.'
    rect(0, 0, 1080, 246, bg)
    heading, key = {
        'night-express': ('City lights', 'One building per week. Each lit window is an active day.'),
        'source-material': ('Ink density', 'One dot per day. Larger dots mark higher activity.'),
        'after-hours': ('Recording levels', 'One meter per week. Each lit segment is an active day.'),
    }[theme]
    text(31, 39, heading, 29, ink, 'Georgia, serif' if theme=='after-hours' else 'Arial, sans-serif', 'bold')
    text(31, 64, key, 15, secondary, 'Arial, sans-serif')
    for i, week in enumerate(weeks):
        x = 32 + 23*i
        if theme == 'night-express':
            top = 84+(i*13%19)
            rect(x,top,20,197-top,'#2e4650')
            rect(x+4,top-4,12,4,'#2e4650')
            for j, level in enumerate(week):
                if level is None:
                    continue
                color = (quiet,'#83aeaa','#94d4c2','#f3b57f','#ffe1a3')[level]
                rect(x+5,111+j*12,11,6,color)
        elif theme == 'source-material':
            for j,level in enumerate(week):
                if level is not None:
                    circle(x+9,90+j*17,(2,4,5,6,8)[level],quiet if level==0 else accent)
        else:
            count = sum(bool(level) for level in week)
            for j in range(7):
                color = (accent if j<4 else '#eb927d') if j<count else quiet
                rect(x,180-j*14,17,10,color)
    text(31,224,'26 WEEKS   /   '+date,16,secondary)
    rect(665,25,2,195,quiet)
    for y, value, label in [(61,annual,'contributions this year'),(125,active,'active days in 26 weeks'),(189,best,'best streak in 26 weeks (days)')]:
        text(695,y,str(value),35,ink,'Arial, sans-serif','bold')
        text(695,y+20,label,16,secondary,'Arial, sans-serif')
    return ET.tostring(svg, encoding='unicode') + '\n'


if __name__=='__main__':
    path = Path(__file__).resolve().parents[1] / 'assets' / 'activity.svg'
    path.write_text(render(THEME, *fetch()), encoding='utf-8')
