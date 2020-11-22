# NestleBot-2020

_Isn't that title going to be outdated in, like, a month? -- Professor Greggory Durret, Ph.D._

---

## [Here is the bot wow](https://twitter.com/NestleBot2020)

Hello internet. How are you?

I am ambiguously employed right now, so I am making a Twitter bot to ***tweet about products by Nestle*** (to avoid, shun, boycott, &tc).

[Nestle is evil](https://www.reddit.com/r/FuckNestle/comments/hmv0nv/the_reasons_why_we_hate_nestle_so_much/) and this Twitter bot will be the viral internet tour de force that takes it down, probably.

### Future directions in NestleBot science

This bot doesn't HAVE to tweet only about Nestle - there are lots of brands people might consider boycotting!

Charles Stover already made a page that makes it easy to look up whether a product is owned by a brand/company that you might consider hating for one reason or another: https://charlesstover.github.io/peoplecott/ (or here is the [repo itself](https://github.com/CharlesStover/peoplecott)).

NestleBot could use the [underlying data](https://github.com/CharlesStover/peoplecott/tree/master/src/constants) to tweet not only about Nestle, but about products from other brands as well! Stover's dataset only includes Nestle for now, but it appears set up to [accommodate multiple companies](https://github.com/CharlesStover/peoplecott/blob/master/src/constants/entities.ts) and multiple reasons to detest any of them.

### Tweet Generation

Tweet types:

1) News articles - from crawling the web for recent news articles about Nestle doing bad things

2) Products - from google image search of Nestle brands and products

 * [Google image search](https://pypi.org/project/Google-Images-Search/) for "Nestle", maybe randomly choosing one among a hard-coded list of brand or product names to search for
 
 * Out of the top N search results, filter out any images that don't contain text using the [EAST image detector](https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/) powered by [OpenCV](https://opencv.org/). This is a pretty coarse filter, but just to set expectations here, it is about as fancy as you should expect anything in this project to get.

* Combine the image with, I dunno,

  * V1) some generic text ("Nestle is terrible. This is a Nestle product. Don't buy it. Thanks.")

  * V2) some hard-coded information about that product 

  * V3) some freshly extracted information about Nestle (recent news articles shared on anti-Nestle websites, such as [/r/FuckNestle](http://www.reddit.com/r/FuckNestle).
  
  
**Final Output**: Text + image content for NestleBot-2020 to tweet.

### Automatic Tweeting

Bot is hosted on Heroku and will compose + send a tweet every hour.

<<<<<<< Updated upstream
#### Heroku requirements

Gotta run these bits to build the pipfile with the stuff you need to SUCCEED.

=======
>>>>>>> Stashed changes
`pipenv install tweepy`

`pipenv install numpy`

`pipenv install imutils`

`pipenv install opencv-contrib-python`
