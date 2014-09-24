import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

import bobo

@bobo.query('/')
def home():
	return "Home Page"

@bobo.query('/about')
def about():
	return "About Page"	