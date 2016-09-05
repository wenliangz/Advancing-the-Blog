# =========== Rendering Markdown using Javascript============

# 1. Render HTML and Markdown
- in post detail.html ,add a filter safe to instance.content(instance.content|safe), this changes the way how things are rendered. e.g. add <h1>Hi, there </h1>
    - safe works by allowing us rendering html, however, it is not user friendly, taking too long to write post using html.
- Another different html rendering system, called markdown, a quick way to rendering html, such as you can use #, ## etc. the html markdown syntax. 
    - rendering by javascript, install jQuery CDN in the base.html. go to code.jquery.com,
    - add "marked" javascript library, parse and compile markdown written in JavaScript(github.com/chjj/marked), we don't need to install it, instead use cdn. go : cdnjs.com/libraries/marked, copy the cdn code to the base.html. This will alow us to implement the javascript functions to allow us to render our actual content
    - add a new div class, content-markdown, for the content need to be marked down in the post detail.html adn list.html. this class basically mark this content meaning that we are going to mark down this content at some point
    - write and add a new javascript in the base.html to implement our simple jQuery function
 
# 2. Implementation Django Pagedown for rendering markdown eiditing widget
what if the user doesn't know the markdown syntax for writing?  
- Install Pagedown editor
    - install django-pagedown library (github)
    - add pagedown into installed apps
    - collect the static files
- how to sue:
   - import PagedownWidget
   - use the Pagedown wideget itself inside of any particular field (content field here)
   -  in the post_form.html, we need to add css&javascript that are specifically related to the widget: 
        - in base add a block
        - in post_form, use the block with {{form.media}}
 Another example of implementing widget: 
 - implementing widget for selecting date for the date field: 
- Image in the Markdown Content
    - add a link directly in the Markdown Content
    
# 3. Responsive image inside the post Markdown 
if the size of the image is too big,we need to dynamic update the image within the post so that it can fit in a certain size, (responsive like bootstrap image)
- add a jQuery function/method(process) that convert all the content markdown images and add the class of image responsive, which is based on bootstrap
- we can NOT use truncatedchars and linebreaks filter on the content in order for markdown/ responsive image to work

# =========== Rendering Markdown using Dejango ============

# 4. django-markdown-deux (github) for rendering markdown
- pip install django-markdown-deux
- install markdown-deux app in django settings
- define a custome method, get_markdown, within model and return markdown content 
-  within the tempalte, we use {{obj.get_markdown}}
- put the template tag filter, safe, in the template, in order for the image content to show up. OR in the model itself, import django mark_safe function and return safe content
- however, the image is still not responsive. We still have to implement javascript to make the image response. we need to define a div class just for making responsive image.

# 5. trucate markdown post and django template tags adn filters
- truncate the post will remove the characters which may also remove images in the post
- we can use tempalte filter, called truncatechars_html(or truncateword_html), which is aware html tags.
- use django logic instead of filter if you can 

# 6. Dynamic Preview of the full Form Data
we are going to do it using jQuery
- To close the default preview by the PagedownWidget, go to Form.py and add paras:show_preview=False
- in post_form.html, we need to define  div with a some classes that jQuery can monitor this div targets in the form and bring it to preview.
- now , go to base.html, add/modify the javascript to enable preview function, and make it dynamically

# ========== make FORM look better  =================

# 7. crispy form
- install crispy form into virtual env: pip install django-crispy-forms
- in django settings
    - add crispy-form as app 
    - add CRISPY_TEMPLATE_PACK = 'bootstrap3 '
- Now we can use crispy-form tags, which specifically make our form look better
    - in our template, post_form.html, 
        - at the top add: {% load crispy_forms_tags}
        -  render form use {{form|crispy}}
- modify to make the wiget not indented.Inspect the class and change base.css

# 8. make our search bar look better by using Bootstrap input groups components
- inside the search form tag, define a input group div class: input-group and input class
- use font awesome icon for the search button text, make sure that font awesome cdn is installed to render it


# =========== Make our Comments look better ============
# 9. Create our own comments app instead of using facebook social plugin
- Comments should be a separate app, so that it can be used throughout the site
    - create comments app: ptyhon manage.py startapp comments
    - in the model, for testing, make user and post two foreign keys
- Use contentType and Generic Foreign Keys
    - the ideas is that we need to relate comments either to posts(comments on posts), or to other comments(comments on comments).The solution is to use contenttype 
        - import django GenericForeignKey and ContentType
        - create genericForeignKey for the comment model
    - Add comments into the post detail view by contenttype genericForeignKey.  

