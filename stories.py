"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer}:

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text, description=None):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.description = description if description else words

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            if val == '':
                continue
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story_list = [
    Story(
        ["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a
    large {adjective} {noun}. It loved to {verb} {plural_noun}."""),

    Story(
        ["noun"],
        """A nice Succulent {noun} is the best thing in the world.""",
        description="A Thrilling Tale of a joy")
]
