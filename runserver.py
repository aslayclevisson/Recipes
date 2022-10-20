import subprocess


def dev():
    run_dev = ['python', 'manage.py', 'runserver', '8000', '--settings=project.settings.local']
    subprocess.run(run_dev)


def prod():
    # ngrok port 8080
    run_prod = ['python', 'manage.py', 'runserver', '8080', '--settings=project.settings.production']
    subprocess.run(run_prod)
