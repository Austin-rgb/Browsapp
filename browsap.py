from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
import json
def startsession(server,port):
    server.run(port)
    
def foo():
    print('remote callback worked')

class Widget:
    
    def __init__(self):
        self._id=''
        self.widgets=[]
        self.events=dict()
        self.attrs=dict()
        self.attrs['id']=''
        self.css=''
        self.js=''
        self.text=''
        
    def add(self, widget):
        self.widgets.append(widget)
        widget.set_id(str(len(self.widgets)))

    def get_instance(self):
        return f'document.getElementById({self._id})'
    
    def get_widget(self,_id):
        for widget in self.widgets:
            if widget._id==_id:
                return widget
            
    def style(self,style):
        self.css=style
        
    def compile_events(self):
        results=''
        for event in self.events.keys():
            results+=' '+event+f'= "e_{self._id}_{event}()"'
        return results
    
    def compile_attributes(self):
        results=''
        self.attrs['id']+=f'{self._id}'
        for global_attr in self.attrs.keys():
            results+=' '+global_attr+'="'+self.attrs[global_attr]+'"'
        return results
    
    def set_id(self,_id):
        self._id+=_id
        for widget in self.widgets:
            widget.set_id(_id)
            
    def get_id(self):
        return self._id
    
    def get_css(self):
        css= f'#{self._id}'+self.css+'\n'
        for widget in self.widgets:
            css+=widget.get_css()
        return css
    def get_html(self):
        html=f'<div {self.compile_attributes()} {self.compile_events()} >'
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</div>'
        return html
    def get_js(self):
        for event in self.events.keys():
            if isinstance(self.events[event],type(foo)):
                self.js+='\n'+f' function e_{self._id}_{event}()'+'{'+f'execute({self._id},"{event}");'+'}'
            else:
                self.js+='\n'+f' function e_{self._id}_{event}(){self.events[event]}\n'
        for widget in self.widgets:
            self.js+=widget.get_js()
        return self.js

class Activity(BaseHTTPRequestHandler):

    def search_callback(self,widget,callback):
        widget=self.view.get_widget(widget)
        return widget.events[callback]
    
    def set_view(self,view):
        self.view=view

    def do_POST(self):
        content_len=int(self.headers['content-length'])
        post_body=json.loads(self.rfile.read(content_len).decode('utf-8'))
        if self.path=='/remote':
            command=self.search_callback(post_body['widget'],post_body['callback'])
            self.wfile.write(command())
        
        
    def do_GET(self):
        
        if self.path=='/remotef':
            pass
        else:
            remote_execution='''
function execute(widget_id,fun_name){
var xhttp=new XMLHttpRequest();
var data = new FormData()
data.append("widget",widget_id)
data.append("callback",fun_name)
xhttp.open("POST","remote",true);
xhttp.setRequestHeader("Content-Type","application/json")
xhttp.send(`{"widget":"${widget_id}","callback":"${fun_name}"}`);
}
                            '''
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(f'''<!doctype html>
                                   <html>
                                   <head>
                                   <script>{remote_execution}</script>
                                   <style>{self.view.get_css()}</style>
                                   <script>{self.view.get_js()}</script>
                                   <title>{self.title}</title>
                                   </head>
                                   <body>{self.view.get_html()}</body>
                                   </html>''','utf-8'))

class A(Widget):
    def get_html(self):
        return f'<a {self.compile_attributes()} {self.compile_events()}>{self.text}</a>'
class App(ThreadingHTTPServer):
    pass
class Abbr(Widget):
    def get_html(self):
        return f'<abbr {self.compile_events()} {self.compile_attributes()}>{self.text}</abbr>'

class Area(Widget):
    def get_html(self):
        return f'<area {self.compile_events()} {self.compile_attributes()}>{self.text}</area>'

class Blockquote(Widget):
    def get_html(self):
        html=f'<blockquote {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</blockquote>'
        return html
    
class Caption(Widget):
    def get_html(self):
        html=f'<caption {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</caption >'
        return html
    
class Cite(Widget):
    def get_html(self):
        html=f'<cite {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</cite>'
        return html
    
class Code(Widget):
    def get_html(self):
        html=f'<code {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</code>'
        return html
    
class Col(Widget):
    def get_html(self):
        html=f'<col {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</col>'
        return html
    
class Colgroup(Widget):
    def get_html(self):
        html=f'<colgroup {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</colgroup >'
        return html
    
class Command(Widget):
    def get_html(self):
        html=f'<command {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</command >'
        return html
class Dd(Widget):
    def get_html(self):
        html=f'<dd {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</dd >'
        return html
    
class Del(Widget):
    def get_html(self):
        html=f'<del {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</del>'
        return html
    
class Dfn(Widget):
    def get_html(self):
        html=f'<dfn {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</dfn >'
        return html
    
class Dialog(Widget):
    def get_html(self):
        html=f'<dialog {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</dialog >'
        return html
    
class Div(Widget):
    def get_html(self):
        html=f'<div {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</div >'
        return html
class Dl(Widget):
    def get_html(self):
        html=f'<dl {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</dl >'
        return html
    
class Menu(Widget):
    def get_html(self):
        html=f'<menu {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</menu >'
        return html
    
