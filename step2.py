import urllib2
print('[1] TV show')
print('[2] Movie')
B = input('>>>>>')
if B == '1':
 #get movie link

 #hide id
 print urllib2.urlopen(mlink).url

if B == '2':
  #get TV show link
  
  #hide id
  print urllib2.urlopen(tvlink).url