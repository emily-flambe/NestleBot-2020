# NestleBot-2020

_Isn't that title going to be outdated in, like, a month? -- Professor Greggory Durret, Ph.D._

---

## [Here is the bot on Twitter, wow](https://twitter.com/NestleBot2020)

Hello internet. How are you?

I am ambiguously employed right now, so I am making a Twitter bot to ***tweet about products by Nestle*** (to avoid, shun, boycott, &tc).

[Nestle is evil](https://www.reddit.com/r/FuckNestle/comments/hmv0nv/the_reasons_why_we_hate_nestle_so_much/) and this Twitter bot will be the viral internet tour de force that takes it down, probably.


## How it works

TBD lmao

### Future directions in NestleBot science

This bot doesn't HAVE to tweet only about Nestle - there are lots of brands people might consider boycotting!

Charles Stover already made a page that makes it easy to look up whether a product is owned by a brand/company that you might consider hating for one reason or another: https://charlesstover.github.io/peoplecott/ (or here is the [repo itself](https://github.com/CharlesStover/peoplecott)).

NestleBot could use the [underlying data](https://github.com/CharlesStover/peoplecott/tree/master/src/constants) to tweet not only about Nestle, but about products from other brands as well! Stover's dataset only includes Nestle for now, but it appears set up to [accommodate multiple companies](https://github.com/CharlesStover/peoplecott/blob/master/src/constants/entities.ts) and multiple reasons to detest any of them.


## Deployment on Heroku

This bot is deployed on Heroku and is currently configured to compose + send a tweet every hour. Tweets might contain stupid images that manage to evade the purpose of the bot - that's *show biz*, baby!

### Heroku requirements

If you, the curious onlooker, wanted to deploy this yourself, you would need to run these commands before locking the pipfile. Maybe this is obvious?

`pipenv install tweepy`

`pipenv install numpy`

`pipenv install imutils`

`pipenv install opencv-contrib-python`
