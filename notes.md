# 1. Render HTML and Markdown
- in post detail.html ,add a filter safe to instance.content(instance.content|safe), this changes the way how things are rendered. e.g. add <h1>Hi, there </h1>
    - safe works by allowing us rendering html, however, it is not user friendly, taking too long to write post using html.
- Another different html rendering system, called markdown, a quick way to rendering html, such as you can use #, ## etc. the html markdown syntax. 
    - rendering by javascript, install jQuery CDN in the base.html. go to code.jquery.com,
    - add "marked" javascript library, parse and compile markdown written in JavaScript(github.com/chjj/marked), we don't need to install it, instead use cdn. go : cdnjs.com/libraries/marked, copy the cdn code to the base.html. This will alow us to implement the javascript functions to allow us to render our actual content
    - add a new div class, content-markdown, for the content need to be marked down in the post detail.htm. this class basically mark this content meaning that we are going to mark down this content at some point
    - write and add a new javascript in the base.html to implement our simple jQuery function
 
 2. 
    
    