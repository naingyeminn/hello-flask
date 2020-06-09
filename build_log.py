from datetime import datetime
with open('build.log', 'a') as file:
  file.write('Build completed at: %s\n' %datetime.now())