class Bdo(Widget):
    def get_html(self):
        html=f'<bdo {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</bdo >'
        return html
    
class B(Widget):
    def get_html(self):
        return '<b>'
    
class Article(Widget):
    def get_html(self):
        return f'<article {self.compile_events()} {self.compile_attributes()}>'

class Aside(Widget):
    def get_html(self):
        return f'<aside {self.compile_events()} {self.compile_attributes()} {self.compile_events} {self.compile_attributes()}>'

class Audio(Widget):
    def get_html(self):
        return f'<audio {self.compile_events()} {self.compile_attributes()}>'

class Bdi(Widget):
    def get_html(self):
        return f'<bdi {self.compile_events()} {self.compile_attributes()}>'

class Canvas(Widget):
    def get_html(self):
        return f'<canvas {self.compile_events()} {self.compile_attributes()}>'

class Datalist(Widget):
    def get_html(self):
        return f'<datalist {self.compile_events()} {self.compile_attributes()}>'

class Details(Widget):
    def get_html(self):
        return f'<details {self.compile_events()} {self.compile_attributes()}>'

class Embed(Widget):
    def get_html(self):
        html=f'<embed {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</embed >'
        return html

class Fieldset(Widget):
    def get_html(self):
        html=f'<fieldset {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</fieldset >'
        return html

class Figcaption(Widget):
    def get_html(self):
        return f'<figcaption {self.compile_events()} {self.compile_attributes()}>'

class Figure(Widget):
    def get_html(self):
        return f'<figure {self.compile_events()} {self.compile_attributes()}>'

class Footer(Widget):
    def get_html(self):
        return f'<footer {self.compile_events()} {self.compile_attributes()}>'

class Form(Widget):
    def get_html(self):
        html=f'<form {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</form >'
        return html

class H1(Widget):
    def get_html(self):
        html=f'<h1 {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</h1 >'
        return html

class H2(Widget):
    def get_html(self):
        html=f'<h2 {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</h2 >'
        return html

class H3(Widget):
    def get_html(self):
        html=f'<h3 {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</h3 >'
        return html

class H4(Widget):
    def get_html(self):
        html=f'<h4 {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</h4 >'
        return html

class H5(Widget):
    def get_html(self):
        html=f'<h4 {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</h4 >'
        return html

class H6(Widget):
    def get_html(self):
        html=f'<h6 {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</h6 >'
        return html

class Header(Widget):
    def get_html(self):
        return f'<header {self.compile_events()} {self.compile_attributes()}>'

class Iframe(Widget):
    def get_html(self):
        html=f'<iframe {self.compile_events()} {self.compile_attributes()}> '
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</iframe >'
        return html

class Input(Widget):
    def get_html(self):
        return f'<input {self.compile_events()} {self.compile_attributes()}/> '

class Keygen(Widget):
    def get_html(self):
        return f'<keygen {self.compile_events()} {self.compile_attributes()}> '

class Legend(Widget):
    def get_html(self):
        html= f'<legend {self.compile_events()} {self.compile_attributes()}>'
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</legend>'
        return html

class Li(Widget):
    def get_html(self):
        html= f'<mark {self.compile_events()} {self.compile_attributes()}>'
        for widget in self.widgets:
            html+=widget.get_html()
        return html

class Link(Widget):
    def get_html(self):
        return f'<link {self.compile_attributes()} >'

class Main(Widget):
    def get_html(self):
        html= f'<main {self.compile_events()} {self.compile_attributes()}>'
        for widget in self.widgets:
            html+=widget.get_html()
        html+='</main>'
        return html

class Mark(Widget):
    def get_html(self):
        html= f'<mark {self.compile_events()} {self.compile_attributes()}>'
        for widget in self.widgets:
            html+=widget.get_html()
        return html
    
class Menuitem(Widget):
    def get_html(self):
        return f'<menuitem {self.compile_events()} {self.compile_attributes()}>'
        
    
class Meter(Widget):
    def get_html(self):
        return f'<meter {self.compile_events()} {self.compile_attributes()}>'

class Nav(Widget):
    def get_html(self):
        return f'<nav {self.compile_events()} {self.compile_attributes()}>'

class Output(Widget):
    def get_html(self):
        return f'<output {self.compile_events()} {self.compile_attributes()}>'

class Progress(Widget):
    def get_html(self):
        return f'<progress {self.compile_events()} {self.compile_attributes()}>'

class Rp(Widget):
    def get_html(self):
        return f'<rp {self.compile_events()} {self.compile_attributes()}>'

class Button(Widget):
    def onclick(self,command):
        if isinstance(command,str):
            self.js=command
        else:self.pyf=command
    def get_html(self):
        self.running=True
        return f'<button {self.compile_events()} {self.compile_attributes()}>{self.text}</button>'
    def set_text(self,text):
        self.text=text
    

class Label(Widget):
    def set_text(self,text):
        self.innertext=text
    def get_html(self):
        return f'<label class = "c{self.ixfwm4d}">{self.innertext}</label>'

class TextArea(Widget):
    def set_text(self,text):
        self.text=text
    def get_html(self):
        return f'<textarea class = "c{self.id}"></textarea>'

