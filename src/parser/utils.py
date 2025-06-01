import requests
from bs4 import BeautifulSoup


def parse_techpark_table(limit=10):
    url = "https://astanahub.com/ru/service/techpark/"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table")
    rows = table.find_all("tr")[1:]  # Пропустить заголовок

    companies = []

    for row in rows[:limit]:
        cols = row.find_all("td")
        if len(cols) < 6:
            continue  # пропустить неполные строки

        companies.append(
            {
                "certificate_number": cols[0].text.strip(),
                "issue_date": cols[1].text.strip(),
                "valid_until": cols[2].text.strip(),
                "bin": cols[3].text.strip(),
                "status": cols[4].text.strip(),
                "name": cols[5].text.strip(),
            }
        )

    return companies
