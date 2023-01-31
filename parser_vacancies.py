import json
import requests
from bs4 import BeautifulSoup


def get_first_vacancies_from_yandex():
    """Задача этой функции - собрать имеющиеся вакансии на сайте и записать их в словарь."""
    with open("vacancies_dict.json", encoding="utf-8") as file:  # для windows - encoding="utf-8"
        vacancies_dict = json.load(file)

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70"
    }

    url = "https://yandex.ru/jobs/vacancies/?cities=moscow&text=&skills=34&pro_levels=junior"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    vacancies_cards = soup.find_all("span", class_="lc-jobs-vacancy-card")

    for vacancy in vacancies_cards:
        vacancy_title = vacancy.find("div", class_="lc-jobs-vacancy-card__header").text.strip()
        vacancy_url = f'https://yandex.ru{vacancy.find("a").get("href")}'
        vacancy_id = vacancy.get("data-vacancy-id")

        vacancies_dict[vacancy_id] = {
            "vacancy_title": vacancy_title,
            "vacancy_url": vacancy_url
        }

    with open("vacancies_dict.json", "w", encoding="utf-8") as file:  # для windows - encoding="utf-8"
        json.dump(vacancies_dict, file, indent=4, ensure_ascii=False)


def get_first_vacancies_from_vk():
    """Задача этой функции - собрать имеющиеся вакансии на сайте и записать их в словарь."""
    with open("vacancies_dict.json", encoding="utf-8") as file:  # для windows - encoding="utf-8"
        vacancies_dict = json.load(file)

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70"
    }

    url = "https://team.vk.company/vacancy/?specialty=282&town=1&tag=2221"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    vacancies_cards = soup.find_all("a", class_="result-item js-result-list-item")

    for vacancy in vacancies_cards:
        vacancy_title = vacancy.find("h3").text.strip()
        vacancy_url = f'https://team.vk.company{vacancy.get("href")}'
        vacancy_id = vacancy.get("href").strip("/").split("/")[-1]

        vacancies_dict[vacancy_id] = {
            "vacancy_title": vacancy_title,
            "vacancy_url": vacancy_url
        }

    with open("vacancies_dict.json", "w", encoding="utf-8") as file:  # для windows - encoding="utf-8"
        json.dump(vacancies_dict, file, indent=4, ensure_ascii=False)


def check_vacancies_update_from_yandex():
    """Проверка на новые вакансии, запись новых вакансий в общий словарь и словарь с только новыми вакансиями."""
    with open("vacancies_dict.json", encoding="utf-8") as file:  # для windows - encoding="utf-8"
        vacancies_dict = json.load(file)

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70"
    }

    url = "https://yandex.ru/jobs/vacancies/?cities=moscow&text=&skills=34&pro_levels=junior"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    vacancies_cards = soup.find_all("span", class_="lc-jobs-vacancy-card")

    fresh_vacancies = {}

    for vacancy in vacancies_cards:
        vacancy_id = vacancy.get("data-vacancy-id")
        if vacancy_id in vacancies_dict:
            continue
        else:
            vacancy_title = vacancy.find("div", class_="lc-jobs-vacancy-card__header").text.strip()
            vacancy_url = f'https://yandex.ru{vacancy.find("a").get("href")}'

            vacancies_dict[vacancy_id] = {
                "vacancy_title": vacancy_title,
                "vacancy_url": vacancy_url
            }

            fresh_vacancies[vacancy_id] = {
                "vacancy_title": vacancy_title,
                "vacancy_url": vacancy_url
            }

    with open("vacancies_dict.json", "w", encoding="utf-8") as file:  # для windows - encoding="utf-8"
        json.dump(vacancies_dict, file, indent=4, ensure_ascii=False)

    return fresh_vacancies


def check_vacancies_update_from_vk():
    """Проверка на новые вакансии, запись новых вакансий в общий словарь и словарь с только новыми вакансиями."""
    with open("vacancies_dict.json", encoding="utf-8") as file:  # для windows - encoding="utf-8"
        vacancies_dict = json.load(file)

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70"
    }

    url = "https://team.vk.company/vacancy/?specialty=282&town=1&tag=2221"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    vacancies_cards = soup.find_all("a", class_="result-item js-result-list-item")

    fresh_vacancies = {}

    for vacancy in vacancies_cards:
        vacancy_id = vacancy.get("href").strip("/").split("/")[-1]
        if vacancy_id in vacancies_dict:
            continue
        else:
            vacancy_title = vacancy.find("h3").text.strip()
            vacancy_url = f'https://team.vk.company{vacancy.get("href")}'

            vacancies_dict[vacancy_id] = {
                "vacancy_title": vacancy_title,
                "vacancy_url": vacancy_url
            }

            fresh_vacancies[vacancy_id] = {
                "vacancy_title": vacancy_title,
                "vacancy_url": vacancy_url
            }

    with open("vacancies_dict.json", "w", encoding="utf-8") as file:  # для windows - encoding="utf-8"
        json.dump(vacancies_dict, file, indent=4, ensure_ascii=False)

    return fresh_vacancies


def main():
    # get_first_vacancies_from_yandex() эту функцию нужно использовать один раз для заполнения json начальными данными
    # get_first_vacancies_from_vk() эту функцию нужно использовать один раз для заполнения json начальными данными
    check_vacancies_update_from_yandex()
    check_vacancies_update_from_vk()


if __name__ == "__main__":
    main()
