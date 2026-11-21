"""Render the profile activity panel from GitHub GraphQL data."""
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

QUERY = """
query($login: String!) {
  user(login: $login) {
    followers(first: 1) { totalCount }
    repositories(first: 1, privacy: PUBLIC, ownerAffiliations: [OWNER]) { totalCount }
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date weekday contributionCount contributionLevel } }
      }
    }
  }
}
"""

COLORS = dict(zip(
    ("NONE", "FIRST_QUARTILE", "SECOND_QUARTILE", "THIRD_QUARTILE", "FOURTH_QUARTILE"),
    ("#253345", "#235769", "#287f88", "#42b5ab", "#9bf3cf"),
))


def fetch_user():
    request = Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": "Sanzzz1125"}}).encode(),
        headers={
            "Authorization": f"Bearer {os.environ['GH_TOKEN']}",
            "Content-Type": "application/json",
            "User-Agent": "profile-observatory",
        },
    )
    with urlopen(request, timeout=30) as response:
        result = json.load(response)
    if result.get("errors") or not result.get("data", {}).get("user"):
        raise RuntimeError(f"GitHub GraphQL request failed: {result.get('errors')}")
    return result["data"]["user"]


def render(user):
    calendar = user["contributionsCollection"]["contributionCalendar"]
    weeks = calendar["weeks"]
    if not weeks or len(weeks) > 54:
        raise ValueError("Expected up to 54 weeks in the contribution calendar")
    streak = best_streak = 0
    cells = []
    for column, week in enumerate(weeks):
        for day in week["contributionDays"]:
            count = day["contributionCount"]
            streak = streak + 1 if count else 0
            best_streak = max(best_streak, streak)
            x = 27 + column * 15
            y = 67 + day["weekday"] * 14
            color = COLORS[day["contributionLevel"]]
            cells.append(f'<rect x="{x}" y="{y}" width="11" height="11" rx="2" fill="{color}"/>')

    streak_label = f"{best_streak} day" if best_streak == 1 else f"{best_streak} days"
    stats = [
        ("CONTRIBUTIONS", calendar["totalContributions"]),
        ("BEST STREAK", streak_label),
        ("PUBLIC REPOS", user["repositories"]["totalCount"]),
        ("FOLLOWERS", user["followers"]["totalCount"]),
    ]
    stats_markup = []
    for index, (label, value) in enumerate(stats):
        x = 27 + index * 203
        stats_markup.append(f"""
  <rect x="{x}" y="185" width="193" height="64" rx="8" fill="#192637"/>
  <text x="{x + 13}" y="208" fill="#b7cbda" font-size="13">{label}</text>
  <text x="{x + 13}" y="233" fill="#f2f6fb" font-size="22" font-weight="700">{value}</text>""")

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 272" role="img" aria-labelledby="title" font-family="ui-monospace, monospace">
  <title id="title">GitHub activity: {calendar["totalContributions"]} contributions and a best streak of {streak_label} over the past year</title>
  <defs>
    <clipPath id="grid"><rect x="27" y="61" width="805" height="109"/></clipPath>
  </defs>
  <rect x="1" y="1" width="858" height="270" rx="16" fill="#101722" stroke="#374c61"/>
  <text x="27" y="38" fill="#a1edd7" font-size="17" letter-spacing="2">CONTRIBUTION FLIGHT</text>
  <text x="831" y="38" text-anchor="end" fill="#b7cbda" font-size="14">PAST YEAR</text>
  {''.join(cells)}
  <g clip-path="url(#grid)">
    <g>
      <path d="M-30 110h19m-27 6h24m-13 6h16" stroke="#e6a362" stroke-width="2" stroke-linecap="round"/>
      <path d="M-10 105L13 116-10 127-5 116Z" fill="#ffda96" stroke="#101722" stroke-width="2"/>
      <circle cx="0" cy="116" r="2.6" fill="#235769"/>
      <animateMotion path="M28 0 C190 -47 300 53 445 0 S700 -46 850 0" dur="11s" repeatCount="indefinite"/>
    </g>
  </g>
  {''.join(stats_markup)}
</svg>
'''


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "assets" / "activity.svg"
    output.write_text(render(fetch_user()), encoding="utf-8")
