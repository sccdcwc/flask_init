import os
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from config import Flag

if Flag == 'master':
    app = create_app('production')
elif Flag == 'dev':
    app = create_app('development')
elif Flag=="test":
    app = create_app('testing')
else:
    app=create_app("default")

# manager = Manager(app)
# migrate = Migrate(app, db)

# def make_shell_context():
#     return dict(app=app, db=db)

# manager.add_command("shell",Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8011, debug=True, use_reloader=False)