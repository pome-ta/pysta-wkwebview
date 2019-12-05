import ui
from objc_util import *
from pprint import pprint
import os


def pdbg(obj):
  def pPass():
    print('Pass')
  print('# --- name______')
  try:
    pprint(obj)
  except:
    pPass()
  print('# --- vars( )______')
  try:
    pprint(vars(obj))
  except:
    pPass()
  print('# --- dir( )______')
  try:
    pprint(dir(obj))
  except:
    pPass()
  
  # todo: 落ちる時は落ちる
  print('# --- ivarDescription')
  try:
    pass
    #pprint(obj._ivarDescription())
  except:
    pPass()
  print('# --- shortMethodDescription')
  try:
    pprint(obj._shortMethodDescription())
  except:
    pPass()
  print('# --- methodDescription')
  try:
    pprint(obj._methodDescription())
  except:
    pPass()
  
  print('# --- recursiveDescription')
  try:
    pprint(obj.recursiveDescription())
  except:
    pPass()
  print('# --- autolayoutTrace')
  try:
    pprint(obj._autolayoutTrace())
  except:
    pPass()



# load classes
WKWebView,NSURLRequest=map(ObjCClass,['WKWebView','NSURLRequest'])

path=os.path.abspath('index.html')
url=nsurl(path)



#WKWebView=ObjCClass('WKWebView')

class MainView(ui.View):
  def __init__(self,*args, **kwargs):
    # todo: おまじないになっとる
    super().__init__(self, *args, **kwargs)
    self.bg_color='red'
    f = CGRect(CGPoint(0, 0), CGSize(self.width, self.height))
    flex_width, flex_height = (1<<1), (1<<4)
    
    self.ins=ObjCInstance(self)
    
    self.webview=WKWebView.alloc().initWithFrame_(f)
    self.webview.allowsBackForwardNavigationGestures=1
    
    self.webview.setAutoresizingMask_(flex_width|flex_height)
    #self.webview.setMagnification_centeredAtPoint_(1,1.0)
    #pdbg(url)
    self.webview.loadRequest_(NSURLRequest.requestWithURL_(url))
    
    
    
    self.ins.addSubview_(self.webview)
    
    


v=MainView()
#v.present(hide_title_bar=1)

v.present()
#pdbg(v.webview)
