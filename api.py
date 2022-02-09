import justpy as jp
import definition
import json


class Api:
    """Handles requests at /api?w=word"""
    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get("w")

        definition_word = definition.Definition(word).get()  # Gets the definition of the word

        response = {
            "word":word,
            "definition":definition_word
        }

        wp.html = json.dumps(response)
        return wp


