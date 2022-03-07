# Contenda Takehome
Hello! 👋 Thank you for checking out this repository. To make sure you're in the right place, this is the repo for the following jobs:

> [Senior Engineer](https://careers.contenda.co/senior)

> [Fullstack Engineer](https://careers.contenda.co/fullstack)

The goal of this assignment is twofold. One, we want to make sure you'd actually be happy doing the type of work we do on a daily basis. This assignment mocks a real feature that we already have in production. Two, we want to see how you think about real world problems, not leetcode brain teasers. It's especially helpful if you can walk us through your thinking via writing. 

If you have any questions, please email lilly@contenda.co.

## Task
Contenda strives to increase the top of funnel engagement for technical content. We know people work really hard to make high quality content, but sometimes it gets lost in the noise, or just due to time of posting. Let's say I made a Getting Started guide and posted it during my work day (2PM EST). That's 8PM in London, midnight in Dubai, and 5AM in Tokyo. A lot of people are going to miss my content because of *time*. **The goal of this feature is to find optimal times to post content so that all of my Twitter followers can have equal visibility**. 

As a user, I'm really concerned about annoying my followers. I definitely don't want something to post so often that it feels robotic. Keep that in mind when you're designing a solution. Remember, not all problems are solved through code. If you have a solution through UX, product, or even just good copy, tell us in the README. 

At your disposal is a large `json` dump of Twitter follower data from this endpoint:

https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-followers

#### Input
A single date time object that has the day and the time.

`datetime.now()`

#### Output
Array of datetime objects that have the day and the time.

`[datetime.datetime]`

## Setup
For your convenience, I put a Dockerfile and helloworld Python file into this repo. Do the following to get started:


