import json
from datetime import datetime, timedelta
import pytz
from typing import List, Dict, Any
from collections import defaultdict

from location_db import LocationDb


location_db = LocationDb()


def read_follower_data():
    with open("Netlify-follower-raw.json", "r") as f:
        data = json.load(f)
        return data


def build_location_db():
    """
    One time build out the database from the twitter follower data
    """
    location_db = LocationDb()
    follower_data = read_follower_data()
    locations = [",".join(value[0].split("username=")[1].split(",")[1:])
                 for value in follower_data.values()]
    for location in locations:
        location_db.get_location_timezone(location)


def get_user_location(user_data:List[str]) -> str:
    """
    take in the list of user data like
    [<User id=1500017105407602688 name=Papon Barmon username=barmon_papon1>, 'Dhaka, Bangladesh']
    and output the location. This data is dirrrty so some basic cleanup.
    """
    return ",".join(user_data[0].split("username=")[1].split(",")[1:])


def get_user_post_time(user_data:List[str], requested_date_time: datetime)-> datetime:
    """
    Given a user in the follower data and a date time, return the user's datetime in their tz
    :param user_data:
    :param requested_date_time:
    :return:
    """
    user_location = get_user_location(user_data)
    user_timezone = location_db.get_location_timezone(user_location)

    return requested_date_time.astimezone(user_timezone)


def get_highest_count(data: Dict[Any, int]) -> Any:
    return max(data, key=data.get)


def main(now:datetime):
    """
    Given a datetime.datetime.now(), figure out the next optimal time to post the tweet to reach
    the most of your followers. I'm going to assume 9am is the optimal time to tweet.
    This means find the next 9am in the time zone that contains most of your followers, starting from datetime.now().
    :return:
    """
    followers = read_follower_data()
    timezone_counts = defaultdict(lambda: 0)
    for follower in followers.keys():
        timezone = location_db.get_location_timezone(get_user_location(followers[follower]), use_google_maps=False)
        timezone_counts[timezone] += 1
    timezone_with_highest_number_of_followers = get_highest_count(timezone_counts)
    now_in_optimal_timezone = now.astimezone(pytz.timezone(timezone_with_highest_number_of_followers))

    # Get the next 9am datetime in optimal time zone
    if now_in_optimal_timezone.hour >= 9:
        optimal_time = (now_in_optimal_timezone + timedelta(days=1)).replace(hour=9, minute=0, microsecond=0, second=0)
    else:
        optimal_time = now_in_optimal_timezone.replace(hour=9, minute=0, microsecond=0, second=0)
    print("Optimal time to post tweet:", optimal_time)


if __name__ == '__main__':
    main(datetime.now())