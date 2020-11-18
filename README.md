# NestleBot-2020

_Isn't that title going to be outdated in, like, a month? -- Professor Greggory Durret, Ph.D._

---

Hello internet. How are you?

I am ambiguously employed right now, so I am making a Twitter bot to ***tweet about products by Nestle*** (to avoid, shun, boycott, &tc).

[Nestle is evil](https://www.reddit.com/r/FuckNestle/comments/hmv0nv/the_reasons_why_we_hate_nestle_so_much/) and this Twitter bot will be the viral internet tour de force that takes it down, probably.


## How it works

Here are the steps I have in mind:

1) (Google image search)[https://pypi.org/project/Google-Images-Search/] for "Nestle", maybe randomly choosing one among a hard-coded list of brand or product names to search for

2) Out of the top N search results, filter out any images that don't contain text using the (EAST image detector)[https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/] powered by (OpenCV)[https://opencv.org/]. This is a pretty coarse filter, but just to set expectations here, it is about as fancy as you should expect anything in this project to get.

3) Compose a tweet. Combine the image with, I dunno,

  * V1) some generic text ("Nestle is terrible. This is a Nestle product. Don't buy it. Thanks.")

  * V2) some hard-coded information about that product 

  * V3) some freshly extracted information about Nestle (recent news articles shared on anti-Nestle websites, such as (/r/FuckNestle)[http://www.reddit.com/r/FuckNestle].

4) Tweet the tweet
