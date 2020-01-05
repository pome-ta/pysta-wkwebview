# pysta-wkwebview
[Pythonista](http://omz-software.com/pythonista/) WKWebView test space repository.


# 📝 2020/01/05
過去のものは、customフォルダに移動

## accessory tool bar のカスタマイズ

- `<textarea>` 選択時の状態でプリントデバッグ
- `search_bar.py` として吐出し
- 階層内から探してみる

### 参照
[Objective-Cの黒魔術がよくわからなかったので覗いてみた👻](https://qiita.com/mopiemon/items/8d0dd7d678c4dadeadd4)



# 📝 2019/12/04

~~とりあえず、view で出すことはできた。[Apple の公式ページ](https://www.apple.com/jp/)~~



html ファイルを呼び出す


## 簡単な概要

### `ui.View()`

Pythonista の`ui` モジュールを使い外側を作る。

#### `super().__init__(self, *args, **kwargs)`
objc では、通例的な呼び出しやけど。おまじないなんじゃないか？🤔と思ってる

#### `ObjCInstance(self)`
objc 類の連携のため、Python の`self` (`ui.View()`) をインスタンス化


### `def pdbg(obj)`

objc のprintデバッグ用（白目）

## `ObjCClass`

### `loadRequest_`
`NSURLRequest.requestWithURL_(url)` を噛ませないと死ぬ


### `allowsBackForwardNavigationGestures=1`
swipe で戻れるようにしたけど、多分使わないわ



## 今後の制御系統について
多分、objc だとめんどくさ味あるので、css かjsで対応するかも🤗





---

> The following is the `README.md` 😜

# pysta-wkwebview

Practice WKWebView with Pythonista

[Pythonista](http://omz-software.com/pythonista/) の`objc_util` を使い、Objective-C の理解と、 `WKWebView` の理解ができるようにする。



[mainScript.py](https://github.com/pome-ta/pysta-wkwebview/blob/master/mainScript.py) のmaster branch にcommit しまくってる


## Basic Data
- iPhone
	- iPhone 11 64GB
	- iOS 13.2

- Pythonista
	- ver_3.2

## Giants' shoulders

[youey/youey/wkwebview.py](https://github.com/mikaelho/youey/blob/master/youey/wkwebview.py)


