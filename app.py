from flask import Flask, request, render_template as render
from stories import Story, story_list

app = Flask(__name__)
@app.route('/')
def pick_a_story():
    """Returns the story picking page"""
    return render('pick_a_story.html',story_list=story_list)

@app.route('/story/<int:story_id>')
def story_form(story_id):
    """gets the story from the list and returns the unique story form html"""
    story = story_list[story_id]
    return render('story_form.html', prompts=story.prompts, story_id = story_id)

@app.route('/story_result/<int:story_id>', methods=["GET"])
def story_result(story_id):
    """returns the compiled story after receiving input from user
    note, if no arguments are included in this call, the story input form HTML will be returned instead
    """
    #if no arguments...
    if not len(request.args):
        #...return form page instead
        return story_form(story_id)
    #get the story from the list
    story = story_list[story_id]
    #turn the array of tuples into a dict for Story.generate()
    ans = {prompt:answer for (prompt, answer) in request.args.items()}
    #get the result from story.generate
    result = story.generate(ans)
    # return the html with the unique story passed in
    return render('story_result.html', story=result)
