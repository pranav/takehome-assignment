# Contenda Takehome
Hello! 👋 Thank you for checking out this repository. To make sure you're in the right place, this is the repo for the following jobs:

> [Senior Engineer](https://careers.contenda.co/senior)

> [Fullstack Engineer](https://careers.contenda.co/fullstack)

The goal of this assignment is twofold. One, we want to make sure you'd actually be happy doing the type of work we do on a daily basis. This assignment mocks a real feature that we already have in production. Two, we want to see how you think about real world problems, not leetcode brain teasers. It's especially helpful if you can walk us through your thinking via writing. 

**Please don't spend more than 3 hours on this assignment.** We're really excited to see what you can do, but we also want to respect your time 😄

If you have any questions, please email lilly@contenda.co.

## Task
Contenda strives to increase the top of funnel engagement for technical content. We know people work really hard to make high quality content, but sometimes it gets lost in the noise, or just due to time of posting. Let's say I made a Getting Started guide and posted it during my work day (2PM EST). That's 8PM in London, midnight in Dubai, and 5AM in Tokyo. A lot of people are going to miss my content because of *time*. **The goal of this feature is to find optimal times to post content so that all of my Twitter followers can have equal visibility, no matter where in the world they are located**. 

As a user, I'm really concerned about annoying my followers. I definitely don't want something to post so often that it feels robotic. Keep that in mind when you're designing a solution. Remember, not all problems are solved through code. If you have a solution through UX, product, or even just good copy, tell us in the README. 

At your disposal is a large `json` dump of Twitter follower data from this endpoint:

https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-followers

One of our interns exported the file and something went wrong. It should be: `{"{user_id}":[{user.data},"{user.data.location}"` . Here is an example: `{"1500017105407602688":[<User id=1500017105407602688 name=Papon Barmon username=barmon_papon1>, 'Dhaka, Bangladesh']}`. But instead it's got some weird tags and other stuff in it. Unfortunately, I don't have time to clean it up, so uh. Good luck. 

#### Input
A single date time object that has the day and the time.

`datetime.now()`

#### Output
Array of datetime objects that have the day and the time.

`[datetime.datetime]`

## Setup
For your convenience, I put a Dockerfile and helloworld Python file into this repo. Do the following to get started:

1. Install Docker. We're going to be using the official python3 image from the Docker repo. 
2. Clone this repo and `cd` into it
3. `docker build -t main .`
4. `docker run main`

It should print "Hello World!". 

## Evaluation
Submit a Github repo (fork this one) via email to lilly@contenda.co. Please include a README that has the following:

1. Any additional setup required outside of the ones I wrote so that I can run your app
2. What your code does and why
4. Stuff you'd like to get to but didn't have the time
5. A rough estimate of how you spent your time

When I read your code, I'll be asking myself the following:

- Does this solve the business problem?
- Is this code efficient?
- Is this code understandable? 
- Did you use your time well?

If it makes sense, we'll organize a video call for our engineering team to ask you a few questions live and walk through the code together. 

Can't wait to see what you come up with! As always, if you have any feedback on this particular assignment, please let me know. 
