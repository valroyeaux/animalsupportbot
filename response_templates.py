"""
This file contains the templates for responses used in redditbot.py
"""

# End of the response template
## Contains 1 formattable field (for link references)
END_TEMPLATE = """
\n *** \n This was an automatically generated response based on the idea(s)/myth(s): \n\n {} \n\n
\n *** \n
*(Responses taken from vegan advocates like [Earthling Ed](https://www.youtube.com/channel/UCVRrGAcUc7cblUzOhI1KfFg) and our community contributors)* \n\n
*If you would like to contribute to the responses this bot can match to, please take a look at the [animalsupportbot GitHub repo](https://github.com/veganhacktivists/animalsupportbot)* \n\n
**[Vegan Hacktivists](https://veganhacktivists.org/), [Vegan Bootcamp](https://veganbootcamp.org/)**
"""

# Respond to mention with this comment when bot fails
## No forrmattable fields
FAILURE_COMMENT = """
Sorry, we couldn't quite match up this comment to one of our counter-arguments.

If you think it should have responded differently, raise this as an issue on the [GitHub repo](https://github.com/veganhacktivists/animalsupportbot/issues).
"""

# Failure message to PM user
## Contains 1 formattable field (for failed comment)
FAILURE_PM = """
Hi, we couldn't find a response to the following comment: \n
"{}" \n
If you think this response should have been responded to automatically, please report this as an issue on the [GitHub repo](https://github.com/veganhacktivists/animalsupportbot/issues)
"""
