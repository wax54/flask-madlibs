from flask import Flask, request, render_template
from stories import Story, story_list

app = Flask(__name__)

@app.route('/story/<int:story_id>')
def story_form(story_id):
    story = story_list[story_id]
    return render_template('story_form.html', prompts=story.prompts, story_id = story_id)

@app.route('/story_result/<int:story_id>', methods=["GET"])
def story_result(story_id):
    if not len(request.args):
        return story_form(story_id)
    story = story_list[story_id]
    #turn the array of tuples into a dict for Story.generate()
    ans = {prompt:answer for (prompt, answer) in request.args.items()}
    result = story.generate(ans).upper()
    print(result, story)
    return render_template('story_result.html', story=result)
