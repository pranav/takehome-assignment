MY README
=========

# Setup

```shell
pip install -r requirements.txt
python main.py
```

# What this code does

There are two main things that this code does
1. It takes in twitter follower data and attempts to convert their location into a timezone.
2. Given the current time, it figures out when the next time to post a tweet that will reach the most followers will be.
   For the sake of this exercise, it will choose 9am as the best time to tweet something.

# What I would have liked to get to
1. Better cleanup/sanitization of the input data, possibly regex matching locations or removing Nones.
2. A better way to geocode locations. 
   I used the Google Maps Geocoding API to guess follower locations, which is incredibly expensive for 72k followers. 
   At $5/1000 API requests, guessing the 72,000+ followers here would have been very expensive so I took a small sample.
   I could have shrunk it down significantly if I had removed all the Nones.
3. More documentation surrounding the code, with more time I could have made things more clear or abstracted things
   better but I decided for a one-off this was okay.

# How I spent my time
1. Hilariously, I went on twitter to see how tweets get surfaced to me. If other people I know liked/retweeted something,
   I would see a tweet from a day or two ago before newer tweets on my timeline. That tells me the quality of the tweet
   matters a lot and if I surface it to many people once, it will appear for other people any time of day for them.
2. I spent some time looking at the output of the location data from the given netlify follower list and saw a lot of
   unstructured data so I tried to find an API that would geocode fuzzy text. Google Maps Geocoding API seemed simple
   enough to use to I went with that.
3. I spent a lot of time thinking about what "optimal" time meant for a tweet. I went with the marketing tried and true:
   9am. I'm sure there are better times but for this exercise, choosing an arbitrary time was enough. If I did this for 
   real I think there would be other factors I could look at but with the data I had this seemed like enough.