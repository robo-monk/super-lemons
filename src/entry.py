from js import Response, fetch
import inspect

async def on_fetch(request, env):
    code = (await request.text())
    user_def, caller = code.split("---\n")
    print(user_def, caller)

    loc = {}
    exec(user_def, globals(), loc)
    exec(f"result = {caller.strip()}", globals(), loc)

    result = loc["result"]
    if inspect.iscoroutine(result):
        result = await result

    return Response.new(result)
