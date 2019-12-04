import ui
from objc_util import *
from pprint import pprint


def pPass():
  print('Pass')
def pdbg(obj):
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
WKWebView,WKWebViewConfiguration,NSURLRequest=map(ObjCClass,['WKWebView','WKWebViewConfiguration','NSURLRequest'])


url=nsurl('https://www.apple.com/jp/')



#WKWebView=ObjCClass('WKWebView')

class MainView(ui.View):
  def __init__(self,*args, **kwargs):
    # todo: おまじないになっとる
    super().__init__(self, *args, **kwargs)
    self.bg_color='red'
    f = CGRect(CGPoint(0, 0), CGSize(self.width, self.height))
    flex_width, flex_height = (1<<1), (1<<4)
    
    self.ins=ObjCInstance(self)
    webview=WKWebView.alloc().initWithFrame_(f)
    webview.setAutoresizingMask_(flex_width|flex_height)
    #pdbg(url)
    webview.loadRequest_(NSURLRequest.requestWithURL_(url))
    
    
    self.ins.addSubview_(webview)
    

v=MainView()
v.present()

