import zhipuai
import json

zhipuai.api_key = "60abe5cc11ce1af33ea6331daf1babde.hEjvmvuC6nGVLv8G"

task_id = ""


def get_chat_res(text):
    question = text
    response = zhipuai.model_api.invoke(
        # model="chatglm_std",
        model="chatglm_lite",
        prompt=[
            {"role": "user", "content": question},
        ],
        temperature=0.95,
        top_p=0.7,
        incremental=True
    )
    print(response['data']['choices'][0]['content'])
    result = response['data']['choices'][0]['content']
    return result


def invoke_example():
    response = zhipuai.model_api.invoke(
        model="chatglm_lite",
        prompt=[{"role": "user", "content": "人工智能"}],
        top_p=0.7,
        temperature=0.9,
    )
    print(response)


def async_invoke_example():
    response = zhipuai.model_api.async_invoke(
        model="chatglm_lite",
        prompt=[{"role": "user", "content": "人工智能"}],
        top_p=0.7,
        temperature=0.9,
    )
    print(response)


'''
  说明：
  add: 事件流开启
  error: 平台服务或者模型异常，响应的异常事件
  interrupted: 中断事件，例如：触发敏感词
  finish: 数据接收完毕，关闭事件流
'''


def sse_invoke_example():
    response = zhipuai.model_api.sse_invoke(
        model="chatglm_lite",
        prompt=[{"role": "user", "content": "人工智能"}],
        top_p=0.7,
        temperature=0.9,
    )

    for event in response.events():
        if event.event == "add":
            print(event.data)
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
        elif event.event == "finish":
            print(event.data)
            print(event.meta)
        else:
            print(event.data)


def query_async_invoke_result_example():
    response = zhipuai.model_api.query_async_invoke_result(task_id)
    print(response)


if __name__ == '__main__':
    # query_async_invoke_result_example()
    print(get_chat_res("你好"))
