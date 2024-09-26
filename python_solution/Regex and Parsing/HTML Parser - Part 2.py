from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
 def handle_comment(self, comment):
        if '\n' in comment:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
            
        print(comment)
    
 def handle_data(self, data):
        if data == '\n': return
        print('>>> Data')
        print(data)  
  