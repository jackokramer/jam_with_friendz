from config import app
from controller_functions import index, regis, verif, finish, login, homepage, signups, rehearse, stores, concerts, upcoming, logout

app.add_url_rule('/', view_func=index)
app.add_url_rule('/regis', view_func=regis, methods=['POST'])
app.add_url_rule('/verif', view_func=verif)
app.add_url_rule('/finish', view_func=finish, methods=['POST'])
app.add_url_rule('/login', view_func=login, methods=['POST'])
app.add_url_rule('/homepage', view_func=homepage)
app.add_url_rule('/signups', view_func=signups)
app.add_url_rule('/rehearse', view_func=rehearse, methods=['POST'])
app.add_url_rule('/stores', view_func=stores)
app.add_url_rule('/concerts', view_func=concerts)
app.add_url_rule('/sessions', view_func=upcoming)
app.add_url_rule('/logout', view_func=logout)