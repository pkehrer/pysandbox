from invoke import task


@task
def hello(c):
    print("hello world!")


@task
def functions(c, docs=False):
    c.run("python3 functions.py")
