# nb_serverproxy_openrefine
Jupyter server proxy for gradio

## jupyter-server-proxy設定
```
def setup_gradio():
    return {
        'command': ['ls'],
        'port': 7860,
        'environment': {},
        'timeout': 120,
        'launcher_entry': {
            'title': 'Gradio',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'gradio.svg')
        }
    }
```
## jupyter-server-proxy運作原理
1. 點擊jupyterlab extension icon啟動
2. 檢查目標port
3. 執行command
4. 導向到目標port

## 由於gradio由notebook啟動，所以無法套用nb-proxy-gradio

## 推薦做法-使用外部連結
```
import gradio as gr
import cv2

def to_black(image):
    output = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return output

interface = gr.Interface(fn=to_black, inputs="image", outputs="image")
interface.launch(share=True)
```
