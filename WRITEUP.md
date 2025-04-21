# WRITEUP
My goal for this project was to analyze the overall sentiment of headlines from a given news website. For my project, I chose to analyze National Geographic.
I imported the Requests, BeautifulSoup, and NLTK libraries to retrieve data from the URL, parse the text, and use specific functions for the analysis.
The results found that out of 24 headlines, 7 were classified as positive, 2 were classified as negative, and 15 were classified as neutral.
NatGeo's headlines were overall very neutral, which was not very surprising to me considering it is intended to be an educational website containing primarily objective information about science and history, albeit with some speculative articles relating to those subjects in the mix.
In fact, one of the two "negative" headlines wasn't even from a published article but rather one that addresses privacy/copyright concerns. This was only included with the overall analysis because the site didn't utilize that many HTML elements, and the only unique element for the article previews were their links signified by the 'a' element. This happens to be the element shared with some sort of navigation tab/sidebar unrelated to news.
