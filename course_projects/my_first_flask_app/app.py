from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
posts = {
  0: {
    'id': 0,
    'title': 'Hello, World',
    'content': 'This is my first blog post!'
  }
}

@app.route('/')
def home():
  return render_template('home.jinja2', posts = posts)

@app.route('/post/<int:post_id>')
def post(post_id):
  post_obj = posts.get(post_id)
  if not post_obj: #POST WILL BE NONE IF NOT FOUND; NOT NONE => TRUE
    return render_template('404.jinja2', message = f'Post with id {post_id} not found!')
  return render_template('post.jinja2', post = post_obj)

@app.route('/post/create', methods = ['GET', 'POST'])
def create():
  if request.method == 'POST':
    title = request.form.get('title')
    content = request.form.get('content')
    post_id = len(posts)
    posts[post_id] = {'id': post_id, 'title': title,'content': content}

    return redirect(url_for('post', post_id = post_id))
  return render_template('create.jinja2')

if __name__ == '__main__':
  app.run(debug=True)