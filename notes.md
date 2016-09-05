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

# 6. 

