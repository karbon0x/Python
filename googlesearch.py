import webbrowser
google = raw_input('What do you want to search google for:')
webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)
