import datetime
import logging
import os
import sys

from sheets import GoogleSheetsUpdater
from yandex_contest_api import YandexContestAPI


def main(contests):
    gsu = GoogleSheetsUpdater('HSE Algo Seminars 2021', 'Контесты 3-4 модуль')

    students = gsu.get_students_list()

    gsu.wks.update('A1', str(datetime.datetime.now()))
    logging.info(students)

    for contest_id, is_long in contests:
        oauth_token = os.getenv("YANDEX_CONTEST_OAUTH_KEY")
        assert oauth_token is not None, "env YANDEX_CONTEST_OAUTH_KEY must be set"

        yandex_contest_api = YandexContestAPI(oauth_token, contest_id)
        standings = yandex_contest_api.generate_standings(students)
        gsu.update_sheet(standings, is_long)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    main([
        (24514, False),
        (24808, False),
        (24924, True),
        (26746, True),
        (26747, False),
        (27185, False),
    ])
